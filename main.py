# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from config import *
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime as dt, timedelta
import requests

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

print("Welcome to Skafti's Flight Club.")
print("We find the best flight deals and email you the details.")
first_name = input("What is your first name?")
last_name = input("What is your last name?")
user_email = input("What is your email?")
verify_email = input("Type your email again.")

if user_email == verify_email:
    new_member = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": user_email
        }
    }
    response = requests.post(
        sheety_users_endpoint, headers=sheety_headers, json=new_member)
    print(response.text)
    
    print("Congrats! You're in the club")
else:
    None


sheet_data = data_manager.get_destination_data()
data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    print(city_names)

    codes = flight_search.get_destination_code(city_names)
    data_manager.update_destination_codes(codes)
    sheet_data = data_manager.get_destination_data()

tomorrow = dt.now() + timedelta(days=1)
six_months_from_today = dt.today() + timedelta(6 * 30)

for destination in sheet_data:
    flight = flight_search.check_flights(
        origin_city_iata,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )

    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_email(
            message=f"Það kostar aðeins {flight.price} kr. að fljúga frá {flight.origin_city}-{flight.origin_airport} til {flight.destination_city}-{flight.destination_airport}, frá {flight.out_date} til {flight.return_date}")
