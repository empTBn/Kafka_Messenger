from pymongo import MongoClient


class MongoDBService:
    def __init__(self, uri, db_name, collection_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_message(self, message):
        self.collection.insert_one(message)

    def get_messages_by_topic(self, topic):
        return self.collection.find({"topic": topic})
