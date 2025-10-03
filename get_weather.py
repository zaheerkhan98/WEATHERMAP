# get_weather.py
# This file is used to fetch weather details from the OpenWeatherMap API

import requests   # requests is a library to call APIs 

def get_weather(city, api_key):
    """
    This function takes a city name and API key as input.
    It calls the OpenWeatherMap API and returns weather details as a dictionary.
    If the city is invalid, it returns None.
    """

    # The URL to fetch weather data (units=metric means we get Celsius)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Send a request to the API
    response = requests.get(url)

    # Convert the response to JSON (dictionary format)
    data = response.json()

    # Check if city is valid (if not valid, API returns "cod" other than 200)
    if data.get("cod") != 200:
        return None

    # Extract required details
    weather = {
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"]
    }

    return weather
