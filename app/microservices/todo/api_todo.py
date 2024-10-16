import os
from dotenv import load_dotenv
import http.client
import sys
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from functools import wraps
from app.microservices.todo.todo_service import TodoService 
import logging

load_dotenv('app/.env')
API_KEY = os.getenv('API_KEY')
DB_URI = os.getenv('DB_URI')
DB_NAME = os.getenv('TODO_DB_NAME')
COLLECTION_NAME = os.getenv('TODO_COLLECTION_NAME')

api_application = Flask(__name__)
CORS(api_application, resources={r"/*": {"origins": "*"}})
HEADERS = {"Content-Type": "application/json"}


try:
    my_todo_srv = TodoService(DB_URI, DB_NAME, COLLECTION_NAME)
except Exception as e:
    logging.error("Fail to create Login service in flask: " + str(e))
    sys.exit(1)  # Usar sys.exit() para abortar el programa


def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key_received = request.headers.get('X-ApiKey')
        if API_KEY == api_key_received:
            return f(*args, **kwargs)
        else:
            return jsonify({"message": "API key is missing or invalid"}), 401
    return decorated_function


@api_application.route("/")
def hello():
     return render_template('hello.html')


@api_application.route("/todo/<user>", methods=['GET'])
@require_api_key
def get_tasks_list(user):
    try:
        token_jwt = request.headers.get('Authorization')
        if not token_jwt:
            raise ValueError("Authorization token missing")
        response = my_todo_srv.list_task(user, token_jwt)
        return (response, http.client.OK, HEADERS)
    except Exception as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/todo/<user>", methods=['POST'])
@require_api_key
def set_task(user):
    try:
        task = request.get_json()
        response = my_todo_srv.create_task(user, task)
        return (response, http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/todo/<user>/<task_id>", methods=['GET'])
@require_api_key
def read_task(user, task_id):
    try:
        response = my_todo_srv.read_task(user, task_id)
        return (response, http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)        


@api_application.route("/todo/<user>/<task_id>", methods=['PUT'])
@require_api_key
def update_task(user, task_id):
    try:
        task_text = request.get_json()
        response = my_todo_srv.update_task(user, task_id, task_text)
        return (response, http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)
          
        
@api_application.route("/todo/<user>/<task_id>", methods=['DELETE'])
@require_api_key
def delete_task(user, task_id):
    try:
        response = my_todo_srv.delete_task(user, task_id)
        return (response, http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)
