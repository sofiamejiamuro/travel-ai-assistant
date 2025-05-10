from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from typing_extensions import TypedDict
from agents.planner import planner_fn
from agents.optimizer import optimizer_fn
from agents.reporter import reporter_fn
from tools.llm_factory import init_llm_with_prompt

load_dotenv()

# Initialize the LLM
travel_mode = input("What kind of trip do you want? (scenic / fastest / weather): ")
llm = init_llm_with_prompt(travel_mode.strip().lower())

# Step 1: Define State
class TravelState(TypedDict):
    origin: str
    destination: str
    preferences: str
    itinerary: str
    optimized_itinerary: str
    final_message: str
    planner_notes: str
    optimizer_notes: str

# Step 2: Initialize LangGraph
graph_builder = StateGraph(TravelState)

# Step 3: Add nodes (agent functions)
graph_builder.add_node("planner", lambda state: planner_fn(state, llm=llm))
graph_builder.add_node("optimizer", optimizer_fn)
graph_builder.add_node("reporter", lambda state: reporter_fn(state, llm))


# Step 4: Define edges (agent collaboration)
graph_builder.set_entry_point("planner")
graph_builder.add_edge("planner", "optimizer")
graph_builder.add_edge("optimizer", "reporter")
graph_builder.add_edge("reporter", END)

# Step 5: Compile the graph
graph = graph_builder.compile()

# Step 6: Gather user input
origin = input("Enter your origin city: ")
destination = input("Enter your destination city: ")
preferences = input("Any travel preferences? (e.g. scenic, short, avoid weather): ")

initial_state = {
    "origin": origin,
    "destination": destination,
    "preferences": preferences,
    "itinerary": "",
    "optimized_itinerary": "",
    "final_message": "",
    "planner_notes": "",
    "optimizer_notes": ""
}

# Step 7: Run the graph
output = graph.invoke(initial_state)

# Step 8: Show final result
print("\n🧳 Final Travel Plan:")
print(output["final_message"])