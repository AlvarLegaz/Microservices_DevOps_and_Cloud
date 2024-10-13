#!/bin/bash
echo "Deploy front web service"

PORT=8081
DIRECTORY=./app/front/src/components

python3 app\front\src\front_web_server.py %PORT% %DIRECTORY%
