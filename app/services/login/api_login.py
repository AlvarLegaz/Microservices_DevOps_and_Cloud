import http.client
from flask import Flask
from flask import request
from app.services.login.login_service import login_service 

api_application = Flask(__name__)
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}

my_login_srv = login_service()

@api_application.route("/")
def hello():
    return ("Hello from login api. version 1.0.0", http.client.OK, HEADERS)

@api_application.route("/login", methods=['PUT'])
def login_by_user():
    try:
        entry = request.get_json()
        response = my_login_srv.login(entry['user'], entry['password'])
        return ({'access_token':response}, http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)
