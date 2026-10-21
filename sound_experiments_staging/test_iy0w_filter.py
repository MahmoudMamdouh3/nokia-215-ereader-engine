import os
import sys
from pathlib import Path

# Add torch/lib for CUDA cuDNN DLLs
torch_lib = Path(sys.prefix) / "Lib" / "site-packages" / "torch" / "lib"
if torch_lib.exists():
    try:
        os.add_dll_directory(str(torch_lib))
    except Exception:
        pass
    os.environ["PATH"] = str(torch_lib) + os.pathsep + os.environ.get("PATH", "")

import torch
torch.backends.cudnn.enabled = False

from faster_whisper import WhisperModel
from soundlab.speaker_filter import KobeVoiceprintFilter
from resemblyzer import preprocess_wav

audio_path = Path(r"E:\Sound Experiments\Kobe bryant Database raw\sources\youtube\IY0wRtk6FM4\audio.opus")
print("Audio exists:", audio_path.exists())

# Load Whisper on GPU
try:
    print("Loading Whisper base.en...")
    model = WhisperModel("base.en", device="cuda", compute_type="float16")
    segments, info = model.transcribe(str(audio_path), vad_filter=True)
except Exception as e:
    print(f"Whisper CUDA fallback to CPU: {e}")
    model = WhisperModel("base.en", device="cpu", compute_type="int8")
    segments, info = model.transcribe(str(audio_path), vad_filter=True)

# Collect first 20 segments
seg_list = []
for i, s in enumerate(segments):
    if i >= 20:
        break
    seg_list.append({"start": s.start, "end": s.end, "text": s.text})

print(f"Transcribed {len(seg_list)} segments. Testing Kobe biometric filter...")
filt = KobeVoiceprintFilter(device="cuda")
results = []
wav = preprocess_wav(str(audio_path))

for s in seg_list:
    st_idx = int(s["start"] * 16000)
    en_idx = int(s["end"] * 16000)
    slice_wav = wav[st_idx:en_idx]
    if len(slice_wav) < 8000:
        continue
    sim = filt.compute_similarity(slice_wav)
    results.append((s["start"], s["end"], sim, s["text"]))

print("\n=== RESULTS: Speaker Biometric Verification on IY0wRtk6FM4 ===")
for st, en, sim, txt in results:
    status = "KOBE (PASS)" if sim >= 0.82 else "INTERVIEWER/OTHER (REJECT)"
    print(f"[{st:6.1f}s - {en:6.1f}s] Sim={sim:.4f} -> {status:28s} | {txt.strip()}")
