import os
import json
from dotenv import load_dotenv
from app.tools.security_toolbox import security_toolbox
from app.UsersJsonFileManager import UsersJsonFileManager
from app.database_connector.mongodb_handler import mongodb_handler

load_dotenv()
file_name = os.getenv('USERS_FILE')
db_url = os.getenv('DB_URL')
users_db = os.getenv('DB_NAME')
users_collection = os.getenv('COLLECTION_NAME')
secrect = os.getenv('SECRECT_JWT')


class UserAccountManager:

    def __init__(self, source):
        self.source = source
        self.security_tools = security_toolbox(secrect)
        if(self.source == 'json_file'):
            self.db_Json_File = UsersJsonFileManager(file_name)
        elif(self.source == 'mongoDB'):  
            self.users_db_handler = mongodb_handler(db_url, users_db, users_collection)  
        else:
            raise ValueError("Unknown source!")
            

    def signin(self, username, password):
        if(self.source == 'json_file'):
            index = self.db_Json_File.search_user(username)
            if index != 0:
                user_credentials = self.db_Json_File.read_entry(index)
                password_sha_signature = self.security_tools.get_sha256_signature(password)

                if user_credentials['pass'] == password_sha_signature:
                    return  user_credentials
            raise ValueError("Wrong user or password")
        
        elif(self.source == 'mongoDB'):
            query = {"user": username}
            user_credentials = self.users_db_handler.read(query)
            
            password_sha_signature = self.security_tools.get_sha256_signature(password)
            try:
                if user_credentials[0]['pass'] == password_sha_signature:
                    print(user_credentials[0])
                    return  user_credentials[0]
                else:
                    raise ValueError("Wrong user or password") 
            except Exception as e:
                    raise ValueError("Wrong user or password") 
            


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

# Test Class
if __name__ == '__main__':
    my_UserAccountManager = UserAccountManager('mongoDB')
    my_UserAccountManager.signin('pedro2','1234')
    my_UserAccountManager.signin('pedro2','124')
    my_UserAccountManager.signin('pedro552','1234')
