# app_service.py
from kafka_service import KafkaService
from mongodb_service import MongoDBService
from datetime import datetime
import json


class Controller:
    def __init__(self, mongo_uri, db_name, collection_name, kafka_bootstrap_servers):
        self.mongo_service = MongoDBService(mongo_uri, db_name, collection_name)
        self.kafka_service = KafkaService(kafka_bootstrap_servers)
        self.username = None
        self.current_topic = "General"

    def run_console_interface(self):
        self.username = input("Ingrese su nombre de usuario: ")
        self.select_topic()
        while True:
            print("\nSeleccione una opción:")
            print("1. Escribir mensaje")
            print("2. Leer mensajes")
            print("3. Cambiar de topic")
            print("4. Salir")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self.write_message()
            elif opcion == "2":
                self.read_messages()
            elif opcion == "3":
                self.select_topic()
            elif opcion == "4":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")

    def select_topic(self):
        # Obtener todos los topics disponibles en la base de datos
        topics = self.mongo_service.get_all_topics()
        print(topics)
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
        input_mesg = input("Ingrese el mensaje: ")

        # Construir el mensaje en formato JSON
        json_message = {
            "autor": self.username,
            "timestamp": datetime.now().isoformat(),
            "mensaje": input_mesg,
        }

        # Enviar el mensaje a Kafka
        self.kafka_service.produce_message(topic, json.dumps(json_message))
        self.mongo_service.insert_message(json_message, topic)
        print("Mensaje enviado con éxito.")

    def read_messages(self):
        topic = input("Ingrese el nombre del topic: ")
        print(f"\nMensajes en el tópico '{topic}':")

        consumer = self.kafka_service.consume_messages(topic)
        try:
            while True:
                message = next(consumer, None)
                if message is None:
                    consumer.close()
                    break
                # Decodificar el mensaje JSON
                try:
                    json_message = json.loads(message.value)
                    author = json_message.get("autor")
                    timestamp = json_message.get("timestamp")
                    message_text = json_message.get("mensaje")
                    print(
                        f"Autor: {author}, Timestamp: {timestamp}, Msg: {message_text}"
                    )
                except json.JSONDecodeError:
                    print("Error: El mensaje no está en formato JSON")
        except KeyboardInterrupt:
            consumer.close()
            print("Lectura de mensajes interrumpida.")
