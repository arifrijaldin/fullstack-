@echo off
title PETA ARSITEKTUR & ALUR KERJA SISTEM (SLIDER PRESENTASI)
cd /d "%~dp0"
echo Membuka Presentasi Interaktif Alur Sistem Otomasi Hotel...
start "" chrome.exe --app="file:///%~dp0frontend/arsitektur_flow_sistem.html" --start-maximized
exit
