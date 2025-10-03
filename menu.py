# menu.py
# This file contains the main menu and connects the functions

from get_weather import get_weather   
from view_weather import view_weather 

def menu(api_key):
    """
    This function shows the menu to the user.
    Based on user input, it fetches and displays the weather.
    """

    while True:  # keep showing the menu until user exits
        print("===== Weather Map Application =====")
        print("1. Get Weather by City")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            # Ask for city name
            city = input("Enter city name: ")

            # Fetch weather using API
            weather_data = get_weather(city, api_key)

            # Display the result
            view_weather(weather_data)

        elif choice == "2":
            print("\nExiting program...\n")
            break

        else:
            print("\nInvalid choice! Please enter 1 or 2.\n")
