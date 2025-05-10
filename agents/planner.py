def planner_fn(state):
    origin = state.get("origin")
    destination = state.get("destination")
    preferences = state.get("preferences", "scenic route")
    
    # Simulate basic itinerary creation
    itinerary = f"Start in {origin}, take scenic route to {destination}, stopping at historical landmarks."
    
    return {
        "itinerary": itinerary,
        "planner_notes": f"Planned based on preferences: {preferences}"
    }
