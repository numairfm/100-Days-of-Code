import requests
import dotenv
import os
dotenv.load_dotenv()
class FlightSearch:
    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API_KEY")
        self._secret = os.environ.get("AMADEUS_SECRET")
        self._token = self._get_new_token()
        
        

    def _get_new_token(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._secret
        }

        response = requests.post("https://test.api.amadeus.com/v1/security/oauth2/token", headers=headers, data=body)
        return response.json()
    
    def get_code(self, city):
        headers = {
            "Authorization": f"Bearer {self._token["access_token"]}"
        }

        city_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        parameters = {
            "keyword": city,
                "max": 1,
        }

        response = requests.get(city_endpoint, headers=headers, params=parameters)
        response.raise_for_status()
        data = response.json()
        iata_code = data["data"][0]["iataCode"]
        print(iata_code)
        return iata_code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"Authorization": f"Bearer {self._token['access_token']}"}
        
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time,
            "returnDate": to_time,       
            "adults": 1,
            "nonStop": "false",          
            "currencyCode": "PHP",
            "max": 5,                   
        }

        response = requests.get(
            url="https://test.api.amadeus.com/v2/shopping/flight-offers",
            headers=headers,
            params=query
        )

        if response.status_code != 200:
            print(f"Check flights failed for {destination_city_code}: {response.text}")
            return None

        return response.json()

