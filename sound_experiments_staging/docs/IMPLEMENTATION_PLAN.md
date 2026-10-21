# Implementation Plan - Kobe Bryant Voice Dataset

**Project 01 of _Sound Experiments_** | Status: **DRAFT v1 - awaiting your review** | Written 2026-10-21

> Read together with [`SOFTWARE_DESIGN.md`](SOFTWARE_DESIGN.md) (how it is built) and
> [`SYSTEM_SPECS.md`](SYSTEM_SPECS.md) (the laptop this is tuned to).

---

## 1. Objective

Build the most complete, verified, de-duplicated archive of **Kobe Bryant's own voice** that can be
found online, stored raw at `E:\Sound Experiments\Kobe bryant Database raw`, and from it derive a
curated, clean training set for **retrieval-based voice conversion (RVC)**.

Three deliverables, in priority order:

1. **The raw archive** - original, untouched audio files plus a catalog (SQLite) that says, for every
   file, who speaks when, how clean it is, whether it is a duplicate and why.
2. **A web app (Gradio)** to run the pipeline, review uncertain cases by ear, inspect duplicates, and
   export datasets.
3. **Reusable `soundlab` library + tools** so later projects (voice cloning, singing studio, music
   generation) reuse the same audio I/O, storage, quality and dedup code.

## 2. What "every recording" means (scope)

**In scope** - any publicly reachable audio/video where Kobe speaks, in any language:

| Category | Examples of what the discovery engine will hunt |
|---|---|
| Interviews | TV/radio/podcast/sit-down, all eras 1996-2020, English / Italian / Spanish / other |
| Press & ceremonies | Post-game pressers, draft day, retirement speech, jersey retirement, award speeches, Oscar speech |
| Narration & studio work | "Dear Basketball", documentary narration, audiobooks/podcasts he voiced, ads/commercials |
| Film / TV / games | Cameos, "as himself" appearances, voice lines in games (via filmography seed lists) |
| Music / misc | Any recorded rap/vocal work, behind-the-scenes, motivational talks, panels |
| Movie / Documentary Extractions | Full audio extraction from films, series, sports documentaries, and specials |
| Local imports | Bulk drop directory (`inbox/` folder) for manual dumps, rips, and external archives |

**Scope:** Exhaustive acquisition across all indexed internet sources, video platforms, audio streaming channels, podcast feeds, public archives, and imported media files.


**Honest limit:** nobody can prove they found *every* recording. The plan therefore **measures coverage**
(capture-recapture estimate across independent discovery strategies, see 6.1) and reports a number
instead of claiming 100 %.

## 3. Ground truth about this machine

From the probe in `SYSTEM_SPECS.md` (full detail + benchmarks in that file):

| Resource | Value | Consequence for the plan |
|---|---|---|
| CPU | i7-13700H, 14 cores / 20 threads | Good for parallel I/O, fingerprinting, ffmpeg. Leave 4-6 threads free. |
| RAM | **16 GB** DDR5-5600 (2x8) | Stream / chunk long audio (20-min windows); never load whole archives. |
| GPU | RTX 4060 Laptop, **8 GB VRAM** (CC 8.9), driver CUDA 13.4 | **One** heavy model at a time; fp16 / int8; Whisper large-v3 in int8_float16 fits. |
| E: | **100 GB ReFS Dev Drive, ~84 GB free** | Raw archive target. **Tight** - see storage plan. |
| D: | 465 GB NVMe, ~285 GB free | Derived data, model caches, venv. |
| C: | 953 GB NVMe, ~138 GB free | Avoid for bulk data. |
| Python | global 3.10.6, no torch | Create a dedicated venv (never touch global packages). |
| Tools present | ffmpeg 9.0.2, yt-dlp 2026.08.19, aria2c 1.37, git, Node, **Deno 2.9**, **uv 0.11**, CMake | Missing: Chromaprint `fpcalc` (installed in Phase 0). |
| Network | Wi-Fi, measured **~27 Mbit/s (~3.4 MB/s)** | 60 GB of audio is ~5 h of pure transfer; throttle politely; everything resumable. |

> **Important:** you said space does not matter, but `E:` only has ~84 GB free. The plan keeps
> your requested raw location on `E:` and uses a **storage manager that spills to `D:`** automatically
> so the pipeline never fills the drive. Details in Section 5.

## 4. Key design decisions

