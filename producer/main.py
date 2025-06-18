import json
import xmltodict

from api import Api


def main():
    print("Executing main function")
    base_url = "https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx"
    api = Api(base_url)

    api_key = api.get_api_key()
    url_suffix = f"?key={api_key}&mapid=40380"
    response = api.get_request(url_suffix)

    response_dict = xmltodict.parse(response)
    json_data = json.dumps(response_dict, indent=4)
    print(json_data)


if __name__ == "__main__":
    main()
