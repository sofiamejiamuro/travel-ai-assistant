from tools.weather import get_weather

def optimizer_fn(state):
    itinerary_lines = state.get("itinerary", "").split("\\n")
    optimized = []

    for line in itinerary_lines:
        stop = line.split(" - ")[0]
        weather = get_weather(stop)
        if "rain" not in weather.lower():
            optimized.append(f"{line} (Weather: {weather})")

    return {
        "optimized_itinerary": "\\n".join(optimized),
        "optimizer_notes": "Filtered out rainy stops"
    }
