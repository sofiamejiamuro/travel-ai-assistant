from tools.budget import estimate_trip_cost

def reporter_fn(state):
    itinerary = state.get("optimized_itinerary", "")
    stops = itinerary.split("\\n")
    cost = estimate_trip_cost(len(stops))
    itinerary = itinerary.replace("\\n", "\n")

    return {
        "final_message": f"Here’s your plan:\n{itinerary}\n\nEstimated trip cost: {cost}"
    }