| # | Decision | Why |
|---|---|---|
| D1 | **Keep raw files byte-exact and immutable.** All analysis runs on scratch copies on `D:`. | Raw must stay a trustworthy source of truth; re-processing with better models later costs nothing. |
| D2 | **Download audio-only (best audio stream), original codec, no re-encode.** | ~55 MB/hour (Opus/AAC ~128 kbps) vs GBs for video. No quality loss. |
| D3 | **Download -> verify -> keep-or-purge loop.** A source is kept in full only if it contains >= N minutes of Kobe speech; otherwise only metadata is stored. | Most search hits are highlight reels/music with no Kobe speech. This saves most of the disk. |
| D4 | **Speaker verification is the heart of the system**, not scraping. Diarization + embedding ensemble + era-aware prototypes + calibrated thresholds + human review of the gray zone. | Videos contain interviewers, crowds, commentators, **impersonators** and **AI fakes**. Wrong speaker = poisoned RVC model. |
| D5 | **Era-aware voice model.** Separate prototypes for teen/early (1996-99), prime (2000-07), mid (2008-15), post-retirement (2016-20). | A teenage Kobe and a 40-year-old Kobe differ; a single centroid would reject real early clips. |
| D6 | **Synthetic-voice detector as a hard filter.** | YouTube is full of RVC "Kobe" covers and TTS fakes; training on them would be circular. |
| D7 | **Multi-layer de-duplication with a "keep-best" policy**, never delete, only quarantine (reversible), plus a benchmark and a verifier script. | Re-uploads, re-encodes, clips, speed changes, music beds. See Section 7. |
| D8 | **SQLite catalog (WAL) is the single source of truth.** Idempotent resumable stages; no hidden state. | Crash-safe, inspectable, scriptable, trivially backed up. |
| D9 | **Gradio** for the UI (native audio / waveform / dataframe components, runs on localhost, LAN optional). | Fastest route to a rich audio review tool; matches the "test it on the web" requirement. |
| D10 | **Dedicated Python 3.11 venv on `D:` via `uv`**, pinned lockfile after a smoke test. | Global env has numpy 2.x and no torch; isolation avoids dependency fights. |
| D11 | **Pilot before mass download**: run Phases 1-4 on ~200 candidate videos, measure precision/yield/GB-per-hour, then scale. | Prevents burning days and disk on a mis-tuned pipeline. |
| D12 | **Separation / enhancement is non-destructive and evaluated, not assumed.** Both versions kept; export profile chooses. | Over-processing creates artifacts that RVC learns. Ablate on listening + metrics. |
| D13 | **No gated models, no tokens.** Diarization via `sherpa-onnx` (ONNX segmentation + ungated speaker-embedding model), fallback: Silero VAD + sliding-window ECAPA embeddings + agglomerative clustering. | You chose to skip pyannote. Both options are ungated, Windows-friendly and run on CPU or GPU. Validated head-to-head in the Phase 0/3 pilot. |

## 5. Storage plan (the part that can bite)

```text
E:\Sound Experiments\                       (repo, ~1 GB, git)
E:\Sound Experiments\Kobe bryant Database raw\   <- RAW ARCHIVE (budget <= 60 GB, hard stop at 12 GB free)
    sources\<platform>\<id>\audio.<ext>     original download, never modified
    _catalog\catalog.sqlite (+ WAL)         the database
    _manifests\                              daily JSONL exports + checksums (also copied to D:)
    _quarantine\duplicates\                  reversible dedupe moves
    inbox\                                   drop your own files here
D:\SoundExperiments\                        (derived, budget <= 150 GB)
    venv\  models\ (HF + torch caches)  scratch\  derived\  exports\
```

