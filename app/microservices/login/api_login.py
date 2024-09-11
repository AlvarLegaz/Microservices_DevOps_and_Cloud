import os
from dotenv import load_dotenv
from app.tools.security_toolbox import security_toolbox
from app.database_handler.mongodb_handler import mongodb_handler


load_dotenv('app/.env')

DB_URI = os.getenv('DB_URI')
DB_NAME = os.getenv('DB_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')

SECRECT_JWT = os.getenv('SECRECT_JWT')
JWT_TOKEN_LIFETIME_MIN = 10

db_url = "mongodb://localhost:27017"
db_name = 'my_users_db'
collection_name = 'users'


class LoginService:

    def __init__(self):
        self.my_db = mongodb_handler(DB_URI, DB_NAME, COLLECTION_NAME)
        self.my_security_toolbox = security_toolbox(SECRECT_JWT)
        

    def login(self, username, password):
        password_sha_signature = self.my_security_toolbox.get_sha256_signature(password)
       	response = self.my_db.find_one({'user': username, 'pass': password_sha_signature})
        if response:
            return self.my_security_toolbox.get_jwt_token(str(username), JWT_TOKEN_LIFETIME_MIN)
        else:
            return None
    
    def register_user(self, username, password):
        password_sha_signature = self.my_security_toolbox.get_sha256_signature(password)
        response = self.my_db.create({'user': username, 'pass': password_sha_signature})
        if response:
            return response
        else:
            return None
    
        
