from confluent_kafka import Consumer
import json
from datetime import datetime
import sys

c = Consumer(
    {
        "bootstrap.servers": "localhost:9092",
        "group.id": "mygroup",
        "auto.offset.reset": "earliest",
    }
)

c.subscribe(["map-id-40380"])

while True:
    msg = c.poll(1.0)

    if msg is None:
        print("Msg is none")
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    current_timestamp = datetime.now()
    print(f"Received message @ {current_timestamp}")
    message = msg.value().decode("utf-8")
    message_dict = json.loads(message)
    eta = message_dict["ctatt"]["eta"][0]
    stop_name = eta["staNm"]
    stop_dest = eta["stpDe"]
    arrival_time = eta["arrT"]
    print(f"Arrival time for {stop_name} -> {stop_dest} is {arrival_time}")
