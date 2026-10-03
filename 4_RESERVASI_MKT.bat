@echo off
title RESERVASI MARKETING AI (DEMO)
cd /d "%~dp0"
echo Memulai server portal reservasi marketing...
start "" python services\app_marketing_web.py
timeout /t 2 >nul
start "" "http://127.0.0.1:5000"
exit
