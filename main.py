from dotenv import load_dotenv
from typing import Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from typing_extensions import TypedDict

load_dotenv()

# Initialize the LLM
llm = init_chat_model(
    "openai:gpt-4"
)

# Step 1: Define State
class State(TypedDict):
    messages: Annotated[list, add_messages]
    message_type: str | None


# Step 2: Initialize StateGraph
graph_builder = StateGraph(State)


# Define chatbot function
def chatbot(state:State):
    return {"messages":[llm.invoke(state["messages"])]}


# Add nodes and edges
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START,"chatbot")
graph_builder.add_edge("chatbot",END)


# Compile the graph
graph = graph_builder.compile()

# Gathering information
user_input= input("Where are you planning to go?: ")

state = graph.invoke({"messages": [{"role": "user","content": user_input}]})

print(state["messages"][-1].content)

