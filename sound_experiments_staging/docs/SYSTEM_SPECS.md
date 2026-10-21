# SYSTEM SPECS

_Generated 2026-10-21T20:00:40+03:00 by `tools/system_probe.py`. Re-run it whenever hardware or drivers change._

> **For any AI model / tool tuning code for this laptop:** read `configs/hardware_profile.yaml` for ready-made limits (VRAM budget, worker counts, chunk sizes). The hard constraints are summarised below.

## Hard constraints (read first)

- **GPU VRAM is 8188 MiB (8 GB-class laptop GPU).** One heavy model at a time. Use fp16/int8.
- **System RAM is 15.73 GB.** Chunk long audio; no whole-archive in-memory ops.
- **E: (repo + raw dataset) has only 83.84 GB free** of 99.94 GB (ReFS Dev Drive). D: has 285.1 GB free, C: has 138.2 GB free.
- Laptop thermals: sustained GPU jobs throttle; keep plugged in, use the High performance power plan for long runs.

## Machine

| Item | Value |
|---|---|
| Model | LENOVO 82YA |
| OS | Microsoft Windows 11 Home (build 26300, 64-bit) |
| BIOS | M2CN32WW |
| Long paths enabled | True |
| Power scheme | Power Scheme GUID: 381b4222-f694-41f0-9685-ff5bb260df2e  (Balanced) |

## CPU

- 13th Gen Intel(R) Core(TM) i7-13700H - 14 cores / 20 threads, max 2400 MHz, L2 11776 KB, L3 24576 KB
- ISA features: SSE4.2, AVX, AVX2

## Memory

- Total 15.73 GB, free at probe time 0.82 GB
- Module: 8.0 GB @ 5600 MT/s (Samsung)
- Module: 8.0 GB @ 5600 MT/s (Samsung)

## GPU

- Intel(R) Iris(R) Xe Graphics (driver 32.0.101.6790)
- NVIDIA GeForce RTX 4060 Laptop GPU (driver 32.0.16.1692)

| NVIDIA field | Value |
|---|---|
| name | NVIDIA GeForce RTX 4060 Laptop GPU |
| memory.total | 8188 |
| memory.used | 1765 |
| memory.free | 6192 |
| driver_version | 616.92 |
| compute_cap | 8.9 |
| pcie.link.gen.current | 2 |
| pcie.link.gen.max | 4 |
| pcie.link.width.current | 8 |
| power.limit | [N/A] |
| clocks.max.sm | 3105 |
| clocks.max.mem | 8001 |
| temperature.gpu | 47 |
| utilization.gpu | 38 |
| CUDA version supported by driver | 13.4 |
| nvcc | not installed (not needed for PyTorch wheels) |

_PCIe generation, clocks, temperature and utilisation are idle-state snapshots (the link downclocks to gen 1 at idle and boosts to gen 4 under load). The Intel iGPU drives the display; CUDA only sees the NVIDIA GPU._

## Storage

| Drive | Label | FS | Size GB | Free GB | Sequential write MB/s |
|---|---|---|---|---|---|
| E: | Dev Drive 1 | ReFS | 99.94 | 83.84 | 580.4 |
| C: |  | NTFS | 953.13 | 138.2 | 1164.2 |
| D: | SSD2 | NTFS | 464.76 | 285.1 | 754.6 |

- Physical disk: Msft Virtual Disk - SSD / File Backed Virtual - 100.0 GB
- Physical disk: SAMSUNG MZVL21T0HCLR-00BL2 - SSD / NVMe - 953.87 GB
- Physical disk: Samsung SSD 980 500GB - SSD / NVMe - 465.76 GB

## Network

- Download throughput: **26.9 Mbit/s**
- TCP connect www.youtube.com: 74.1 ms
- TCP connect archive.org: 211.2 ms
- TCP connect huggingface.co: 16.1 ms
- TCP connect pypi.org: 63.1 ms
- TCP connect github.com: 77.0 ms

## Toolchain

