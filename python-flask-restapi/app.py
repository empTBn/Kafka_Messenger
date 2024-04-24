from app_service import AppService

from dbMongo import MongoDatabase           # Importa la clase MongoDatabase
from pymongo import MongoClient
from kafka import KafkaClient

from flask import Flask

# Configuración de la base de datos MongoDB
MONGO_HOST = os.getenv("DB_HOST_MONGO")
MONGO_PORT = os.getenv("DB_PORT_MONGO")
MONGO_USER = os.getenv("DB_USER_MONGO")
MONGO_PASSWORD = os.getenv("DB_PASSWORD_MONGO")

# Inicializar la conexión al cliente de Kafka

kafka_client = KafkaClient(broker='localhost:9092', group_id='my_consumer_group')

# Inicializar la conexión a la base de datos MongoDB
client = MongoClient(
    f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/?authSource=admin"
)
mongo_db = MongoDatabase(client)

# Inicializar la instancia de AppService con ambas conexiones de base de datos
appService = AppService(mongo_db)


# ------------------------------------------------------------------- Inicializar la aplicación Flask -------------------------------------------------------------------
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "1234"  # Cambia esto por tu clave secreta


# -------------------------------------------------------------------- Autenticación y Autorización --------------------------------------------------------------------

