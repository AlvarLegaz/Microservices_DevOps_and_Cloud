import os
import json
from dotenv import load_dotenv
from UsersJsonFileManager import UsersJsonFileManager

print("UserJsonManager test script")

load_dotenv()

file_name = os.getenv('USERS_FILE')

manager = UsersJsonFileManager(file_name)

print("\nTest 1: Create entries:")
manager.create_entry({'user': 'pedro', 'pass': '1234'})
manager.create_entry({'user': 'paco', 'pass': 'abcd'})
manager.create_entry({'pass': 'qwerty', 'user': 'manuel'})
manager.create_entry({'user': 'juan', 'pass': 'qwerty', 'email':'juan@juan.com'})
manager.list_entries()

print("\nTest 2: search by name:")
print ("User paco has index =" , manager.search_user('paco'))
print ("User pedro has index =" , manager.search_user('pedro'))
print ("User manuel has index =" , manager.search_user('manuel'))

print("\nTest 3: read entries:")
# Convertir la cadena JSON en un diccionario
entrada_json = (manager.read_entry(0))
print(entrada_json)
print(entrada_json['user'])

print("\nTest 4: update entries:")
manager.update_entry(0,{'user': 'pedro', 'pass': '1'})
manager.update_entry(1,{'user': 'pedro2', 'pass': '12'})
manager.update_entry(4,{'user': 'pedro3', 'pass': '123'})
manager.list_entries()

print("\nTest 5: delete entries:")
manager.delete_entry(0)
manager.delete_entry(manager.search_user('manuel'))
manager.list_entries()

