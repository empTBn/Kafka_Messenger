from kafka import KafkaProducer, KafkaConsumer
import threading

class KafkaService:
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers
        self.consumer = KafkaConsumer(
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            value_deserializer=lambda x: x.decode("utf-8"),
        )

    def produce_message(self, topic, message):
        producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)
        producer.send(topic, message.encode("utf-8"))
        producer.flush()

    def consume_messages(self, topic, timeout=None):
        self.consumer.subscribe([topic])  # Subscribe to the topic
        messages = []

        def message_fetcher():
            nonlocal messages
            for message in self.consumer:
                messages.append(message.value)

        # Start message fetching thread
        fetch_thread = threading.Thread(target=message_fetcher)
        fetch_thread.start()

        # Wait for the thread to finish or timeout
        fetch_thread.join(timeout)

        # If the thread is still running, stop it
        if fetch_thread.is_alive():
            self.consumer.close()
            raise TimeoutError("Tiempo de espera agotado.")

        return messages