from confluent_kafka import Producer, Consumer, KafkaError
import json

class KafkaClient:
    
    def __init__(self, broker, group_id):
        self.broker = broker
        self.group_id = group_id

    def _delivery_report(self, err, msg):
        if err is not None:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

    def produce_message(self, topic, message):
        producer_conf = {
            'bootstrap.servers': self.broker,
            'client.id': 'my_producer',
        }
        producer = Producer(producer_conf)
        producer.produce(topic, json.dumps(message), callback=self._delivery_report)
        producer.flush()

    def consume_messages(self, topic, callback):
        consumer_conf = {
            'bootstrap.servers': self.broker,
            'group.id': self.group_id,
            'auto.offset.reset': 'earliest',  # Start consuming from the beginning of the topic
        }
        consumer = Consumer(consumer_conf)
        consumer.subscribe([topic])
        
        try:
            while True:
                msg = consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition, no more messages
                        continue
                    else:
                        print(f'Consumer error: {msg.error()}')
                        break
                callback(msg.value().decode("utf-8"))
        finally:
            consumer.close()


# Example usage:
if __name__ == "__main__":
    kafka_client = KafkaClient(broker='localhost:9092', group_id='my_consumer_group')
    
    # Example sending message
    message = {"key": "value"}
    kafka_client.produce_message(topic='my_topic', message=message)

    # Example consuming messages
    def message_handler(message):
        print(f'Received message: {message}')
    
    kafka_client.consume_messages(topic='my_topic', callback=message_handler)