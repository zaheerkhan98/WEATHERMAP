# view_weather.py
# This file is used to display the weather details in a nice way

def view_weather(weather_data):
    """
    This function takes the weather dictionary and prints it nicely.
    If data is None (invalid city), it shows an error message.
    """
    if weather_data:
        print("\n----- Weather Report -----")
        print("City:", weather_data['city'])
        print("Temperature:", weather_data['temperature'], "°C")
        print("Humidity:", weather_data['humidity'], "%")
        print("Description:", weather_data['description'].capitalize())
        print("---------------------------\n")
    else:
        print("\n City not found! Please try again.\n")
