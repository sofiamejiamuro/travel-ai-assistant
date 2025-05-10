import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

def load_system_prompt(travel_mode: str) -> str:
    path = f"prompts/{travel_mode}.txt"
    if not os.path.exists(path):
        raise ValueError(f"Prompt for mode '{travel_mode}' not found.")
    with open(path, "r") as file:
        return file.read()

def init_llm_with_prompt(travel_mode: str = "scenic") -> ChatPromptTemplate:
    system_prompt_text = load_system_prompt(travel_mode)
    system_prompt = SystemMessagePromptTemplate.from_template(system_prompt_text)
    human_prompt = HumanMessagePromptTemplate.from_template("{input}")
    
    prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])
    llm = ChatOpenAI(model="gpt-4", temperature=0.7)

    return prompt | llm
