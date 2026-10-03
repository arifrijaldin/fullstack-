@echo off
title AUTONOMOUS OTA RESERVATION INGESTION DAEMON (LIVE MONITOR)
cd /d "%~dp0"
echo Membuka Autonomous OTA Ingestion Live Monitor...
start "" chrome.exe --app="file:///%~dp0frontend/live_bot_reservasi.html" --start-maximized
exit
