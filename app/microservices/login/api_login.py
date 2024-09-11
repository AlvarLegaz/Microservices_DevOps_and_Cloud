import http.client
from flask import Flask
from flask import request
from flask_cors import CORS
from app.microservices.login.login_service import LoginService 

api_application = Flask(__name__)
CORS(api_application)

HEADERS = {"Content-Type": "application/json"}

my_login_srv = LoginService()

@api_application.route("/")
def hello():
    return ("Hello from login api. version 1.1.0", http.client.OK, HEADERS)


@api_application.route("/login", methods=['POST'])
def login_by_user():
    try:
        entry = request.get_json()
        response = my_login_srv.login(entry['user'], entry['password'])
        if response is None:
            return ({"error": "Incorrect username or password"}, http.client.UNAUTHORIZED, HEADERS)
        else:
            return ({'access_token':response}, http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/register", methods=['POST'])
def register_user():
    try:
        entry = request.get_json()
        response = my_login_srv.register_user(entry['user'], entry['password'])
        return (response, http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)  
