echo off

echo Deploy Services

echo Deploy API LOGIN at PORT 3000
set PYTHONPATH=.
set FLASK_APP=app\microservices\login\api_login.py
python -m flask --debug run -h 0.0.0.0 -p 3000
pause()

