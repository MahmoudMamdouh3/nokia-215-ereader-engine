"""Sound Experiments - system probe.

Collects hardware / OS / toolchain / storage / network facts for this laptop and writes:

    docs/system_specs.json          machine-readable full report
    docs/SYSTEM_SPECS.md            human + LLM readable report
    configs/hardware_profile.yaml   heuristic tuning knobs derived from the facts

Other tools (and other AI models helping on this repo) should read hardware_profile.yaml
instead of guessing batch sizes, VRAM budgets or worker counts.

Usage:
    python tools/system_probe.py                 # full probe incl. disk + network benchmarks
    python tools/system_probe.py --no-bench      # skip disk write / network throughput tests
    python tools/system_probe.py --drives E D C  # drives to benchmark (default: E D C)

Stdlib only on purpose, so it runs before any virtualenv exists.
"""
from __future__ import annotations

import argparse
import ctypes
import datetime as dt
import json
import os
import platform
import re
import shutil
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DOCS = REPO / "docs"
CONFIGS = REPO / "configs"


# --------------------------------------------------------------------------- helpers
def run(cmd, timeout=60):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout,
                           encoding="utf-8", errors="replace")
        return (r.stdout or "").strip(), (r.stderr or "").strip(), r.returncode
    except Exception as exc:  # noqa: BLE001
        return "", str(exc), -1


def ps_json(expr):
    out, _err, _rc = run(["powershell", "-NoProfile", "-Command",
                          f"{expr} | ConvertTo-Json -Depth 4 -Compress"], timeout=90)
    if not out:
        return None
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return None


def as_list(x):
    if x is None:
        return []
    return x if isinstance(x, list) else [x]


def gb(n):
    return round(float(n) / (1024 ** 3), 2) if n is not None else None


# --------------------------------------------------------------------------- probes
def probe_os():
    d = ps_json("Get-CimInstance Win32_OperatingSystem | Select-Object Caption,Version,BuildNumber,OSArchitecture") or {}
    bios = ps_json("Get-CimInstance Win32_BIOS | Select-Object SMBIOSBIOSVersion,Manufacturer") or {}
    cs = ps_json("Get-CimInstance Win32_ComputerSystem | Select-Object Manufacturer,Model,SystemType") or {}
    long_paths = None
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\FileSystem") as k:
            long_paths = bool(winreg.QueryValueEx(k, "LongPathsEnabled")[0])
    except Exception:  # noqa: BLE001
        pass
    power_out, _, _ = run(["powercfg", "/getactivescheme"])
    batt = ps_json("Get-CimInstance Win32_Battery | Select-Object EstimatedChargeRemaining,BatteryStatus")
    return {
        "os": d, "bios": bios, "computer": cs,
        "python_platform": platform.platform(),
        "long_paths_enabled": long_paths,
        "power_scheme": power_out,
        "battery": batt,
    }


def probe_cpu():
    cpu = as_list(ps_json("Get-CimInstance Win32_Processor | Select-Object Name,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed,CurrentClockSpeed,L2CacheSize,L3CacheSize"))
    feats = {}
    try:
        k32 = ctypes.windll.kernel32
        for name, idx in {"SSE4.2": 38, "AVX": 39, "AVX2": 40, "AVX512F": 41}.items():
            feats[name] = bool(k32.IsProcessorFeaturePresent(idx))
    except Exception:  # noqa: BLE001
        pass
    return {"processors": cpu, "features": feats, "logical_cpus_python": os.cpu_count()}


def probe_memory():
    mods = as_list(ps_json("Get-CimInstance Win32_PhysicalMemory | Select-Object Capacity,Speed,ConfiguredClockSpeed,Manufacturer,PartNumber"))
    osm = ps_json("Get-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize,FreePhysicalMemory,TotalVirtualMemorySize,FreeVirtualMemory") or {}
    page = as_list(ps_json("Get-CimInstance Win32_PageFileUsage | Select-Object Name,AllocatedBaseSize,CurrentUsage"))
    total_kb = osm.get("TotalVisibleMemorySize") or 0
    free_kb = osm.get("FreePhysicalMemory") or 0
    return {
        "modules": mods,
        "total_gb": round(total_kb / 1024 / 1024, 2),
        "free_gb_now": round(free_kb / 1024 / 1024, 2),
        "pagefile": page,
    }


