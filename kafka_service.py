from confluent_kafka import Producer, Consumer


class KafkaService:
    def __init__(self, bootstrap_servers):
        self.producer = Producer({"bootstrap.servers": bootstrap_servers})
        self.consumer = Consumer(
            {"bootstrap.servers": bootstrap_servers, "group.id": "my_group"}
        )

    def produce_message(self, topic, message):
        # Produce un mensaje en un topic específico
        self.producer.produce(topic, message.encode("utf-8"))
        self.producer.flush()

    def consume_messages(self, topic):
        # Se suscribe a un topic y consume mensajes
        self.consumer.subscribe([topic])
        while True:
            msg = self.consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                print("Error al consumir mensaje: {}".format(msg.error()))
                continue
            print("Mensaje recibido: {}".format(msg.value().decode("utf-8")))
