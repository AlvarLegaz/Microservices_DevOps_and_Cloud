import os
import json
import datetime
from bson.json_util import dumps
from bson.objectid import ObjectId
from jsonschema import validate, ValidationError
from dotenv import load_dotenv
from app.tools.security_toolbox import SecurityToolbox # type: ignore
from app.database_handler.mongodb_handler import mongodb_handler

load_dotenv('app/.env')

SECRET_JWT = str(os.getenv('SECRET_JWT'))
JWT_TOKEN_LIFETIME_MIN = 10

class TodoService:

    def __init__(self, DB_URI, DB_NAME, COLLECTION_NAME):
        try:
            self.my_db = mongodb_handler(DB_URI, DB_NAME, COLLECTION_NAME)
            self.task_esquema = {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "doing": {"type": "boolean"},  
                    "done": {"type": "boolean"}, 
                    "createdAt": {"type": "string"},
                    "updatedAt": {"type": "string"}
                },
                "required": ["title", "description", "doing", "done"]
            }
            self.my_security_toolbox = SecurityToolbox(SECRET_JWT)
        except Exception as e:
            print(f"Error initializing Todo Service: {e}")
            raise Exception("Fail Todo Service" + str(e))

    def create_task(self, user, task_json):
        self.validate_task_json(task_json)
        # Add user to the db item. item is task and user
        task_json["user"] = user
        utc_now = datetime.datetime.utcnow()
        task_json["createdAt"] = utc_now.strftime("%Y-%m-%d %H:%M:%S")
        task_json["updatedAt"] = utc_now.strftime("%Y-%m-%d %H:%M:%S")
        self.my_db.create(task_json)
        return dumps(task_json)
    
    
    def read_task(self, user, id_task):
        task = self.my_db.find_one({'user': user, "_id": ObjectId(id_task)})
        return dumps(task)
    
    
    def update_task(self, user, id_task, task_json):
        self.validate_task_json(task_json)
        utc_now = datetime.datetime.utcnow()
        task_json["updatedAt"] = utc_now.strftime("%Y-%m-%d %H:%M:%S")
        self.my_db.update({'user': user, "_id": ObjectId(id_task)}, task_json)
        return dumps(task_json)
    
    
    def delete_task(self, user, id_task):
        self.my_db.delete({'user': user, "_id": ObjectId(id_task)})
        return "OK"
    
    
    def list_task(self, user, token_jwt):
        try:
            decoded_token = self.my_security_toolbox.decode_jwt_token(token_jwt)
            if decoded_token['user_id'] != user:
                raise Exception("Token not correspond to user")
            tasks_list = list(self.my_db.list({'user': user}))
            tasks_list_json = dumps(tasks_list, default=str, indent=4)
            return tasks_list_json
        except Exception as e:
            raise Exception("Fail get list todo Service:" + str(e))
        
    def validate_task_json(self, json_data):
        try:
            # Si json_data es una cadena, conviértela a diccionario
            if isinstance(json_data, str):
                data = json.loads(json_data)
            else:
                data = json_data
            
            # Validar el diccionario contra el esquema
            validate(instance=data, schema=self.task_esquema)
            return True, "El JSON es válido."
        except (json.JSONDecodeError, ValidationError) as e:
            raise TypeError(f"Task json not valid: {e.message}")
        
        
        