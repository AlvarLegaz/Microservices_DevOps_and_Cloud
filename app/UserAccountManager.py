import hashlib
import os
import json
from dotenv import load_dotenv
from app.UsersJsonFileManager import UsersJsonFileManager

load_dotenv()
file_name = os.getenv('USERS_FILE')



class UserAccountManager:

    def __init__(self):
        self.db_Json_File = UsersJsonFileManager(file_name)

    def signin(self, username, password):
        index = self.db_Json_File.search_user(username)
        if index != 0:
            user_credentials = self.db_Json_File.read_entry(index)
            hash_object = hashlib.sha256()
            hash_object.update(password.encode('utf-8'))
            password_sha_signature = hash_object.hexdigest()
            if user_credentials['pass'] == password_sha_signature:
                return  user_credentials
        raise ValueError("Error: Wrong user or password")


    def signout(self, user):
        # Implementa el cierre de sesión aquí
        pass

    def signup(self, user, password):
        user_credentials = json.loads('{"user": "' + user + '", "pass": "' + password + '"}')
        print(user_credentials)
        self.db_Json_File.create_entry(user_credentials)
        pass

    def update_user(self, user, new_data):
        # Implementa la actualización del usuario aquí
        pass