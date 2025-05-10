from tools.routes import get_mock_route
from tools.pois import get_mock_pois
from tools.search import search_travel_info

def planner_fn(state):
    origin = state["origin"]
    destination = state["destination"]
    preferences = state.get("preferences", "scenic route")

    route = get_mock_route(origin, destination)
    pois = {stop: get_mock_pois(stop) for stop in route}

    try:
        search_summary = search_travel_info(f"scenic route between {origin} and {destination}")
    except:
        search_summary = "No search data available."

    itinerary = "\\n".join([
        f"{stop} - POIs: {', '.join(pois.get(stop, []))}" for stop in route
    ])

    return {
        "itinerary": itinerary,
        "planner_notes": f"Planned based on {preferences}",
        "search_summary": search_summary
    }