| Tool | Version / path |
|---|---|
| python | Python 3.10.6 - C:\Users\mahmo\AppData\Local\Programs\Python\Python310\python.EXE |
| pip | pip 26.0.1 from C:\Users\mahmo\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10) - C:\Users\mahmo\AppData\Local\Programs\Python\Python310\Scripts\pip.EXE |
| uv | uv 0.11.26 (396ef7ce4 2026-06-30 x86_64-pc-windows-msvc) - C:\Users\mahmo\.local\bin\uv.EXE |
| git | git version 2.56.0.windows.2 - C:\Program Files\Git\cmd\git.EXE |
| ffmpeg | ffmpeg version 9.0.2-full_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg developers - C:\Users\mahmo\AppData\Local\Microsoft\WinGet\Links\ffmpeg.EXE |
| ffprobe | ffprobe version 9.0.2-full_build-www.gyan.dev Copyright (c) 2007-2026 the FFmpeg developers - C:\Users\mahmo\AppData\Local\Microsoft\WinGet\Links\ffprobe.EXE |
| yt-dlp | 2026.08.19 - C:\Users\mahmo\AppData\Local\Microsoft\WinGet\Links\yt-dlp.EXE |
| aria2c | aria2 version 1.37.0 - C:\Users\mahmo\AppData\Local\Microsoft\WinGet\Links\aria2c.EXE |
| node | v26.8.1 - C:\Program Files\nodejs\node.EXE |
| deno | deno 2.9.7 (stable, release, x86_64-pc-windows-msvc) - C:\Users\mahmo\AppData\Local\Microsoft\WinGet\Links\deno.EXE |
| fpcalc | NOT FOUND |
| sox | NOT FOUND |
| cmake | cmake version 4.4.4 - C:\Program Files\CMake\bin\cmake.EXE |
| 7z | NOT FOUND |
| winget | v1.29.380 - C:\Users\mahmo\AppData\Local\Microsoft\WindowsApps\winget.EXE |
| conda | NOT FOUND |

- Python in use: 3.10.6 (`C:\Users\mahmo\AppData\Local\Programs\Python\Python310\python.exe`)
- Packages of interest in the *global* interpreter (a dedicated venv is planned, see implementation plan):
  - torch: not installed
  - torchaudio: not installed
  - numpy: 2.2.6
  - scipy: not installed
  - librosa: not installed
  - soundfile: 0.13.1
  - gradio: not installed
  - yt-dlp: not installed
  - faster-whisper: not installed
  - whisperx: not installed
  - pyannote.audio: not installed
  - speechbrain: not installed
  - demucs: not installed
  - audio-separator: not installed
  - faiss-cpu: not installed
  - faiss-gpu: not installed
  - onnxruntime: not installed
  - onnxruntime-gpu: not installed
  - transformers: not installed
  - pysubs2: 1.8.1
  - webrtcvad-wheels: 2.0.14.post1
  - datasketch: not installed
  - sqlalchemy: not installed
  - typer: not installed
  - pydantic: 2.13.4

## Derived tuning profile (heuristic)

```yaml
generated_by: "tools/system_probe.py (heuristics - validate with real benchmarks)"
gpu:
  name: "NVIDIA GeForce RTX 4060 Laptop GPU"
  vram_total_mib: 8188.0
  vram_idle_free_mib: 6423.0
  vram_budget_mib: 5459
  max_concurrent_gpu_jobs: 1
  note: "Laptop dGPU shares VRAM with the desktop compositor; load ONE heavy model at a time."
cpu:
  logical_cpus: 20
  io_workers: 8
  cpu_workers: 14
  note: "Keep ~4-6 logical CPUs free for the UI, OS and the GPU feeder thread."
memory:
  total_gb: 15.73
  free_gb_at_probe: 0.82
  pipeline_ram_budget_gb_ceiling: 9.4
  audio_chunk_minutes: 20
  note: "Only ~16 GB RAM and usually much less is free (browser/IDE/Windows). Treat the budget as a CEILING: at runtime use min(ceiling, available_ram - 2 GB). Stream/chunk long audio."
models:
  whisper:
    model: "large-v3"
    compute_type: "int8_float16"
    batch_size: 8
  separation:
    preferred:
      - "bs_roformer"
      - "mel_band_roformer"
      - "htdemucs_ft"
    segment_overlap: 0.25
    fp16: true
  diarization:
    device: "cuda"
    batch_size: 16
  embedding:
    device: "cuda"
    batch_size: 64
storage:
  volumes_gb_free:
    E: 83.84
    C: 138.2
    D: 285.1
  raw_budget_gb_on_E: 55
  keep_free_gb_on_E: 12
  note: "E: is a 100 GB ReFS Dev Drive; use D: (and C: sparingly) for derived data and model caches."
```
