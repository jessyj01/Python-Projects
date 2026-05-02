from datetime import datetime
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_user_input():
    print("Enter the city name and date:")
    city = input("City: ")
    date = input("Optional - Date (MM-DD): ")
    num_days = 1
    
    if date:
        while True:
            try:
                date = datetime.strptime(date, "%m-%d").replace(year=2026).date()
                num_days = abs((date - datetime.now().date()).days) + 1
                if num_days>10:
                    print("Date is too far in the past. Please enter a date within the last 10 days.")
                    date = input("Date (MM-DD): ")
                else:
                    return city, num_days
            except ValueError:
                print("Invalid date format. Please enter the date in MM-DD format.")
                date = input("Date (MM-DD): ")
    else:
        return city, num_days


def get_weather_data(city, num_days):
    api_key = os.getenv("MY_API_KEY")
    base_url = os.getenv("BASE_URL")

    response = requests.get(f"{base_url}?q={city}&appid={api_key}&cnt={num_days}")

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print((response.json().get("message")).capitalize())
    else:
        print(f"Error: {response.status_code} - {response.reason}")