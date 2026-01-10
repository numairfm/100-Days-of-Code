import requests
import datetime

date = datetime.datetime.now().strftime("%Y%m%d")
print(date)
TOKEN = "0mvqn5vvyn9qvqhuoifkjahervv89a4"
USERNAME = "numair"
pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)
GRAPH = "graph1"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH,
    "name": "Push Ups Daily",
    "unit": "count",
    "type": "int",
    "color": "kuro",
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
pixel_config = {
    "date": date,
    "quantity": "1",
}

headers = {
    "X-USER-TOKEN": TOKEN
}


update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date}"
update_pixel_config = {
    "quantity": "100",
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)

response = requests.delete(url=update_pixel_endpoint, headers=headers)

print(response.text)
