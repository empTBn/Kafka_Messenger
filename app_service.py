# app_service.py
import time
from kafka_service import KafkaService
from mongodb_service import MongoDBService


class AppService:
    def __init__(self, mongo_uri, db_name, collection_name, kafka_bootstrap_servers):
        self.mongo_service = MongoDBService(mongo_uri, db_name, collection_name)
        self.kafka_service = KafkaService(kafka_bootstrap_servers)

    def run_console_interface(self):
        while True:
            print("\nSeleccione una opción:")
            print("1. Escribir mensaje")
            print("2. Leer mensajes por tópico")
            print("3. Salir")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                self.write_message()
            elif opcion == "2":
                self.read_messages()
            elif opcion == "3":
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")

    def write_message(self):
        topic = input("Ingrese el nombre del tópico: ")
        message = input("Ingrese el mensaje: ")
        self.kafka_service.produce_message(topic, message)
        self.mongo_service.insert_message({"message": message, "topic": topic})
        print("Mensaje enviado con éxito.")

    def read_messages(self):
        topic = input("Ingrese el nombre del tópico para leer los mensajes: ")
        
        # Implement a timeout of 10 seconds
        timeout = 10
        start_time = time.time()
        
        try:
            # Consume messages from Kafka
            messages = self.kafka_service.consume_messages(topic, timeout=timeout)
        except TimeoutError:
            print("Tiempo de espera agotado. Intenta nuevamente más tarde.")
            return
        except Exception as e:
            print(f"Error al leer mensajes de Kafka: {e}")
            return
        
        print(f"\nMensajes en el tópico '{topic}':")
        for message in messages:
            print(f"- {message}")

        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        print(f"\nTiempo de lectura: {elapsed_time:.2f} segundos")