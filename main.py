import requests
from datetime import datetime

USERNAME = "luink-habit"
TOKEN = "fdBap894TlCkIlyJCkyMt2cewK7IvBqKbqk-765igpY"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "coding101"

user_body = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

headers_data = {
    "X-USER-TOKEN": TOKEN
}


# Step 1 - Create a user
# response = requests.post(url=pixela_endpoint, json=user_body)
# print(response.text)

# Step 2 - Create a graph
# graph_url = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": GRAPH,
#     "name": "Side Hustle Graph",
#     "unit": "minutes",
#     "type": "float",
#     "color": "sora",
#     "timezone": "Asia/Kuala_Lumpur"
# }
#
# # response = requests.post(url=graph_url, json=graph_config, headers=headers_data)
# # print(response.text)

# Step 3 - Post a pixel
pixel_url = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
date_entry = today.strftime("%Y%m%d")

pixel_config = {
    "date": date_entry,
    "quantity": "65",
    "optionalData": "{\"notes\":\"Learned about POST, PUT and DELETE API in Python\"}"
}

response = requests.post(url=pixel_url, json=pixel_config, headers=headers_data)
print(response.text)
