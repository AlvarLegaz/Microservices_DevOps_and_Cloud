#!/bin/bash
echo "Deploy front web service"

PUERTO=8081
DIRECTORIO="app/front/src/components/"

python3 -m http.server $PUERTO --directory $DIRECTORIO
