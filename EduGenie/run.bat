@echo off
echo ========================================================
echo Starting EduGenie: Google Gemini Powered Learning Assistant
echo ========================================================
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
) else if exist "..\Edu-Genie\.venv\Scripts\python.exe" (
    "..\Edu-Genie\.venv\Scripts\python.exe" -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
) else (
    uvicorn main:app --reload --host 127.0.0.1 --port 8000
)
pause
