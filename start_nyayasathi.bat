@echo off
title NyayaSathi Kiosk Runner
echo ========================================================
echo   Starting NyayaSathi Kiosk System (Backend + Frontend)
echo ========================================================
echo.

set "PATH=C:\Program Files\nodejs;%PATH%"

echo [1/2] Starting Backend Server (FastAPI on Port 8000)...
start "NyayaSathi Backend" cmd /k "cd /d %~dp0 && python backend\run.py"

echo [2/2] Starting Frontend Server (Vite on Port 5173)...
start "NyayaSathi Frontend" cmd /k "cd /d %~dp0frontend && npm.cmd run dev"

echo.
echo ========================================================
echo   NyayaSathi is starting up!
echo   Frontend: http://localhost:5173
echo   Backend:  http://127.0.0.1:8000
echo ========================================================
timeout /t 3 >nul
start http://localhost:5173
