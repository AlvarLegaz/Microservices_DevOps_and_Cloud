@echo off
echo Deploy front web service

set PORT=8081
set DIRECTORY=./app/front/src/components

python app\front\src\front_web_server.py %PORT% %DIRECTORY%

pause

