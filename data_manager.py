from config import *
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.destination_data = {}
        
    def get_destination_data(self):
        response = requests.get(
            sheety_prices_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
        
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(f"{sheety_prices_endpoint}/{city['id']}", json=new_data, headers=sheety_headers)
            print(response.text)
    
        
