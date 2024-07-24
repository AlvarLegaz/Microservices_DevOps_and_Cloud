echo off

echo Deploy Services

echo Deploy API LOGIN at PORT 3000
set FLASK_APP=app\api_login.py
start python -m flask --debug run -h localhost -p 3000
pause()

