from tools.weather import get_weather

print(get_weather("Lyon"))

cities = ["Rome", "Paris", "Mexico City", "Berlin"]
for city in cities:
    print(f"{city}: {get_weather(city)}")
