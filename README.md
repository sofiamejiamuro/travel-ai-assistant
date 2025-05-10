# 🧭 Travel AI Assistant

A modular, agent-powered travel planner built with LangGraph and LangChain, integrating real-time APIs (OpenWeatherMap) and prompt engineering strategies to deliver personalized trip plans.

---

## 🌍 Overview

This project simulates a next-generation AI-assisted travel guide. It enables tourists to dynamically plan and adjust their itineraries based on preferences like weather, budget, route type, and cultural points of interest. Built as part of a technical assessment, the solution focuses on:

* ✅ Multi-agent collaboration
* ✅ Prompt engineering strategies
* ✅ Real-time API integration
* ✅ Modular, testable code

---

## 🧠 Architecture

### 🧩 Agent Design (LangGraph MCP-style)

* **Planner Agent**: builds an initial itinerary based on the user's origin, destination, and preferences.
* **Optimizer Agent**: adjusts the itinerary considering constraints such as cost, weather, or duration.
* **Reporter Agent**: generates a friendly final summary in natural language using an LLM.

All agents are orchestrated using LangGraph's `StateGraph`, enabling clear state propagation and flow control.

---

## 📝 Prompt Strategy

System prompts play a crucial role in shaping agent behavior. This project includes three prompt variants tailored to common travel goals:

### 1. `scenic.txt`

**Tone**: Descriptive, enriching
**Goal**: Maximize cultural, natural, and historical exposure
**Use case**: Ideal for users who want slow, inspiring travel experiences

> "You are a thoughtful travel planner focused on crafting scenic journeys. Include stops at natural landscapes, historic towns, and cultural landmarks. Avoid highways and prioritize memorable routes."

### 2. `fastest.txt`

**Tone**: Direct, pragmatic
**Goal**: Optimize travel speed and efficiency
**Use case**: Ideal for business travelers or users on tight schedules

> "You are a highly efficient travel planner. Your goal is to minimize travel time while ensuring essential details like directions and weather are accurate. Focus on highways and direct routes."

### 3. `weather.txt`

**Tone**: Balanced, cautious
**Goal**: Maximize safety and comfort by avoiding bad weather
**Use case**: Ideal for family travel or travel during volatile seasons

> "You are a travel planner that optimizes routes for weather safety. Suggest routes that avoid rain, storms, or extreme temperatures. Prioritize stops with good weather over scenic appeal."

### 🧠 Rationale

These prompts vary across three dimensions:

* **Tone** (warm vs. efficient)
* **Goal** (scenic vs. fast vs. safe)
* **Constraints** (avoid bad weather, prioritize comfort or cultural depth)

This allows us to:

* Test **response quality and tone adaptability**
* Evaluate how well different prompts satisfy **user intent**
* Support future **multi-turn adaptation**

Prompt loading is dynamic based on the user's trip type (selected via input).

---

## 🔌 API Integrations

* **OpenWeatherMap API**: for real-time weather summaries at each stop.
* **Mocked POI and Routing APIs**: simulate cultural sites and path generation with location-specific logic (Europe vs Mexico).

---

## 🧪 Evaluation Logic *(in progress)*

A modular script will:

1. Run the graph with each prompt.
2. Score based on:

   * Itinerary structure (start, stops, destination)
   * Constraint match (weather, cost, duration)
   * LLM-based critique on tone & helpfulness

---

## ✅ Testing Plan *(in progress)*

* Unit tests for each agent (`planner`, `optimizer`, `reporter`)
* Mocked API test cases
* Prompt-based behavior comparison tests

---

## 🚀 Run the App

```bash
# Set up environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Add your .env with:
OPENAI_API_KEY=your_key_here
OPENWEATHERMAP_API_KEY=your_key_here
SERPAPI_API_KE=your_key_here

# Run the app
python main.py
```

---

## 📁 Folder Structure

```
├── agents/
│   ├── optimizer.py
│   ├── planner.py
│   └── reporter.py
├── prompts/
│   ├── fastest.txt
│   ├── scenic.txt
│   └── weather.txt
├── tools/
│   ├── budget.py
│   ├── llm_factory.py
│   ├── pois.py
│   ├── routes.py
│   ├── search.py
│   └── weather.py
├── main.py
└── README.md
```

---

## ✨ Next Steps

* [ ] Add evaluation runner script
* [ ] Finalize test coverage
* [ ] Expand to support cultural preferences
* [ ] Optional: Add Streamlit UI for demo

---

## 🙌 Notes

This was completed under a strict time constraint. The solution reflects scalable thinking, modular structure, and production-oriented architecture despite being a prototype.

> Built with ❤️ by Sof
