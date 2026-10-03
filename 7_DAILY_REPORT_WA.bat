@echo off
title GENERATOR DAILY REPORT OPERATIONAL WA (DEMO)
cd /d "%~dp0"
echo Membuka Generator Laporan WhatsApp Operasional...
start "" chrome.exe --app="file:///%~dp0frontend/daily_report_wa.html" --start-maximized
exit
