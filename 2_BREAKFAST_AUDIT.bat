@echo off
title BREAKFAST AUDIT (DEMO)
cd /d "%~dp0"
echo Menjalankan kalkulasi audit sarapan...
python services\audit_breakfast.py
start "" chrome.exe --app="file:///%~dp0frontend/breakfast_audit.html" --start-maximized
exit
