from dbMongo import MongoDatabase  # Importa la clase MongoDatabase
from kafkaSetup import KafkaClient  # Importa la clase KafkaClient

class AppService:
    def __init__(
        self,
        mongo_database: MongoDatabase,
        kafka_client: kafkaClient,
    ):
        self.mongo_database = mongo_database
        self.kafka_client = kafkaClient