@echo off
echo ========================================
echo   UAC Analytics - Public URL Setup
echo ========================================
echo.

REM Check if ngrok is installed
where ngrok >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] ngrok is not installed!
    echo.
    echo Please install ngrok:
    echo 1. Download from: https://ngrok.com/download
    echo 2. Extract ngrok.exe to this folder or add to PATH
    echo 3. Run this script again
    echo.
    pause
    exit /b 1
)

echo [1/3] Setting up ngrok authentication...
ngrok config add-authtoken 39WWKz1t3uBHjAtQBmAJDaO8DFc_3evevEHLsKcnbFLcoCUS7

echo [2/3] Starting ngrok tunnel on port 8501...
echo.
echo ========================================
echo   PUBLIC URL READY!
echo ========================================
echo.
echo Your dashboard is now accessible at:
echo Check the URL below (https://xxxx.ngrok-free.app)
echo.
echo Or visit: http://localhost:4040
echo.
echo Keep this window open to maintain access!
echo Press Ctrl+C to stop the tunnel
echo ========================================
echo.

ngrok http 8501
