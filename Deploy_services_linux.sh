echo Deploy Services

echo Deploy API LOGIN at PORT 3000
export FLASK_APP=app/services/login/api_login.py
python3 -m flask --debug run -h 0.0.0.0 -p 3000 &
pause()
