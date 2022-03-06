import requests
from datetime import datetime

USERNAME = "eduka"
TOKEN = "edohabits"
pixela_endpoint = 'https://pixe.la/v1/users'
ID = "g1"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# r = requests.post(url=pixela_endpoint, json=user_params)
# print(r.json())

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {
"X-USER-TOKEN": TOKEN
}
graph_config = {
    "id": ID,
    "name": "coding",
    "unit": "hours",
    "type": "int",
    "color": "sora"

}
# rgc = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(rgc.text)

graph_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

today = datetime.now()

graph_value = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5",


}

# gvd = requests.post(url=graph_value_endpoint, json=graph_value, headers=headers)
# print(gvd.text)

graph_value_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/20220306"

graph_value_update = {
    "quantity": "8",

}

# gvu = requests.put(url=graph_value_update_endpoint, json=graph_value_update, headers=headers)
# print(gvu.text)

#gdelete = requests.delete(url=graph_value_update_endpoint, json=graph_value_update, headers=headers)
print(gdelete.text)
