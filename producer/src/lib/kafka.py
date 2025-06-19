import sys
from confluent_kafka.admin import (
    AdminClient,
    NewTopic,
    KafkaException,
    KafkaError,
)
from confluent_kafka import Producer


class Kafka:

    def __init__(self) -> None:
        self.admin_client = AdminClient({"bootstrap.servers": "localhost:9092"})
        print("Kafka Admin Client Successfully Initialized")

    def _delivery_report(self, err, msg):
        """Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush()."""
        if err is not None:
            print("Message delivery failed: {}".format(err))
        else:
            print("Message delivered to {} [{}]".format(msg.topic(), msg.partition()))

    def create_topic(
        self, name: str, partitions: int = 1, replication_factor: int = 1
    ) -> None:

        topic = NewTopic(name, partitions, replication_factor)
        fs = self.admin_client.create_topics([topic])
        for topic, future in fs.items():
            try:
                future.result()
                print(f"Successfully created topic named: {name}")
            except KafkaException as e:
                if (
                    isinstance(e.args[0], KafkaError)
                    and e.args[0].code() == KafkaError.TOPIC_ALREADY_EXISTS
                ):
                    print(f"Kafka topic {name} already exists, continuing...")
                else:
                    print(f"Error creating Kafka topic {name} - {e}")
                    sys.exit(1)

    def create_producer(self):
        print(f"Initializing producer...")
        self.producer = Producer({"bootstrap.servers": "localhost:9092"})

    def send_message(self, topic: str, data: str):
        self.producer.poll(0)
        self.producer.produce(
            topic, data.encode("utf-8"), callback=self._delivery_report
        )
        self.producer.flush()
