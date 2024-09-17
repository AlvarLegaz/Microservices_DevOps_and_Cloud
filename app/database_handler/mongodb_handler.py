from pymongo import MongoClient

class mongodb_handler:
    def __init__(self, db_url, db_name, collection_name):
        try:
            self.client = MongoClient(db_url)
            # MongoDB no realiza conexión inmediatamente a la base de datos cuando se instancia. 
            # En su lugar, la conexión se realiza con la primera operacion.
            # Se realiza ping para asegurarse de que se ha establecido la conexión.
            self.client.admin.command('ping')
            self.db = self.client[db_name]
            self.collection = self.db[collection_name]
        except Exception as e:
            raise Exception("Failed to connect to MongoDB " + str(e))

    def drop_collection(self):
        try:
            self.db[collection_name].drop()
        except Exception as e:
            raise Exception("Fail to drop MongoDB collection: " + str(e))
    
    def create(self, data):
        try:
            return self.collection.insert_one(data).inserted_id
        except Exception as e:
            raise Exception("Error inserting document in MongoDB: " + str(e))

    def read(self, query):
        try:
            return self.collection.find(query)
        except Exception as e:
            raise Exception("Error reading docoment in MongoDB: " +str(e))

    def update(self, query, new_values):
        try:
            return self.collection.update_one(query, {'$set': new_values})
        except Exception as e:
            raise Exception("Error updating docoment in MongoDB: " + str(e))

    def delete(self, query):
        try:
            return self.collection.delete_one(query)
        except Exception as e:
            raise Exception("Error deleting document in MongoDB: " + str(e))

    def list(self):
        try:
            return self.collection.find()
        except Exception as e:
            raise Exception("Error listing documents of MongoDB table: " + str(e))
    
    def list(self, query):
        try:
            return self.collection.find(query)
        except Exception as e:
            raise Exception("Error listing documents of MongoDB table: " + str(e))
    
    def find_one(self, query):
        try:
            return self.collection.find_one(query)
        except Exception as e:
            raise Exception("Error finding document in MongoDB" + str(e))

if __name__ == '__main__':
    # Uso de la clase
    db_url = "mongodb://localhost:27017"
    db_name = 'TestDB'
    collection_name = 'test_collection'
    crudl = mongodb_handler(db_url, db_name, collection_name)

    # Crear un nuevo documento
    print("Create test ...")
    new_document = {'nombre': 'Juan', 'edad': 30}
    print(crudl.create(new_document))

    # Leer documentos
    print("Read test ...")
    query = {'nombre': 'Juan'}
    documents = crudl.read(query)
    for doc in documents:
        print(doc)

    # Actualizar un documento
    print("Update test ...")
    query = {'nombre': 'Juan'}
    new_values = {'edad': 31}
    crudl.update(query, new_values)
    documents = crudl.read(query)
    for doc in documents:
        print(doc)

    # Find user
    print("Find user test ...")
    query = {'nombre': 'Juan', 'edad': 31} 
    document = crudl.find_one(query)
    print(document['nombre'])

    # Eliminar un documento
    print("Delete test ...")
    crudl.delete(query)

    # Listar todos los documentos
    print("List test ...")
    all_documents = crudl.list()
    for doc in all_documents:
        print(doc)

    # Drop collection
    print("Drop test ...")
    crudl.drop_collection()

# Test exceptions

    db_url = "mongodb://localhosssst:27017"
    db_name = 'TestDB'
    collection_name = 'test_collection'
    crudl = mongodb_handler(db_url, db_name, collection_name)

