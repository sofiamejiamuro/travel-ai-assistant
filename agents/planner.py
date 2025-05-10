from tools.routes import get_mock_route
from tools.pois import get_mock_pois
from tools.search import search_travel_info

def planner_fn(state, llm=None):
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

     # Optional: Use the LLM to describe the route
    if llm:
        user_prompt = f"Create a short paragraph introducing a {preferences} road trip from {origin} to {destination}, including notable places like {', '.join(route)}."
        try:
            ai_summary = llm.invoke({"input": user_prompt}).content
        except:
            ai_summary = "No LLM summary available."
    else:
        ai_summary = "LLM was not provided."

    return {
        "itinerary": itinerary,
        "planner_notes": f"Planned based on {preferences}",
        "search_summary": search_summary
    }
