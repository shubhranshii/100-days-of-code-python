

import requests
from twilio.rest import Client
import config

API_KEY = config.api_key
ACCOUNT_SID = config.account_sid
AUTH_TOKEN = config.auth_token
MY_PHONE = config.my_phone
OW_MAP_ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall?"

weather_parameters = {
    "lat": 61.566667,
    "lon": -123.283333,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",

}

response = requests.get(url=OW_MAP_ENDPOINT, params=weather_parameters)
response.raise_for_status()
data = response.json()

required_data = data['hourly'][0:13]
will_rain = False

for hour in required_data:
    id = hour['weather'][0]['id']
    if id < 700:
        will_rain = True
        break

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="Its going to rain. Bring an umbrella!",
        from_='+12295973709',
        to=MY_PHONE
    )
    print(message.status)
