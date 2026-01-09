import requests

api_key = "3087fff6205c27b2fa9d97d24bdd119d"
endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": 44.34,
    "lon": 10.99,
    "appid": api_key
}

def get_weather(endpoint, p):
    response = requests.get(endpoint, params=p)
    return response

print(get_weather(endpoint, parameters))