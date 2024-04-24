from kafka import KafkaProducer, KafkaConsumer


class KafkaService:
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    def produce_message(self, topic, message):
        self.producer.send(topic, message.encode("utf-8"))
        self.producer.flush()

    def consume_messages(self, topic):
        consumer = KafkaConsumer(
            topic,
            group_id="my-group",
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            value_deserializer=lambda x: x.decode("utf-8"),
        )
        return consumer
