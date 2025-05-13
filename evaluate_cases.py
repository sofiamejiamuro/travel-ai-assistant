from tools.weather import get_weather

def evaluate_itinerary(origin, destination, preferences, itinerary_text):
    score = 0
    max_score = 4
    details = []

    # 1. Route feasibility: must have at least 1 intermediate stop
    stops = [line for line in itinerary_text.splitlines() if "Stop" in line]
    if len(stops) >= 1:
        details.append("✅ Route has multiple stops.")
        score += 1
    else:
        details.append("❌ Route does not have multiple stops.")

    # 2. POIs must be specific
    if "Generic tourist site" not in itinerary_text:
        details.append("✅ POIs are present for each stop.")
        score += 1
    else:
        details.append("❌ One or more stops lack specific POIs.")

    # 3. Weather available
    has_weather_data = True
    for line in itinerary_text.splitlines():
        if "POIs:" in line:
            city = line.split(":")[0].replace("Start in", "").replace("Stop", "").replace("Arrive in", "").strip()
            weather = get_weather(city)
            if "unavailable" in weather.lower() or "error" in weather.lower():
                has_weather_data = False
                break
    if has_weather_data:
        details.append("✅ Weather data available for all stops.")
        score += 1
    else:
        details.append("❌ Weather unavailable for one or more stops.")

    # 4. Constraint matching
    if all(term.strip().lower() in itinerary_text.lower() for term in preferences.split(",")):
        details.append("✅ Preferences are reflected in the itinerary.")
        score += 1
    else:
        details.append("❌ Preferences not matched.")

    return {"score": score, "max_score": max_score, "details": details}

# Test cases
test_cases = [
    
    {
        "name": "All Pass",
        "origin": "Frankfurt",
        "destination": "Rome",
        "preferences": "avoid bad weather, include cultural sites",
        "itinerary_text": """
        Start in Frankfurt – POIs: Römerberg Square
        Stop 1: Strasbourg – POIs: Petite France
        Stop 2: Lyon – POIs: Roman Theatre
        Arrive in Rome – POIs: Colosseum
        """
    },
    {
        "name": "Fail Weather",
        "origin": "Frankfurt",
        "destination": "Rome",
        "preferences": "avoid bad weather, include cultural sites",
        "itinerary_text": """
        Start in Frankfurt – POIs: Römerberg Square
        Stop 1: Strasbourg – POIs: Petite France
        Stop 2: Lyon – POIs: Roman Theatre
        Arrive in Rome – POIs: Colosseum
        """  
    },
    {
        "name": "Fail POIs",
        "origin": "Frankfurt",
        "destination": "Rome",
        "preferences": "avoid bad weather, include cultural sites",
        "itinerary_text": """
        Start in Frankfurt – POIs: Generic tourist site
        Stop 1: Strasbourg – POIs: Generic tourist site
        Arrive in Rome – POIs: Generic tourist site
        """
    },
    {
        "name": "Fail Preferences",
        "origin": "Frankfurt",
        "destination": "Rome",
        "preferences": "avoid bad weather, include cultural sites",
        "itinerary_text": """
        Start in Frankfurt – POIs: Römerberg Square
        Stop 1: Strasbourg – POIs: Petite France
        Stop 2: Lyon – POIs: Roman Theatre
        Arrive in Rome – POIs: Colosseum
        """
    },
    {
        "name": "Fail Route Feasibility",
        "origin": "Frankfurt",
        "destination": "Rome",
        "preferences": "avoid bad weather, include cultural sites",
        "itinerary_text": """
        Start in Frankfurt – POIs: Römerberg Square
        Arrive in Rome – POIs: Colosseum
        """
    },
    {
        "name" : "TEst" ,   
        "origin": "Paris",
        "destination": "Rome",
        "preferences": "scenic, include cultural sites",
        "itinerary_text": """   
        Start in Paris – POIs: Eiffel Tower, Louvre Museum
        Stop 1: Lyon – POIs: Roman Theatre
        Stop 2: Florence – POIs: Uffizi Gallery
        Arrive in Rome – POIs: Colosseum
        """
    }
]

# Run all test cases
for case in test_cases:
    result = evaluate_itinerary(case["origin"], case["destination"], case["preferences"], case["itinerary_text"])
    print(f"\n--- {case['name']} ---")
    for detail in result["details"]:
        print(detail)
    print(f"Score: {result['score']}/{result['max_score']}")
