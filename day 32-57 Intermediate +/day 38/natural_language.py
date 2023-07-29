import requests
import os

class Exercises:
    def __init__(self):
        self.app_id= os.environ['APP_ID']
        self.app_key= os.environ['API_KEY']
        self.gender=os.environ['GENDER']
        self.weight=os.environ['WEIGHT_KG']
        self.height=os.environ['HEIGHT_CM']
        self.age=os.environ['AGE']

    def estimate_calories(self, text):
        user_params = {
            "query": text,
            "gender": self.gender,
            "weight_kg": self.weight,
            "height_cm": self.height,
            "age": self.age
        }

        headers = {
            'x-app-id': os.environ['APP_ID'],
            'x-app-key': os.environ['API_KEY']
        }

        response = requests.post(url=os.environ['EXERCISE_API_ENDPOINT'], json=user_params, headers=headers)
        result = response.json()
        return result