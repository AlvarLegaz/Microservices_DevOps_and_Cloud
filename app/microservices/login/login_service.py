import os
from bson.json_util import dumps
from dotenv import load_dotenv
from app.tools.security_toolbox import SecurityToolbox # type: ignore
from app.database_handler.mongodb_handler import mongodb_handler # type: ignore

load_dotenv('app/.env')

DB_URI = os.getenv('DB_URI')
DB_NAME = os.getenv('DB_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')

SECRET_JWT = str(os.getenv('SECRET_JWT'))
JWT_TOKEN_LIFETIME_MIN = 10

class LoginService:

    def __init__(self):
        try:
            print("Init LoginService ...")
            self.my_db = mongodb_handler(DB_URI, DB_NAME, COLLECTION_NAME)
            self.my_security_toolbox = SecurityToolbox(SECRET_JWT)
        except Exception as e:
            print(f"Error initializing LoginService: {e}")
            raise Exception("Fail Login" + str(e))

    def login(self, username, password):
        password_sha_signature = self.my_security_toolbox.get_sha256_signature(password)
        try:
            response = self.my_db.find_one({'user': username, 'pass': password_sha_signature})
            if response:
                user_str = response.get('user')
                return self.my_security_toolbox.get_jwt_token(user_str, JWT_TOKEN_LIFETIME_MIN)
            else:
                return None
        except Exception as e:
            print(f"Error during login: {e}")
            raise e
    
    def register_user(self, username, password):
        try:
            password_sha_signature = self.my_security_toolbox.get_sha256_signature(password)
            register_json = {'user': username, 'pass': password_sha_signature}
            if self.user_already_exists(username):
                return None
            else:
                self.my_db.create(register_json)
                return dumps(register_json)
        except Exception as e:
            raise e
        
    def user_already_exists(self, username):
        try:
            response = self.my_db.find_one({'user': username})
            if response == None:
                return False   
            else:
                return True
        except Exception as e:
            raise e


if __name__ == '__main__':
    # Uso de la clase
    loggin = LoginService()

    token = loggin.login("pedro","1234")
    print("token obtained: "+token)


    
        
