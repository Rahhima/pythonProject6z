# Rahhim Adeem

import requests
def fetch_weather_data(api_url, city, api_key):
    """
    Fetches weather data from OpenWeatherMap API.
    Returns:
        dict: JSON response from the API containing weather data.
    """
    url = api_url + "appid=" + api_key + "&q=" + city
    response = requests.get(url).json()
    return response

API_KEY = 'b3e75979e3e807cb3d4a1ebaaf080cbc'
Base_URL = "https://openweathermap.org/data/2.5/weather?q=brisbane&appid=" + API_KEY
CITY = "London"

weather_data = fetch_weather_data(Base_URL, CITY, API_KEY)
print(weather_data)