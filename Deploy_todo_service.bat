echo off

echo Deploy Services

echo Deploy API TODO at PORT 3001
set PYTHONPATH=.
set FLASK_APP=app\microservices\todo\api_todo.py
python -m flask --debug run -h 0.0.0.0 -p 3001
pause()

