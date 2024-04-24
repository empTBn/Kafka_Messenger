# app.py
from app_service import AppService


def main():
    # Configurar los parámetros de conexión a MongoDB y Kafka
    mongo_uri = "mongodb://localhost:27017/"
    db_name = "mensajes"
    collection_name = "mensajes"
    kafka_bootstrap_servers = "localhost:9092"

    # Inicializar el servicio de la aplicación
    app_service = AppService(
        mongo_uri, db_name, collection_name, kafka_bootstrap_servers
    )

    # Ejecutar la interfaz de consola
    app_service.run_console_interface()


if __name__ == "__main__":
    main()
