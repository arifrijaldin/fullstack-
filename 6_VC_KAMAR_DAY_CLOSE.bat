@echo off
title PULIHKAN STATUS KAMAR VC POST DAY CLOSE (DEMO)
cd /d "%~dp0"
echo Membuka Dashboard Pemulihan Status Kamar VC...
start "" chrome.exe --app="file:///%~dp0frontend/vc_kamar_dayclose.html" --start-maximized
exit
