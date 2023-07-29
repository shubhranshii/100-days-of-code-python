import os
from datetime import datetime
import requests

class Sheet:

    def __init__(self):
        self.endpoint=os.environ['SHEET_ENDPOINT']
        self.auth_header= os.environ['AUTHORIZATION_HEADER']

    def add_data(self, result):
        today_date = datetime.now().strftime("%d/%m/%Y")
        now_time = datetime.now().strftime("%X")

        for exercise in result["exercises"]:
            sheet_inputs = {
                "workout": {
                    "date": today_date,
                    "time": now_time,
                    "exercise": exercise["name"].title(),
                    "duration": exercise["duration_min"],
                    "calories": exercise["nf_calories"]
                }
            }

            sheet_response = requests.post(self.endpoint, json=sheet_inputs,
                                           headers={'Authorization': self.auth_header})

            print(sheet_response.text)
