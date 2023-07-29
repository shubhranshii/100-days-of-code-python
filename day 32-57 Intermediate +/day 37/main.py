import requests
from datetime import datetime
import config

USERNAME = config.username
TOKEN = config.token
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {'token': TOKEN,
               'username': USERNAME,
               'agreeTermsOfService': 'yes',
               'notMinor': "yes"}

# response=requests.post(url= PIXELA_ENDPOINT, json= user_params)
# print(response.text)

GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'
GRAPH_ID= 'graph1'

graph_config = {'id': GRAPH_ID,
                'name': 'Running Graph',
                'unit': 'Km',
                'type': 'float',
                'color': 'ajisai'}

token_header = {'X-USER-TOKEN': TOKEN}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=token_header)
# print(response.text)

PIXEL_ENDPOINT=f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime.now()

pixel_params={'date':today.strftime('%Y%m%d'),
              'quantity':input("How many kilometers did you run today?")}

response= requests.post(url= PIXEL_ENDPOINT, json=pixel_params, headers=token_header )
print(response.text)

# UPDATE_ENDPOINT=f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'
#
# update_params={'quantity':'100'}

# response= requests.put(url= UPDATE_ENDPOINT, json=update_params, headers=token_header)
# print(response.text)

# DELETE_ENDPOINT=f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'
# response=requests.delete(url=DELETE_ENDPOINT, headers=token_header)
# print(response.text)