# Sound Experiments

A personal lab for audio-AI projects: voice datasets, voice conversion / cloning, synthesized and
corrected singing voices, AI music generation - all built on one shared, hardware-aware core library
(`soundlab`).

> **Status:** planning complete, implementation not started. Start with
> [`docs/IMPLEMENTATION_PLAN.md`](docs/IMPLEMENTATION_PLAN.md).

## Projects

| # | Project | Status | Goal |
|---|---|---|---|
| 01 | **Kobe Bryant voice dataset** | Planned | Discover, verify, de-duplicate and curate every obtainable recording of one speaker into a raw archive + RVC-ready training exports, with a Gradio review/operations UI |
| 02 | Voice cloning lab | Idea | RVC training/inference harness, A/B listening tests, objective similarity metrics |
| 03 | Singing studio | Idea | "Sing beautifully without being a singer": F0 extraction -> pitch correction -> voice conversion -> denoise -> mastering, in an app |
| 04 | Music generation | Idea | Text/melody-to-music experiments |

## Documents

| Doc | What it is |
|---|---|
| [`docs/IMPLEMENTATION_PLAN.md`](docs/IMPLEMENTATION_PLAN.md) | Scope, decisions, storage budget, phases with acceptance criteria, risks, open questions |
| [`docs/SOFTWARE_DESIGN.md`](docs/SOFTWARE_DESIGN.md) | Architecture, pipeline contracts, data model, module designs, dedup guarantee, UI, testing, tech choices |
| [`docs/PARALLEL_ARCHITECTURE.md`](docs/PARALLEL_ARCHITECTURE.md) | High-throughput concurrent execution model, 4-worker threadpool, SQLite WAL concurrency, dedicated GPU stream |
| [`docs/SYSTEM_SPECS.md`](docs/SYSTEM_SPECS.md) | This laptop's measured hardware / drivers / toolchain / storage / network |
| [`docs/system_specs.json`](docs/system_specs.json) | Same facts, machine-readable |
| [`configs/hardware_profile.yaml`](configs/hardware_profile.yaml) | Ready-made tuning knobs (VRAM budget, workers, chunk sizes) derived from the specs |

## The machine in one paragraph

Lenovo 82YA - i7-13700H (14C/20T), **16 GB RAM**, RTX 4060 Laptop **8 GB VRAM**, Windows 11.
`E:` is a **100 GB** ReFS Dev Drive (repo + raw archive), `D:` has ~285 GB free (derived data, models, venv).
Regenerate everything about it with `python tools/system_probe.py`.

## Layout

```text
Sound Experiments/
|- docs/  configs/  tools/  src/soundlab/  projects/  apps/  tests/
\- Kobe bryant Database raw/     raw archive (git-ignored)
```

Full tree and module responsibilities: see `docs/SOFTWARE_DESIGN.md` section 4.

## Quick start (available now)

```powershell
python tools\system_probe.py            # refresh docs\SYSTEM_SPECS.md + configs\hardware_profile.yaml
python tools\system_probe.py --no-bench # same, without disk/network benchmarks
```

The pipeline, CLI (`soundlab ...`) and web UI (`http://127.0.0.1:7860`) arrive with Phases 0-6 of the plan.

## Source coverage & ingestion

The ingestion engine is designed for exhaustive collection across all available sources:
- **Streaming & video platforms:** YouTube, Vimeo, Dailymotion, Internet Archive (Wayback / audiovisual collections).
- **Audio & podcast feeds:** Apple Podcasts, Spotify public feeds, RSS feeds, SoundCloud, radio archives.
- **Broadcast, TV & Film:** Post-game press conferences, documentary audio tracks, film appearances, award ceremonies, sideline interviews.
- **Direct & local media:** Direct media URLs, web rips, local file inbox (`inbox/` directory) for batch ingestion.


## Notes on scope

- RVC quality saturates well before "all the audio exists". The raw archive stays exhaustive; exports are the curated best N hours.
- A dataset of Kobe **speaking** yields a **speaking-voice** model. It will not sing convincingly outside its pitch range.
  For the singing studio, plan to add singing data (including your own voice).
