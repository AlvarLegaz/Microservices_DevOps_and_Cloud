import app
import json
import hashlib

class UsersJsonFileManager:
    def __init__(self, filename):
        self.filename = filename
        print("Filename" + filename)
        self.hash_object = hashlib.sha256()
        # Intenta cargar las entradas existentes desde el archivo
        try:
            with open(self.filename, 'r') as file:
                self.entries = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.entries = []

    def save_entries_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump(self.entries, file, indent=4)
        return 0

    def create_entry(self, data):
        if "user" in data and "pass" in data:
            if(self.search_user(data['user']) == -1):
                self.hash_object.update(data['pass'].encode('utf-8'))
                data['pass'] = self.hash_object.hexdigest()
                self.entries.append(data)
                self.save_entries_to_file()
                return data
            else:
                raise TypeError("Error: the username already exists")
        else:
            raise TypeError("Error: json format not allowed. Format allowed, received:"+str(data)+" allowed:{'user': 'user_name', 'pass': 'password'}")

    def read_entry(self, index):
        if 0 <= index < len(self.entries):
            return self.entries[index]
        else:
            raise TypeError("Error: List Index Out of Range")

    def update_entry(self, index, new_data):
        if 0 <= index < len(self.entries):
            if "user" in new_data and "pass" in new_data:
                self.hash_object.update(new_data['pass'].encode('utf-8'))
                new_data['pass'] = self.hash_object.hexdigest()
                self.entries[index] = new_data
                self.save_entries_to_file()
                return self.entries[index]
            else:
                raise TypeError("Error: json format not allowed. Format allowed, received:"+str(new_data)+" allowed:{'user': 'user_name', 'pass': 'password'}")
        else:
            raise TypeError("Error: List Index Out of Range")

    def delete_entry(self, index):
        if 0 <= index < len(self.entries):
            del self.entries[index]
            data_removed = self.entries[index]
            self.save_entries_to_file()
            return data_removed
        else:
            raise TypeError("Error: List Index Out of Range")
    
    def list_entries(self):
        return self.entries

    def search_user(self, username):
        for indice, diccionario in enumerate(self.entries):
            if diccionario['user'] == username:
                return indice       
        return -1
