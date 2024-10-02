@echo off
echo Deploy front web service

set PUERTO=8081
set DIRECTORIO=app\front\src\components\

python -m http.server %PUERTO% --directory %DIRECTORIO%
pause
