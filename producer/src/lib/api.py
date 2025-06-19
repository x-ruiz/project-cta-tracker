import requests
import os

from dotenv import load_dotenv


class Api:
    def __init__(self, base_url: str):
        load_dotenv()

        self.base_url = base_url
        self.api_key = os.getenv("API_KEY")

    def get_api_key(self):
        return self.api_key

    def get_request(self, url_suffix: str) -> str:
        """
        Makes a get request to a specified url and returns the response as text
        """
        response = requests.get(self.base_url + url_suffix)
        return response.text
