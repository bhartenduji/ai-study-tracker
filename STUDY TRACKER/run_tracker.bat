@echo off
echo Starting AI/ML Study Tracker on a local server...
start http://localhost:8000
python -m http.server 8000
exit
