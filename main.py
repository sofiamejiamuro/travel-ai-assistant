from dotenv import load_dotenv
from typing import Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from typing_extensions import TypedDict
from agents.planner import planner_fn
from agents.optimizer import optimizer_fn
from agents.reporter import reporter_fn

load_dotenv()

# Initialize the LLM
llm = init_chat_model(
    "openai:gpt-4"
)

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
graph_builder.add_node("planner", planner_fn)
graph_builder.add_node("optimizer", optimizer_fn)
graph_builder.add_node("reporter", reporter_fn)

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