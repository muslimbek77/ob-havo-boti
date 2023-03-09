from config import API_KEY
import requests
def get_date(city):
        """Bu weather funksiyasi"""
        data = {
            "q": city,
            "appid": API_KEY
        }
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather", params=data)
        if response.status_code == 200:
            response = response.json()
            return response["main"]["temp"]-273.15
        return None
