echo off

echo Deploy Login service

echo Deploy API LOGIN at PORT 3000
export PYTHONPATH=.
export FLASK_APP=./app/microservices/login/api_login.py
flask --debug run -h 0.0.0.0 -p 3000


