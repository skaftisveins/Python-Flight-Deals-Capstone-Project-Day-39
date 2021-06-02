from config import *
from flight_data import FlightData
import requests
import pprint


class FlightSearch:
    '''This class is responsible for talking to the Flight Search API.'''

    def __init__(self) -> None:
        self.city_codes = []

    def get_destination_codes(self, city_names):
        print("get destination codes triggered")
        location_endpoint = f"{tequila_endpoint}/locations/query"
        for city in city_names:
            query = {
                "term": city,
                "location_types": "city"
            }
            response = requests.get(
                url=location_endpoint,
                headers=tequila_headers,
                params=query
            )
            results = response.json()["locations"]
            code = results[0]["code"]
            self.city_codes.append(code)

        return self.city_codes

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        print(f"Check flights triggered for {destination_city_code}")
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "ISK"
        }

        search_endpoint = f"{tequila_endpoint}/v2/search"
        response = requests.get(
            url=search_endpoint,
            headers=tequila_headers,
            params=query
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            query["max_stopovers"] = 1
            response = requests.get(
                url=search_endpoint,
                headers=tequila_headers,
                params=query,
            )
            data = response.json()["data"][0]
            pprint(data)
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: {flight_data.price} ISK")
            return flight_data
