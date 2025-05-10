import os
from dotenv import load_dotenv
from langchain_community.utilities import SerpAPIWrapper

load_dotenv()
search_tool = SerpAPIWrapper()

def search_travel_info(query: str) -> str:
    return search_tool.run(query)