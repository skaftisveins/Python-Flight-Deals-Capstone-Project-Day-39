#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_destination_data()
print(sheet_data)

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet data:\n {sheet_data}")
    
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()