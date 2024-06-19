import app
import json
import hashlib

class UsersJsonFileManager:
    def __init__(self, filename):
        self.filename = filename
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
                return 0
            else:
                print("Error: El nombre de usuario ya existe")
                return -2
        else:
            print("Recibido: " + str(data))
            print("Error: El formato de los datos es incorrecto. Debe ser {'user': 'nombre_usuario', 'pass': 'contraseña'}.")
            return -1

    def read_entry(self, index):
        if 0 <= index < len(self.entries):
            return self.entries[index]
        else:
            print("Error: Indice fuera de rango")
            return null

    def update_entry(self, index, new_data):
        if 0 <= index < len(self.entries):
            if "user" in new_data and "pass" in new_data:
                self.entries[index] = new_data
                self.save_entries_to_file()
                return 0
            else:
                print("Error: El formato de los datos es incorrecto.")
                return -1
        else:
            print("Error: Indice fuera de rango.")
            return -1

    def delete_entry(self, index):
        if 0 <= index < len(self.entries):
            del self.entries[index]
            self.save_entries_to_file()
            return 0
        else:
            print("Error: Indice fuera de rango.")
            return -1
    
    def list_entries(self):
        return self.entries

    def search_user(self, username):
        for indice, diccionario in enumerate(self.entries):
            if diccionario['user'] == username:
                return indice       
        return -1



