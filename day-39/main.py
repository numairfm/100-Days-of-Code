import requests
import dotenv
from datetime import datetime, timedelta
import os
import time
from typing import List, Dict
from flight_data import *
from flight_search import *

dotenv.load_dotenv()

ORIGIN_CITY_IATA = "MAN"
tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
six_month_from_today = (datetime.now() + timedelta(days=(6 * 30))).strftime("%Y-%m-%d")

sheet_endpoint = "https://api.sheety.co/2528d8d0252d85c380192c34c3400188/flightPrices/sheet1"
class DataManager:
    def __init__(self):
        self.sheet_data: List[Dict] = []
        self.SHEETY_API_KEY = os.environ.get("SHEETY_API_KEY")
        self.HEADERS = {"Authorization": self.SHEETY_API_KEY}


    def get_data(self):
        response = requests.get(sheet_endpoint, headers=self.HEADERS)
        response.raise_for_status()

        data = response.json().get("sheet1")

        self.sheet_data = data
        return self.sheet_data

    def update_codes(self):
        for row in self.sheet_data:
            if row.get("city") and row.get("city").strip():
                new_data = {
                    "sheet1": {
                        "iataCode": flight_search.get_code(row["city"])

                    }
                }
                put_endpoint = f"{sheet_endpoint}/{row["id"]}"
                response = requests.put(put_endpoint, json=new_data, headers=self.HEADERS)
                response.raise_for_status()
                print(response.json())


if __name__ == "__main__":
    flight_search = FlightSearch()
    data_man = DataManager()
    
    sheet_data = data_man.get_data()

    if sheet_data[0]["iataCode"] == "":
        data_man.update_codes()
        sheet_data = data_man.get_data()

    for destination in sheet_data:
        if destination["iataCode"]:
            print(f"Searching for flights to {destination['city']}...")
            
            raw_flight_json = flight_search.check_flights(
                origin_city_code="MAN", 
                destination_city_code=destination["iataCode"], 
                from_time="2026-01-20",  
                to_time="2026-01-27"
            )

            cheapest_flight = find_cheapest_flight(raw_flight_json)
            
            if cheapest_flight.price != "N/A":
                print(f"{destination['city']}: {cheapest_flight.price}")
        else:
            print(f"Skipping {destination['city']} - No IATA code found.")
