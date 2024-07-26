from pymongo import MongoClient

class mongodb_handler:
    def __init__(self, db_url, db_name, collection_name):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create(self, data):
        return self.collection.insert_one(data).inserted_id

    def read(self, query):
        return self.collection.find(query)

    def update(self, query, new_values):
        return self.collection.update_one(query, {'$set': new_values})

    def delete(self, query):
        return self.collection.delete_one(query)

    def list(self):
        return self.collection.find()
    
    def find_one(self, query):
        return self.collection.find_one(query)

if __name__ == '__main__':
    # Uso de la clase
    db_url = "mongodb://localhost:27017"
    db_name = 'prueba1'
    collection_name = 'mi_coleccion'
    crudl = mongodb_handler(db_url, db_name, collection_name)

    # Crear un nuevo documento
    new_document = {'nombre': 'Juan', 'edad': 30}
    print(crudl.create(new_document))

    # Leer documentos
    query = {'nombre': 'Juan'}
    documents = crudl.read(query)
    for doc in documents:
        print(doc)

    # Actualizar un documento
    new_values = {'edad': 31}
    crudl.update(query, new_values)

    # Eliminar un documento
    crudl.delete(query)

    # Listar todos los documentos
    all_documents = crudl.list()
    for doc in all_documents:
        print(doc)
