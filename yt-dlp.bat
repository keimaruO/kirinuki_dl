@echo off
set /p URL="Enter the URL: "
python yt-dlp.py %URL%
pause
