# weather.py

import requests

def get_weather(city):
    api_key = 'a66a30770a0f4fb6b7f210451251201'  # Replace with your actual API key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['current']['temp_c']
        condition = data['current']['condition']['text']
        print(f"Temperature in {city}: {temperature}°C")
        print(f"Weather condition: {condition}")
    else:
        print("Error fetching weather data.")

# Example usage
get_weather("Nigeria")