def probe_gpu():
    video = as_list(ps_json("Get-CimInstance Win32_VideoController | Select-Object Name,AdapterRAM,DriverVersion,VideoProcessor"))
    nv = {"present": False}
    full, _, rc = run(["nvidia-smi"])
    if rc == 0 and full:
        nv["present"] = True
        m = re.search(r"CUDA (?:UMD )?Version:\s*([\d.]+)", full)
        nv["cuda_version_driver_supports"] = m.group(1) if m else None
        fields = ("name,memory.total,memory.used,memory.free,driver_version,compute_cap,"
                  "pcie.link.gen.current,pcie.link.gen.max,pcie.link.width.current,"
                  "power.limit,clocks.max.sm,clocks.max.mem,temperature.gpu,utilization.gpu")
        out, _, rc2 = run(["nvidia-smi", f"--query-gpu={fields}", "--format=csv,noheader,nounits"])
        if rc2 != 0 or not out:
            fields = "name,memory.total,memory.used,memory.free,driver_version,compute_cap"
            out, _, _ = run(["nvidia-smi", f"--query-gpu={fields}", "--format=csv,noheader,nounits"])
        keys = fields.split(",")
        gpus = []
        for line in out.splitlines():
            vals = [v.strip() for v in line.split(",")]
            gpus.append(dict(zip(keys, vals)))
        nv["gpus"] = gpus
        nv["nvidia_smi_raw"] = full
    nvcc = None
    if shutil.which("nvcc"):
        nvcc, _, _ = run(["nvcc", "--version"])
    return {"video_controllers": video, "nvidia": nv, "nvcc": nvcc}


def probe_storage(drives, bench):
    vols = as_list(ps_json("Get-Volume | Where-Object DriveLetter | Select-Object DriveLetter,FileSystemLabel,FileSystem,Size,SizeRemaining,DriveType,HealthStatus"))
    phys = as_list(ps_json("Get-PhysicalDisk | Select-Object FriendlyName,MediaType,BusType,Size,HealthStatus"))
    out = {"volumes": [], "physical_disks": phys, "dev_drive": {}}
    for v in vols:
        out["volumes"].append({
            "drive": v.get("DriveLetter"), "label": v.get("FileSystemLabel"), "fs": v.get("FileSystem"),
            "size_gb": gb(v.get("Size")), "free_gb": gb(v.get("SizeRemaining")), "health": v.get("HealthStatus")})
    for d in drives:
        so, _, _ = run(["fsutil", "devdrv", "query", f"{d}:"])
        out["dev_drive"][d] = so or "n/a"
    if bench:
        out["write_bench_mb_s"] = {}
        for d in drives:
            out["write_bench_mb_s"][d] = io_bench(Path(f"{d}:\\"))
    return out


def io_bench(root: Path, size_mb=768):
    tmp = root / "_sound_experiments_iobench"
    try:
        tmp.mkdir(exist_ok=True)
        f = tmp / "bench.bin"
        block = os.urandom(1024 * 1024)
        t0 = time.perf_counter()
        with open(f, "wb", buffering=0) as fh:
            for _ in range(size_mb):
                fh.write(block)
            os.fsync(fh.fileno())
        return round(size_mb / (time.perf_counter() - t0), 1)
    except Exception as exc:  # noqa: BLE001
        return f"error: {exc}"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def probe_network(bench):
    res = {"tcp_connect_ms": {}}
    for host in ("www.youtube.com", "archive.org", "huggingface.co", "pypi.org", "github.com"):
        t0 = time.perf_counter()
        try:
            s = socket.create_connection((host, 443), timeout=6)
            s.close()
            res["tcp_connect_ms"][host] = round((time.perf_counter() - t0) * 1000, 1)
        except Exception as exc:  # noqa: BLE001
            res["tcp_connect_ms"][host] = f"error: {exc}"
    if bench:
        try:
            t0 = time.perf_counter()
            n = 0
            req = urllib.request.Request("https://speed.cloudflare.com/__down?bytes=25000000",
                                         headers={"User-Agent": "Mozilla/5.0 (SoundExperiments system_probe)"})
            with urllib.request.urlopen(req, timeout=40) as r:
                while True:
                    chunk = r.read(1 << 16)
                    if not chunk:
                        break
                    n += len(chunk)
            res["download_mbit_s"] = round(n * 8 / (time.perf_counter() - t0) / 1e6, 1)
        except Exception as exc:  # noqa: BLE001
            res["download_mbit_s"] = f"error: {exc}"
    res["interfaces"] = as_list(ps_json("Get-NetConnectionProfile | Select-Object Name,InterfaceAlias,IPv4Connectivity"))
    return res


