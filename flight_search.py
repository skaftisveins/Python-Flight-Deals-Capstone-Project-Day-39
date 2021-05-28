from config import *
import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        location_endpoint = f"{tequila_endpoint}/locations/query"
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=location_endpoint,
                                headers=tequila_headers, params=query)
        result = response.json()["locations"]
        code = result[0]["code"]
        return code
