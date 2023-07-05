@echo off
set /p URL="Enter the URL: "
python Live-wait.py %URL%
pause