TOOLS = {
    "python": ["--version"], "pip": ["--version"], "uv": ["--version"], "git": ["--version"],
    "ffmpeg": ["-version"], "ffprobe": ["-version"], "yt-dlp": ["--version"], "aria2c": ["--version"],
    "node": ["--version"], "deno": ["--version"], "fpcalc": ["-version"], "sox": ["--version"],
    "cmake": ["--version"], "7z": [], "winget": ["--version"], "conda": ["--version"],
}


def probe_toolchain():
    tools = {}
    for name, args in TOOLS.items():
        path = shutil.which(name)
        if not path:
            tools[name] = None
            continue
        ver = ""
        if args:
            so, se, _ = run([path, *args], timeout=20)
            ver = (so or se).splitlines()[0] if (so or se) else ""
        tools[name] = {"path": path, "version": ver}
    hw = ""
    if tools.get("ffmpeg"):
        hw, _, _ = run(["ffmpeg", "-hide_banner", "-hwaccels"])
    pk, _, _ = run([sys.executable, "-m", "pip", "list", "--format=json"], timeout=90)
    try:
        pkgs = {p["name"].lower(): p["version"] for p in json.loads(pk)}
    except Exception:  # noqa: BLE001
        pkgs = {}
    interesting = ("torch", "torchaudio", "numpy", "scipy", "librosa", "soundfile", "gradio", "yt-dlp",
                   "faster-whisper", "whisperx", "pyannote.audio", "speechbrain", "demucs", "audio-separator",
                   "faiss-cpu", "faiss-gpu", "onnxruntime", "onnxruntime-gpu", "transformers", "pysubs2",
                   "webrtcvad-wheels", "datasketch", "sqlalchemy", "typer", "pydantic")
    return {"tools": tools, "ffmpeg_hwaccels": hw, "python_executable": sys.executable,
            "python_version": platform.python_version(),
            "packages_of_interest": {k: pkgs.get(k) for k in interesting},
            "total_installed_packages": len(pkgs)}


# --------------------------------------------------------------------------- recommendations
def recommendations(spec):
    gpus = spec["gpu"]["nvidia"].get("gpus") or [{}]
    g0 = gpus[0] if gpus else {}

    def num(v, default=0.0):
        try:
            return float(v)
        except (TypeError, ValueError):
            return default

    vram_total = num(g0.get("memory.total"))
    vram_used = num(g0.get("memory.used"))
    vram_free = max(vram_total - vram_used, 0)
    logical = spec["cpu"]["logical_cpus_python"] or 8
    ram = spec["memory"]["total_gb"] or 8
    return {
        "generated_by": "tools/system_probe.py (heuristics - validate with real benchmarks)",
        "gpu": {
            "name": g0.get("name"),
            "vram_total_mib": vram_total,
            "vram_idle_free_mib": vram_free,
            "vram_budget_mib": int(vram_free * 0.85),
            "max_concurrent_gpu_jobs": 1,
            "note": "Laptop dGPU shares VRAM with the desktop compositor; load ONE heavy model at a time.",
        },
        "cpu": {
            "logical_cpus": logical,
            "io_workers": max(2, min(8, logical // 2)),
            "cpu_workers": max(2, logical - 6),
            "note": "Keep ~4-6 logical CPUs free for the UI, OS and the GPU feeder thread.",
        },
        "memory": {
            "total_gb": ram,
            "free_gb_at_probe": spec["memory"]["free_gb_now"],
            "pipeline_ram_budget_gb_ceiling": round(ram * 0.6, 1),
            "audio_chunk_minutes": 20 if ram <= 16 else 40,
            "note": ("Only ~16 GB RAM and usually much less is free (browser/IDE/Windows). Treat the budget as a "
                     "CEILING: at runtime use min(ceiling, available_ram - 2 GB). Stream/chunk long audio."),
        },
        "models": {
            "whisper": {"model": "large-v3",
                        "compute_type": "int8_float16" if vram_total <= 8200 else "float16",
                        "batch_size": 8 if vram_total <= 8200 else 16},
            "separation": {"preferred": ["bs_roformer", "mel_band_roformer", "htdemucs_ft"],
                           "segment_overlap": 0.25, "fp16": True},
            "diarization": {"device": "cuda", "batch_size": 16},
            "embedding": {"device": "cuda", "batch_size": 64},
        },
        "storage": {
            "volumes_gb_free": {v["drive"]: v["free_gb"] for v in spec["storage"]["volumes"]},
            "raw_budget_gb_on_E": 55,
            "keep_free_gb_on_E": 12,
            "note": "E: is a 100 GB ReFS Dev Drive; use D: (and C: sparingly) for derived data and model caches.",
        },
    }


def scalar(v):
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    return '"' + str(v).replace('"', "'") + '"'


def to_yaml(obj, indent=0):
    pad = "  " * indent
    lines = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)) and v:
                lines.append(f"{pad}{k}:")
                lines.append(to_yaml(v, indent + 1))
            else:
                lines.append(f"{pad}{k}: {scalar(v)}")
    elif isinstance(obj, list):
        for v in obj:
            if isinstance(v, (dict, list)):
                lines.append(f"{pad}-")
                lines.append(to_yaml(v, indent + 1))
            else:
                lines.append(f"{pad}- {scalar(v)}")
    return "\n".join(lines)


