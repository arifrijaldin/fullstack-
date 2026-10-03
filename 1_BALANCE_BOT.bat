@echo off
title BALANCE BOT - RECONCILIATION ENGINE (DEMO)
cd /d "%~dp0"
echo Membuka Balance Bot Dashboard...
start "" chrome.exe --app="file:///%~dp0frontend/audit_dashboard.html" --start-maximized
exit
