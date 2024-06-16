import http.client

from flask import Flask

import os
from dotenv import load_dotenv

from app import util
from app.UsersJsonFileManager import UsersJsonFileManager

load_dotenv()

file_name = os.getenv('USERS_FILE')

db_Json_File = UsersJsonFileManager(file_name)
api_application = Flask(__name__)
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}

@api_application.route("/")
def hello():
    return ("Hello from users api", http.client.OK, HEADERS)