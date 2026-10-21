@echo off
set PYTHONUNBUFFERED=1
set CUDA_VISIBLE_DEVICES=0
set PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
title Sound Experiments - GPU AI Worker
echo Starting continuous GPU deep learning pipeline (Whisper ASR + UVR5)...
"D:\SoundExperiments\venv\Scripts\python.exe" -u -m soundlab.cli run-worker
pause
