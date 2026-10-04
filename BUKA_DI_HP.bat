@echo off
title BUKA PORTOFOLIO DI HP (JARINGAN LOKAL)
cd /d "%~dp0"

echo =======================================================================
echo    PORTOFOLIO AKHMAD ARIF RIJALDIN, S.Kom.
echo =======================================================================
echo.
echo Server lokal sedang aktif di Port 8080...
echo.
echo CARA BUKA DI HP ANDA:
echo 1. Pastikan HP dan Laptop ini terhubung ke WiFi yang sama.
echo 2. Buka browser di HP Anda (Chrome, Safari, dll).
echo 3. Ketik alamat berikut:
echo.
echo       http://192.168.1.92:8080
echo.
echo =======================================================================
echo Tekan Ctrl+C jika ingin mematikan server.
echo =======================================================================
echo.

python -m http.server 8080
pause
