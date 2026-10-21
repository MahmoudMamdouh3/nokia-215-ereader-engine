@echo off
title Sound Experiments - Web Control Center
echo Starting Sound Experiments Gradio Web UI on http://127.0.0.1:7860 ...
"D:\SoundExperiments\venv\Scripts\python.exe" -m soundlab.cli ui --host 127.0.0.1 --port 7860
pause