# --------------------------------------------------------------------------- markdown
def render_md(spec):
    cpu = (spec["cpu"]["processors"] or [{}])[0]
    cs = spec["os"]["computer"]
    osd = spec["os"]["os"]
    g = spec["gpu"]["nvidia"]
    gpus = g.get("gpus") or []
    L = []
    a = L.append
    a("# SYSTEM SPECS")
    a("")
    a(f"_Generated {spec['generated_at']} by `tools/system_probe.py`. Re-run it whenever hardware or drivers change._")
    a("")
    a("> **For any AI model / tool tuning code for this laptop:** read `configs/hardware_profile.yaml` for ready-made "
      "limits (VRAM budget, worker counts, chunk sizes). The hard constraints are summarised below.")
    a("")
    a("## Hard constraints (read first)")
    a("")
    vram = gpus[0].get("memory.total") if gpus else "?"
    a(f"- **GPU VRAM is {vram} MiB (8 GB-class laptop GPU).** One heavy model at a time. Use fp16/int8.")
    a(f"- **System RAM is {spec['memory']['total_gb']} GB.** Chunk long audio; no whole-archive in-memory ops.")
    vols = {v["drive"]: v for v in spec["storage"]["volumes"]}
    a(f"- **E: (repo + raw dataset) has only {vols.get('E', {}).get('free_gb')} GB free** of "
      f"{vols.get('E', {}).get('size_gb')} GB (ReFS Dev Drive). D: has {vols.get('D', {}).get('free_gb')} GB free, "
      f"C: has {vols.get('C', {}).get('free_gb')} GB free.")
    a("- Laptop thermals: sustained GPU jobs throttle; keep plugged in, use the High performance power plan for long runs.")
    a("")
    a("## Machine")
    a("")
    a("| Item | Value |")
    a("|---|---|")
    a(f"| Model | {cs.get('Manufacturer')} {cs.get('Model')} |")
    a(f"| OS | {osd.get('Caption')} (build {osd.get('BuildNumber')}, {osd.get('OSArchitecture')}) |")
    a(f"| BIOS | {spec['os']['bios'].get('SMBIOSBIOSVersion')} |")
    a(f"| Long paths enabled | {spec['os']['long_paths_enabled']} |")
    a(f"| Power scheme | {spec['os']['power_scheme']} |")
    a("")
    a("## CPU")
    a("")
    a(f"- {cpu.get('Name')} - {cpu.get('NumberOfCores')} cores / {cpu.get('NumberOfLogicalProcessors')} threads, "
      f"max {cpu.get('MaxClockSpeed')} MHz, L2 {cpu.get('L2CacheSize')} KB, L3 {cpu.get('L3CacheSize')} KB")
    a(f"- ISA features: {', '.join(k for k, v in spec['cpu']['features'].items() if v) or 'n/a'}")
    a("")
    a("## Memory")
    a("")
    a(f"- Total {spec['memory']['total_gb']} GB, free at probe time {spec['memory']['free_gb_now']} GB")
    for m in spec["memory"]["modules"]:
        a(f"- Module: {gb(m.get('Capacity'))} GB @ {m.get('Speed')} MT/s ({m.get('Manufacturer')})")
    a("")
    a("## GPU")
    a("")
    for v in spec["gpu"]["video_controllers"]:
        a(f"- {v.get('Name')} (driver {v.get('DriverVersion')})")
    if gpus:
        a("")
        a("| NVIDIA field | Value |")
        a("|---|---|")
        for k, v in gpus[0].items():
            a(f"| {k} | {v} |")
        a(f"| CUDA version supported by driver | {g.get('cuda_version_driver_supports')} |")
        a(f"| nvcc | {'installed' if spec['gpu']['nvcc'] else 'not installed (not needed for PyTorch wheels)'} |")
        a("")
        a("_PCIe generation, clocks, temperature and utilisation are idle-state snapshots (the link downclocks "
          "to gen 1 at idle and boosts to gen 4 under load). The Intel iGPU drives the display; CUDA only sees the NVIDIA GPU._")
    a("")
    a("## Storage")
    a("")
    a("| Drive | Label | FS | Size GB | Free GB | Sequential write MB/s |")
    a("|---|---|---|---|---|---|")
    wb = spec["storage"].get("write_bench_mb_s", {})
    for v in spec["storage"]["volumes"]:
        a(f"| {v['drive']}: | {v['label'] or ''} | {v['fs']} | {v['size_gb']} | {v['free_gb']} | {wb.get(v['drive'], 'n/a')} |")
    a("")
    for p in spec["storage"]["physical_disks"]:
        a(f"- Physical disk: {p.get('FriendlyName')} - {p.get('MediaType')} / {p.get('BusType')} - {gb(p.get('Size'))} GB")
    a("")
    a("## Network")
    a("")
    net = spec["network"]
    a(f"- Download throughput: **{net.get('download_mbit_s', 'not measured')} Mbit/s**")
    for h, v in net["tcp_connect_ms"].items():
        a(f"- TCP connect {h}: {v} ms")
    a("")
    a("## Toolchain")
    a("")
    a("| Tool | Version / path |")
    a("|---|---|")
    for k, v in spec["toolchain"]["tools"].items():
        a(f"| {k} | {(v['version'] + ' - ' + v['path']) if v else 'NOT FOUND'} |")
    a("")
    a(f"- Python in use: {spec['toolchain']['python_version']} (`{spec['toolchain']['python_executable']}`)")
    a("- Packages of interest in the *global* interpreter (a dedicated venv is planned, see implementation plan):")
    for k, v in spec["toolchain"]["packages_of_interest"].items():
        a(f"  - {k}: {v or 'not installed'}")
    a("")
    a("## Derived tuning profile (heuristic)")
    a("")
    a("```yaml")
    a(to_yaml(spec["recommendations"]))
    a("```")
    a("")
    return "\n".join(L)


