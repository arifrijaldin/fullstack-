@echo off
title OTOMASI LAPORAN PENJUALAN NIGHT SHIFT (DEMO)
cd /d "%~dp0"
echo Membuka Dashboard Laporan Penjualan MDR...
start "" chrome.exe --app="file:///%~dp0frontend/laporan_penjualan.html" --start-maximized
exit
