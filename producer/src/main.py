import json
import xmltodict
import time

from lib.api import Api
from lib.kafka import Kafka


def extract_data() -> str:
    print("Extracting data to send")
    base_url = "https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx"
    api = Api(base_url)

    api_key = api.get_api_key()
    url_suffix = f"?key={api_key}&mapid=40380"
    response = api.get_request(url_suffix)

    response_dict = xmltodict.parse(response)
    json_data = json.dumps(response_dict, indent=4)
    return json_data


if __name__ == "__main__":
    # Initialize kafka client, topic, and producer
    topic = "map-id-40380"
    k = Kafka()
    k.create_topic(topic)
    k.create_producer()

    # Extract data and send message
    while True:
        data = extract_data()
        k.send_message(topic, data)
        time.sleep(15)