# --------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-bench", action="store_true", help="skip disk write + network throughput benchmarks")
    ap.add_argument("--drives", nargs="*", default=["E", "D", "C"])
    args = ap.parse_args()
    bench = not args.no_bench

    print("[1/7] OS / BIOS / power ...")
    spec = {"generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
            "os": probe_os()}
    print("[2/7] CPU ...")
    spec["cpu"] = probe_cpu()
    print("[3/7] Memory ...")
    spec["memory"] = probe_memory()
    print("[4/7] GPU ...")
    spec["gpu"] = probe_gpu()
    print(f"[5/7] Storage (bench={bench}) ...")
    spec["storage"] = probe_storage(args.drives, bench)
    print(f"[6/7] Network (bench={bench}) ...")
    spec["network"] = probe_network(bench)
    print("[7/7] Toolchain ...")
    spec["toolchain"] = probe_toolchain()
    spec["recommendations"] = recommendations(spec)

    DOCS.mkdir(parents=True, exist_ok=True)
    CONFIGS.mkdir(parents=True, exist_ok=True)
    (DOCS / "system_specs.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False), encoding="utf-8")
    (DOCS / "SYSTEM_SPECS.md").write_text(render_md(spec), encoding="utf-8")
    (CONFIGS / "hardware_profile.yaml").write_text(
        "# Auto-generated by tools/system_probe.py - heuristic tuning knobs for this laptop.\n"
        + to_yaml(spec["recommendations"]) + "\n", encoding="utf-8")
    print(f"Wrote {DOCS / 'SYSTEM_SPECS.md'}")
    print(f"Wrote {DOCS / 'system_specs.json'}")
    print(f"Wrote {CONFIGS / 'hardware_profile.yaml'}")


if __name__ == "__main__":
    main()
