from acquisition import Acquisition
from config import *
import requests

# acquisition = Acquisition("", "", "", "")

class DataManager:
    '''This class is responsible for talking to the Google Sheet.'''

    def __init__(self) -> None:
        self.destination_data = {}
        self.users_data = {}

    def get_destination_data(self):
        response = requests.get(
            sheety_prices_endpoint, headers=sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def get_users_data(self):
        response = requests.get(sheety_users_endpoint, headers=sheety_headers)
        data = response.json()
        self.users_data = data["users"]
        return self.users_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                f"{sheety_prices_endpoint}/{city['id']}", json=new_data, headers=sheety_headers)
            print(response.text)
            
    # def update_users(self):
    #     for user in self.users_data:
    #         new_member = {
    #             "user":{
    #                 "firstName": user[acquisition.first_name],
    #                 "lastName": user[acquisition.last_name],
    #                 "email": user[acquisition.user_email]
    #             }
    #         }
    #         response = requests.post(sheety_users_endpoint, headers=sheety_headers, json=new_member)
    #         print(response.text)
