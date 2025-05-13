# Travel AI Assistant

A modular, agent-powered travel planner built with LangGraph and LangChain, integrating real-time APIs (OpenWeatherMap) and prompt engineering strategies to deliver personalized trip plans.

---

## 🧭 Overview

This project simulates a next-generation AI-assisted travel guide. It enables tourists to dynamically plan and adjust their itineraries based on preferences like weather, budget, route type, and cultural points of interest. Built as part of a technical assessment, the solution focuses on:

* ✅ Multi-agent collaboration
* ✅ Prompt engineering strategies
* ✅ Real-time API integration
* ✅ Modular, testable code
* ✅ Heuristic-based evaluation

---

## 🧱 Architecture

### 🧠 Agent Design (LangGraph MCP-style)

* **Planner Agent**: Builds an initial itinerary based on user input and selected prompt mode (e.g., scenic, fastest, weather-aware).
* **Optimizer Agent**: Refines the route by applying constraints like weather, POIs, or user preferences.
* **Reporter Agent**: Generates a conversational summary of the final plan.

Agents communicate via a shared state graph, allowing for flexible transitions and easy debugging.

### 🧰 Tools & Mock APIs

* `tools/weather.py`: Fetches weather data using OpenWeatherMap API.
* `tools/pois.py`: Simulates POI lookup per city.
* `tools/routes.py`: Generates mock routes between cities.
* `tools/search.py`: Placeholder for future search integration.

### 📜 Prompt Design

System prompts are stored in `/prompts/` and include:

* `scenic.txt`
* `fastest.txt`
* `weather.txt`

Each prompt adjusts the assistant's tone and planning strategy.

###  🧠 Rationale

These prompts vary across three dimensions:

* Tone (warm vs. efficient)
* Goal (scenic vs. fast vs. safe)
* Constraints (avoid bad weather, prioritize comfort or cultural depth)

This allows us to:

* Test response quality and tone adaptability
* Evaluate how well different prompts satisfy user intent
* Support future multi-turn adaptation

Prompt loading is dynamic based on the user's trip type (selected via input).

---

## ✅ Evaluation Logic

Implemented in `evaluate.py`, the assistant's output is scored across four criteria:

1. **Route Feasibility**: Ensures the itinerary includes more than one stop.
2. **POI Inclusion**: Checks for the presence of points of interest in the itinerary.
3. **Weather Availability**: Verifies that weather data is available for all stops.
4. **Preference Satisfaction**: Assesses whether the itinerary reflects user preferences.

Each criterion adds one point to the total score, with a maximum of 4. Detailed feedback is appended to the final report.

---

## 🚀 Run the App

### 1. Clone the Repository

```bash
git clone https://github.com/sofiamejiamuro/travel-ai-assistant.git
cd travel-ai-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory and add your OpenWeatherMap API key:

```bash
OPENAI_API_KEY=your_api_key_here
OPENWEATHER_API_KEY=your_api_key_here
SERPAPI_API_KEY=your_api_key_here
```

### 4. Run the Assistant

```bash
python main.py
```

Follow the prompts to input your travel preferences and receive a personalized itinerary.

---

## 🧪 Testing

### Weather Function Test

To test the weather function independently:

```bash
python weather_test.py
```

This script will fetch weather data for a predefined list of cities to ensure the API integration works correctly.

---

## 📂 Project Structure

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
│   ├── pois.py 
|   ├── llm_factory.py
│   ├── pois.py
│   ├── routes.py
│   ├── search.py
|   └── weather.py
├── evaluate.py
├── evaluate_cases.py
├── main.py
├── weather_test.py
├── requirements.txt
└── README.md
```

---

## 📝 Future

* **Real API Integration**: Replace mock POI and route data with real-time data from services like Google Places and Mapbox.
* **Enhanced Evaluation**: Incorporate LLM-based evaluation for more nuanced assessment of itinerary quality.

---

🙌 Notes

This was completed under a strict time constraint. The solution reflects scalable thinking, modular structure, and production-oriented architecture despite being a prototype.

> Built with ❤️ and lots of ☕ by Sof