* **Budget guard:** before every download the storage manager checks free space. At `E:` free < 12 GB
  it switches the *physical* location of new raw files to `D:\SoundExperiments\raw_overflow\` and records
  the real path in the catalog (the catalog, not the folder tree, is authoritative). No symlink tricks.
* **Rough sizing** (to be replaced by pilot numbers): 60 GB of Opus/AAC audio ~ 1,000 source-hours.
  Kobe-speech content is a small fraction of that; D3 (purge-if-no-Kobe) keeps this affordable.
* **Derived data** (separated vocals, enhanced audio, 48 kHz FLAC slices, embeddings) lives on `D:`.

## 6. Phases

Effort: S = hours, M = a day or two, L = several days. Each phase ends with a demo + acceptance check.

### Phase 0 - Foundations (M)
- Repo skeleton, `pyproject.toml`, lint/test tooling, `.gitignore` (data never in git).
- `tools/system_probe.py` -> `SYSTEM_SPECS.md`, `hardware_profile.yaml` (**done in this commit**).
- Install: Python 3.11 venv on `D:` via the already-installed `uv`, PyTorch (CUDA build), faster-whisper, sherpa-onnx, SpeechBrain,
  audio-separator (UVR/RoFormer models), DeepFilterNet, PANNs, FAISS-CPU, datasketch, Gradio, Typer,
  SQLAlchemy, Chromaprint `fpcalc` (the JS runtime yt-dlp needs is already present: Deno and Node).
- No Hugging Face token needed (decision D13): every selected model is publicly downloadable.
- GPU smoke test + VRAM/throughput benchmark -> refine `hardware_profile.yaml`.
- Catalog schema + storage manager + job runner with unit tests.
- **Acceptance:** `soundlab doctor` passes (GPU visible, ffmpeg, yt-dlp, fpcalc, HF auth, free-space guard).

### Phase 1 - Discovery engine (M)
Goal: a large, scored **candidate list** (metadata only, no downloads yet).
- Seed sources: filmography/events/interviewer lists, official channels, podcasts (RSS), Internet Archive,
  Wikimedia Commons, social platforms reachable by yt-dlp.
- **Query expansion:** templates x years x events x interviewers x languages x platforms
  (needed because a single YouTube search is depth-capped; we slice by date and facet).
- **Crawl expansion:** from every Kobe-positive source, enumerate its channel, playlists and series.
- Metadata filter + priors (title/description/duration/uploader reputation/language) rank candidates.
- Log yield per query so the engine learns which query families produce Kobe speech.
- **Acceptance:** >= 2,000 unique candidates catalogued; query yield dashboard works.

### Phase 2 - Acquisition (M)
- Resumable audio-only downloader around `yt-dlp` (download archive, retries with backoff, polite sleeps,
  browser cookies for age-gated items, aria2c where useful), per-platform adapters, local `inbox/` importer.
- Records codec, bitrate, sample rate, duration, SHA-256, Chromaprint fingerprint at ingest.
- **Acceptance:** kill the process mid-run and restart: no re-downloads, no corrupt/partial files, catalog consistent.

### Phase 3 - Triage & Kobe verification (L) - the core
1. Decode to 16 kHz mono scratch; Silero VAD.
2. Diarization (sherpa-onnx; fallback Silero + ECAPA sliding-window clustering) -> per-source speaker clusters.
3. Speaker embeddings from an **ensemble** (e.g. ECAPA-TDNN + WeSpeaker/TitaNet) with AS-norm cohort scoring.
4. **Enrollment:** you confirm ~20 clips by ear in the UI -> era prototypes (seed set).
5. Score each cluster against prototypes -> calibrated probability -> `auto_accept / needs_review / auto_reject`.
6. **Keep-or-purge** the source file by Kobe-speech minutes (D3).
7. Active learning: every human label retrains calibration; hard negatives (interviewers, other players,
   impersonators) accumulate in a cohort.
- **Acceptance (targets):** on a 500-segment human-audited sample, accepted-segment precision >= 99 %;
  estimated recall >= 95 % at the chosen threshold; throughput measured and reported (hours audio / hour).

### Phase 4 - De-duplication engine + proof (M)
- Layers: exact hash -> source-ID registry -> Chromaprint fingerprint -> landmark/neural fingerprint on speech
  segments -> **transcript MinHash/SimHash** (robust to music beds & different mixes) -> embedding near-dup (FAISS).
- Keep-best policy by quality score; losers move to `_quarantine/duplicates/` with a reason record.
- **Benchmark harness** synthesizes known duplicates (re-encode, trim, +/-3 % speed, noise/music overlay, loudness change)
  and measures per-layer precision/recall.
- **`verify_no_duplicates` command**: recomputes every layer over the whole archive and fails (non-zero exit)
  if any non-quarantined pair exceeds thresholds.
- **Acceptance:** benchmark recall >= 99 % with 0 false merges on the synthetic set; verifier passes on the pilot archive.

### Phase 5 - Quality & authenticity scoring (M)
- Per segment: DNSMOS / NISQA / UTMOS, WADA-SNR, effective bandwidth (detect upsampled MP3 low-pass), clipping,
  loudness (LUFS), reverb estimate, **music / crowd / applause probability** (PANNs), language ID, ASR transcript
  (faster-whisper large-v3 + word timestamps), **synthetic-speech probability** (AASIST-family detector).
- Optional vocal separation / de-reverb / denoise **evaluated** per source type; both versions retained.
- **Acceptance:** every segment has a complete score card; histograms in the UI; spot-check 100 segments by ear.

### Phase 6 - Gradio web app (M)
Tabs: Dashboard | Discover | Review | Duplicates | Quality explorer | Search | Export | System.
Runs on `http://127.0.0.1:7860` (LAN opt-in, never public by default).
- **Acceptance:** you can review 50 gray-zone clips with keyboard shortcuts, resolve a duplicate cluster, and
  export a dataset without touching the CLI.

