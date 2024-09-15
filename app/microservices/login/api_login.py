import http.client
import sys
from flask import Flask
from flask import request
from flask_cors import CORS
from app.microservices.login.login_service import LoginService  # type: ignore
import logging

api_application = Flask(__name__)
CORS(api_application, resources={r"/*": {"origins": "*"}})

HEADERS = {"Content-Type": "application/json"}

try:
    my_login_srv = LoginService()
except Exception as e:
    logging.error("Fail to create Login service in flask: " + str(e))
    sys.exit(1)  # Usar sys.exit() para abortar el programa

@api_application.route("/")
def hello():
    return ("Hello from login api. version 1.1.1", http.client.OK, HEADERS)


@api_application.route("/login", methods=['POST'])
def login_by_user():
    try:
        entry = request.get_json()
        response = my_login_srv.login(entry['user'], entry['password'])
        if response is None:
            return ({"error": "Incorrect username or password"}, http.client.UNAUTHORIZED, HEADERS)
        else:
            return ({'access_token':response}, http.client.OK, HEADERS)
    except Exception as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)


@api_application.route("/register", methods=['POST'])
def register_user():
    try:
        entry = request.get_json()
        response = my_login_srv.register_user(entry['user'], entry['password'])
        return (response, http.client.OK, HEADERS)
    except Exception as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)  
    
if __name__ == "__main__":
    api_application.run(debug=True)

