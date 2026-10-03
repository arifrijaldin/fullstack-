@echo off
title DEPARTURE CHAT & FO OPERATIONS (DEMO)
cd /d "%~dp0"
echo Membuka Departure Chat Monitoring Board...
start "" chrome.exe --app="file:///%~dp0frontend/departure_chat.html" --start-maximized
exit
