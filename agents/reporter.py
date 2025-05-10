from tools.budget import estimate_trip_cost

def reporter_fn(state, llm):
    itinerary = state.get("optimized_itinerary", "")
    stops = itinerary.split("\\n")
    cost = estimate_trip_cost(len(stops))
    itinerary = itinerary.replace("\\n", "\n")

    summary = llm.invoke([
        {
            "role": "system",
            "content": "You are a friendly travel agent helping users plan scenic and insightful trips."
        },
        {
            "role": "user",
            "content": f"""Create a conversational travel summary for the user based on:
- Itinerary: {state['optimized_itinerary']}
- Trip preferences: {state['preferences']}
- Cost: {cost}
- Weather at each stop: {state.get('weather_notes', 'Not available')}
"""
        }
    ])

    return {
        "final_message": summary.content
    }
