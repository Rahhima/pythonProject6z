
import requests
import time
import logging

logging.basicConfig(filename='weather_api.log', level=logging.ERROR)
def handle_api_error(response):
    if response.status_code == 429:
        print('Rate limit exceeded. Please try again later.')
    elif response.status_code == 401:
        print('Invalid API key. Please check your credentials.')
    elif response.status_code == 404:
        print('Location not found.')
    else:
        print(f'API error: {response.status_code}')

def make_weather_request(location, api_url, api_key):
    url = api_url + "appid=" + api_key + "&q=" + location
    headers = {'x-api-key': api_key}
    retries = 0
    while retries < 3:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f'API request failed: {e}')
            retries += 1
            time.sleep(1 * (2 ** retries))
    handle_api_error(response)

def fetch_weather_data(api_url, city, api_key):
    return make_weather_request(city, api_url, api_key)

def display_weather(data):
    if data is not None:
        if 'main' in data and 'weather' in data:
            temperature = data['main']['temp'] - 273.15  # Convert Kelvin to Celsius
            humidity = data['main']['humidity']
            weather_description = data['weather'][0]['description']
            print(f'Temperature: {temperature:.2f}°C')
            print(f'Humidity: {humidity}%')
            print(f'Weather Description: {weather_description}')
        else:
            print('Invalid API response.')
    else:
        print('No weather data available.')

API_KEY = '8b3e8b8f1ad037250d53e024c138e16'
Base_URL = "https://openweathermap.org/data/2.5/weather?q"
CITY = "London"

weather_data = fetch_weather_data(Base_URL, CITY, API_KEY)
display_weather(weather_data)