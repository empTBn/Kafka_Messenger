from pymongo import MongoClient


class MongoDBService:
    def __init__(self, db_name, collection_name):
        self.client = MongoClient("mongodb://root:password@mongo:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_message(self, message):
        # Inserta un mensaje en la colección
        self.collection.insert_one(message)

    def get_messages(self):
        # Obtiene todos los mensajes de la colección
        return list(self.collection.find())
