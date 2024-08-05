import http.client
from flask import Flask
from flask import request
from app.services.todo.todo_service import todo_service 

api_application = Flask(__name__)
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}

my_todo_srv = todo_service()

@api_application.route("/")
def hello():
    return ("Hello from TO-DO api. version 1.0.0", http.client.OK, HEADERS)


@api_application.route("/todo/<user>", methods=['GET'])
def get_tasks_list(user):
    try:
        entry = request.get_json()
        response = my_todo_srv.list_task(user)
        return (response, http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/todo/<user>", methods=['POST'])
def set_task(user):
    try:
        task_text = request.get_json()
        response = my_todo_srv.create_task(user, task_text)
        return (response, http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/todo/<user>/<task_id>", methods=['GET'])
def read_task(user, task_id):
    try:
        response = my_todo_srv.read_task(user, task_id)
        return (response, http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)        
        
        
@api_application.route("/todo/<user>/<task_id>", methods=['DELETE'])
def delete_task(user, task_id):
    try:
        response = my_todo_srv.delete_task(user, task_id)
        return (response, http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)
