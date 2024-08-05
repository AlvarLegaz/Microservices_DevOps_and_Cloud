echo off

echo Deploy Services

echo Deploy API TODO at PORT 3001
set PYTHONPATH=.
set FLASK_APP=app\services\todo\api_todo.py
start python -m flask --debug run -p 3001

