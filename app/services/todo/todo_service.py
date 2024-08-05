import os
import time
from bson.json_util import dumps
from bson.objectid import ObjectId
from dotenv import load_dotenv
from app.tools.security_toolbox import security_toolbox
from app.database_handler.mongodb_handler import mongodb_handler

load_dotenv('app/.env')

DB_URI = os.getenv('DB_URI')
DB_NAME = os.getenv('TODO_DB_NAME')
COLLECTION_NAME = os.getenv('TODO_COLLECTION_NAME')

SECRECT_JWT = os.getenv('SECRECT_JWT')
JWT_TOKEN_LIFETIME_MIN = 10

class todo_service:

    def __init__(self):
        self.my_db = mongodb_handler(DB_URI, DB_NAME, COLLECTION_NAME)
        self.my_security_toolbox = security_toolbox(SECRECT_JWT)
        

    def create_task(self, user, task_text):
        timestamp = str(time.time())
        item = {
            'user': user,
            'task_text': task_text,
            'doing': 'false',
            'done': 'false',
            'createdAt': timestamp,
            'updatedAt': timestamp
        }
        self.my_db.create(item, default=str, indent=4)
        return dumps(item)
    
    
    def read_task(self, user, id_task):
        task = self.my_db.find_one({'user': user, "_id": ObjectId(id_task)})
        return dumps(task)
    
    
    def update_task(self, user, id_task, task_text):
        return 1
    
    
    def delete_task(self, user, id_task):
        self.my_db.delete({'user': user, "_id": ObjectId(id_task)})
        return "OK"
    
    
    def list_task(self, user):
        tasks = self.my_db.list({'user': user})
        tasks_list = list(tasks)
        tasks_list_json = dumps(tasks_list, default=str, indent=4)
        return tasks_list_json
        
        