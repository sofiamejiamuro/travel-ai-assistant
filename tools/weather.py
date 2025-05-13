import os
import requests
import unidecode
from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
print(f"Loaded API KEY: {API_KEY}")


def get_weather(location, country_code="mx"):
    if not API_KEY:
        return "Weather data unavailable (missing API key)"

    # Normalize and encode location
    clean_location = unidecode.unidecode(location.strip().title())
    #encoded_location = quote(f"{clean_location},{country_code}")
    encoded_location = quote(clean_location)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={encoded_location}&appid={API_KEY}&units=metric"

    print(f"Fetching weather for: {clean_location}")
    print(f"Request URL: {url}")

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return f"Error {response.status_code}: {data.get('message', 'No message')}"

        condition = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return f"{condition}, {temp}°C"

    except Exception as e:
        return f"Weather data unavailable ({str(e)})"
