@echo off
title Sound Experiments - Live Dataset Monitor (Live Refresh)
cls
"D:\SoundExperiments\venv\Scripts\python.exe" -m soundlab.cli progress --target 500 --watch
pause
