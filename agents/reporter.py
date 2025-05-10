def reporter_fn(state):
    optimized = state.get("optimized_itinerary", "")
    
    final_message = f"Here's your updated travel plan: {optimized}. Enjoy your trip!"
    
    return {
        "final_message": final_message
    }
