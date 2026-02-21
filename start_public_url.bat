@echo off
echo ========================================
echo   UAC Analytics - Local Public URL Setup
echo ========================================
echo.

where ngrok >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] ngrok is not installed.
    echo Install ngrok from https://ngrok.com/download and run this script again.
    pause
    exit /b 1
)

if "%NGROK_AUTHTOKEN%"=="" (
    echo [WARNING] NGROK_AUTHTOKEN is not set.
    echo Set it first with:
    echo   set NGROK_AUTHTOKEN=your_token_here
    echo.
) else (
    echo [1/2] Configuring ngrok authentication from NGROK_AUTHTOKEN...
    ngrok config add-authtoken %NGROK_AUTHTOKEN%
)

echo [2/2] Starting ngrok tunnel on port 8501...
echo Open http://localhost:4040 to copy your public forwarding URL.
echo Keep this window open to keep the tunnel active.
echo.
ngrok http 8501
