# app.py
from Controller import Controller


def main():
    mongo_uri = "mongodb://localhost:27017/"
    db_name = "MensajesDB"
    collection_name = "topics"
    kafka_bootstrap_servers = "localhost:9092"

    # Inicializar el servicio de la aplicación
    app_service = Controller(
        mongo_uri, db_name, collection_name, kafka_bootstrap_servers
    )

    # Ejecutar la interfaz de consola
    app_service.run_console_interface()


if __name__ == "__main__":
    main()
