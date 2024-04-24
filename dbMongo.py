# from pymongo import MongoClient


# Clase para interactuar con la base de datos MongoDB
class MongoDatabase:
    def __init__(self, mongoClient):
        self.client = mongoClient
        self.database = self.client["EncuestasDB"]
        self.collection = self.database["encuestas"]
        self.responsesCollect = self.database["respuestas"]
