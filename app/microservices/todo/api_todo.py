import http.client
from flask import Flask, request, render_template
from flask_cors import CORS
from app.microservices.todo.todo_service import TodoService 

api_application = Flask(__name__)
CORS(api_application, resources={r"/*": {"origins": "*"}})

HEADERS = {"Content-Type": "application/json"}

my_todo_srv = TodoService()

@api_application.route("/")
def hello():
     return render_template('hello.html')


@api_application.route("/todo/<user>", methods=['GET'])
def get_tasks_list(user):
    try:
        response = my_todo_srv.list_task(user)
        return (response, http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/todo/<user>", methods=['POST'])
def set_task(user):
    try:
        task = request.get_json()
        response = my_todo_srv.create_task(user, task)
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

@api_application.route("/todo/<user>/<task_id>", methods=['PUT'])
def update_task(user, task_id):
    try:
        task_text = request.get_json()
        response = my_todo_srv.update_task(user, task_id, task_text)
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
