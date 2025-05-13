import re
from unidecode import unidecode
from tools.routes import get_mock_route
from tools.pois import get_mock_pois
from tools.weather import get_weather
from tools.search import search_travel_info


def extract_city_name(location: str) -> str:
    # Removes prefixes like "Start in", "Stop X:", "Arrival in"
    keywords = ["start in", "stop", "arrival in", "arrive in"]
    text = location.lower()
    for key in keywords:
        if key in text:
            text = text.split(key)[-1]
    return unidecode(text.strip()).title()

def evaluate_itinerary(origin, destination, preferences, itinerary_text):
    score = 0
    details = []

    # 1. Route Feasibility
    route = get_mock_route(origin, destination)
    if route and len(route) >= 3:
        score += 1
        details.append("✅ Route has multiple stops.")
    else:
        details.append("❌ Route is too short or missing.")

    # 2. POIs Present
    if all(get_mock_pois(stop) for stop in route):
        score += 1
        details.append("✅ POIs are present for each stop.")
    else:
        details.append("❌ Missing POIs in one or more stops.")

    # 3. Weather Info
    weather_ok = True
    for stop in route:
        print(f"🔍 Original stop: {stop}")
        city = extract_city_name(stop)
        print(f"🛰️ Extracted city: {city}")
        weather = get_weather(city)
        if "error" in weather.lower() or "unavailable" in weather.lower():
            weather_ok = False
            break

    # 4. Preference Matching
    pref_list = preferences.lower().split(", ")
    match_count = sum(pref in itinerary_text.lower() for pref in pref_list)
    if match_count:
        score += 1
        details.append("✅ Preferences reflected in itinerary.")
    else:
        details.append("❌ Preferences not matched.")

    return {
        "score": score,
        "max_score": 4,
        "details": details
    }

# Example usage
if __name__ == "__main__":
    test = evaluate_itinerary(
        origin="Frankfurt",
        destination="Barcelona",
        preferences="avoid bad weather, include cultural sites",
        itinerary_text="""
        Start in Frankfurt - POIs: Frankfurt Cathedral
        Parada 1: Strasbourg - POIs: Petite France
        Parada 2: Lyon - POIs: Roman Theatre
        Arrival in Barcelona - POIs: Sagrada Familia
        """
    )
    for line in test["details"]:
        print(line)
    print(f"\nFinal Score: {test['score']}/{test['max_score']}")