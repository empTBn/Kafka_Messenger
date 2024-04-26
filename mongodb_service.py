from pymongo import MongoClient


class MongoDBService:
    def __init__(self, uri, db_name, collection_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_message(self, message, current_topic):
        topic_document = self.collection.find_one({"topic": current_topic})

        # Si no se encuentra el documento, crea uno nuevo
        if topic_document is None:
            topic_document = {"topic": current_topic, "mensajes": []}

        # Añade el mensaje a la lista de mensajes del topic
        topic_document["mensajes"].append(message)

        # Actualiza o inserta el documento en la colección
        self.collection.update_one(
            {"topic": current_topic}, {"$set": topic_document}, upsert=True
        )

    def get_all_topics(self):
        # Obtener todos los documentos de la colección "topics"
        cursor = self.collection.find({}, {"topic": 1, "_id": 0})

        # Extraer los nombres de los topics de los documentos
        topics = [doc["topic"] for doc in cursor]

        return topics
