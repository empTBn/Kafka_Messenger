# app_service.py
from kafka_service import KafkaService
from mongodb_service import MongoDBService
from datetime import datetime


class AppService:
    def __init__(self, mongo_uri, db_name, collection_name, kafka_bootstrap_servers):
        self.mongo_service = MongoDBService(mongo_uri, db_name, collection_name)
        self.kafka_service = KafkaService(kafka_bootstrap_servers)
        self.username = None
        self.current_topic = None

    def run_console_interface(self):
        self.username = input("Ingrese su nombre de usuario: ")
        while True:
            print("\nSeleccione una opción:")
            print("1. Seleccionar un topic")
            print("2. Escribir mensaje")
            print("3. Leer mensajes")
            print("4. Cambiar de topic")
            print("5. Salir")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self.select_topic()
            elif opcion == "2":
                self.write_message()
            elif opcion == "3":
                self.read_messages()
            elif opcion == "4":
                self.select_topic()
            elif opcion == "5":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")

    def select_topic(self):
        # Obtener todos los topics disponibles en la base de datos
        topics = self.mongo_service.get_all_topics()

        # Mostrar los topics disponibles al usuario
        print("Topics disponibles:")
        for topic in topics:
            print(topic)

        # Pedir al usuario que ingrese el nombre del topic
        topic = input("Ingrese el nombre del topic: ")

        # Verificar si el topic ingresado está en la lista de topics disponibles
        if topic not in topics:
            print("Error: El topic ingresado no existe.")
            return

        # Asignar el topic seleccionado como el topic actual
        self.current_topic = topic
        print(f"Topic seleccionado: {topic}")

    def write_message(self):
        topic = input("Ingrese el nombre del topic: ")
        message = input("Ingrese el mensaje: ")
        print("tipo de topic", type(topic))
        print(topic)
        self.kafka_service.produce_message(topic, message)

        json_message = {
            "autor": self.username,
            "timestamp": datetime.now(),
            "texto": message,
        }
        self.mongo_service.insert_message(json_message, topic)
        print("Mensaje enviado con éxito.")

    def read_messages(self):
        topic = input("Ingrese el nombre del topic: ")
        messages = self.kafka_service.consume_messages(topic)
        print(f"\nMensajes en el tópico '{self.current_topic}':")
        for message in messages:
            print(f"- {message}")
