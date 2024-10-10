echo off

echo Deploy Todo service

echo Deploy API TODO at PORT 3001
export PYTHONPATH=.
export FLASK_APP=./app/microservices/todo/api_todo.py
flask --debug run -h 0.0.0.0 -p 3001