### Phase 7 - Curation & RVC export (S-M)
- Export profiles (e.g. `rvc_48k_clean`, `rvc_40k_clean`, `research_full`): mono, WAV 16-bit, slice lengths,
  loudness/peak normalization, min quality gates, era/language balancing, train/val split by *source* (no leakage).
- Dataset card (`DATASET_CARD.md`) with hours, eras, languages, quality stats, and known issues.
- **Acceptance:** an exported set loads in your RVC training tool; stats match the card.

### Phase 8 - Expansion loop & coverage report (ongoing)
- Re-run discovery with new query families; harvest from newly verified sources; capture-recapture coverage estimate;
  scheduled incremental runs.

## 7. "No duplicates" - how it is guaranteed

1. **Prevention at ingest:** URL/platform-ID registry + SHA-256 + Chromaprint reject identical re-downloads immediately.
2. **Segment-level detection** catches clips, edits, re-mixes, different rips of the same event.
3. **Keep-best, never delete:** the highest-quality copy is canonical; others are quarantined with provenance.
4. **Measured, not assumed:** the synthetic benchmark quantifies each layer; thresholds are tuned there.
5. **Continuous proof:** `verify_no_duplicates` runs after every pipeline batch and in CI on a fixture archive.

Duplicate definitions used (documented so the policy is explicit):
- *Exact:* same bytes.
- *Re-encode:* same audio, different codec/bitrate/container.
- *Clip/overlap:* one asset contains a >= N-second span of another.
- *Same utterance, different recording* (e.g. two broadcasters' feeds of one press conference): treated as
  **content duplicates**; keep the best, because training on 20 copies of one sentence biases the model.

## 8. RVC-readiness bar (what "clean" means)

- Single speaker (Kobe only), no overlap speech, no music bed, minimal crowd/room noise, low reverb.
- Prefer >= 16 kHz effective bandwidth; flag telephone/low-pass sources instead of silently using them.
- Era, language and speaking-style balance reported; extremes (shouting, whisper) tagged for optional exclusion.
- Honest note: RVC quality saturates well before "all the audio". The archive stays exhaustive; the
  *export* is the curated best-N-hours. Also: Kobe data is **speech**, so a model trained on it is a
  **speaking-voice** model. It will not sing well outside its pitch range. For the singing app, plan on
  adding singing datasets (including your own voice) later.

## 9. Risks & mitigations

| Risk | Mitigation |
|---|---|
| E: fills up | Budget guard + spill to D: + purge-if-no-Kobe (D3) |
| YouTube rate limits / bot checks / format churn | Polite throttling, browser cookies, JS runtime, update yt-dlp, retries, resumable queue |
| Wrong-speaker contamination | Ensemble + calibration + human gray-zone review + audit sample metrics |
| AI-generated / impersonated "Kobe" audio | Synthetic detector + provenance (uploader reputation, date) + review |
| 8 GB VRAM / 16 GB RAM limits | One GPU job at a time, int8/fp16, chunked streaming, resource guard |
| Source rate limits / bot checks / platform blocks | Polite throttling, browser cookies, proxy/retry support, resumable worker queues |
| Library breakage on Windows | Smoke-test matrix in Phase 0, pinned lockfile, fallbacks documented per model |

## 10. Decisions

**Resolved (2026-10-21):**

| # | Question | Your answer |
|---|---|---|
| 1 | Publish repo to `E:\Sound Experiments` | Copy via terminal (my file tools cannot write outside the workspace) |
| 2 | Storage layout | Raw on `E:` (60 GB cap, keep 12 GB free), automatic spill to `D:` |
| 3 | Pilot or full run | **Pilot first** (~200 candidates, Phases 0-4), then scale |
| 4 | Diarizer | **Skip pyannote** -> D13 (no tokens, no gated models) |

**Still open (needed before the pilot starts):**

1. **Seed verification:** can you confirm ~20 clips of Kobe by ear in the UI (needed to enroll the voice)?
2. **Browser cookies:** may the downloader read cookies from your logged-in browser for age-gated/limited videos?

## 11. Definition of done (Project 01)

- Raw archive at the target path, every file cataloged, hashed, and traceable to its source URL.
- `verify_no_duplicates` passes; dedup benchmark report committed.
- Kobe-ID audit report (precision/recall estimate) committed.
- Gradio app runs end-to-end on this laptop.
- At least one RVC export profile produced with a dataset card.
- Coverage report states discovered hours, estimated total discoverable hours, and verified yield.

