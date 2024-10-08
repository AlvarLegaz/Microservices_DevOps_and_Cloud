import http.client
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
from functools import wraps
from app.microservices.login.login_service import LoginService  # type: ignore
import logging

api_application = Flask(__name__)
CORS(api_application, resources={r"/*": {"origins": "*"}})

HEADERS = {"Content-Type": "application/json"}

api_key = "aswes8sdgañlekrwaorpañlcasre"

try:
    my_login_srv = LoginService()
except Exception as e:
    logging.error("Fail to create Login service in flask: " + str(e))
    sys.exit(1)  # Usar sys.exit() para abortar el programa


def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key_received = request.headers.get('X-ApiKey')
        if api_key == api_key_received:
            return f(*args, **kwargs)
        else:
            return jsonify({"message": "API key is missing or invalid"}), 401
    return decorated_function


@api_application.route("/")
@require_api_key
def hello():
    return ("Hello from login api. version 2.0.0", http.client.OK, HEADERS)


@api_application.route("/login", methods=['POST'])
@require_api_key
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
        if response is None:
            return ({"error": "Username already exits"}, http.client.UNAUTHORIZED, HEADERS)
        else:
            return (response, http.client.OK, HEADERS)
    except Exception as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)  
                
    
if __name__ == "__main__":
    api_application.run(debug=True)

