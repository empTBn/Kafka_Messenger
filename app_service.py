from mongodb_service import MongoDBService
from kafka_service import KafkaService


class AppService:
    def __init__(self, db_name, collection_name, kafka_bootstrap_servers):
        self.mongo_service = MongoDBService(db_name, collection_name)
        self.kafka_service = KafkaService(kafka_bootstrap_servers)

    def send_message(self, message, topic):
        # Envía un mensaje a Kafka y lo almacena en MongoDB
        self.kafka_service.produce_message(topic, message)
        self.mongo_service.insert_message({"message": message, "topic": topic})

    def read_messages(self):
        # Lee todos los mensajes almacenados en MongoDB
        return self.mongo_service.get_messages()
