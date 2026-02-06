# AI Operations Assistant (FastAPI + Multi‑Agent GenAI)

## 🚀 Overview
The **AI Operations Assistant** is a locally runnable, production‑style GenAI system that accepts a natural‑language task, plans execution steps, calls real third‑party APIs, and returns a structured response.

This project demonstrates **agent‑based reasoning**, **LLM orchestration**, and **real API integration** using a clean FastAPI service.

---

## 🧠 Architecture
The system follows a **multi‑agent design**:

1. **Planner Agent**
   - Uses an LLM (Gemini) to convert a user task into a strict JSON execution plan
   - Selects tools deterministically (no execution)

2. **Executor Agent**
   - Executes the planner steps in order
   - Calls real third‑party APIs
   - Handles failures per step (supports partial success)

3. **Verifier Agent**
   - Validates executor outputs
   - Separates successful results and errors
   - Produces the final API response

```text
Client → FastAPI → Planner → Executor → Verifier → Response
```

---

## 🛠️ Tools & APIs Used

- **GitHub API** (free)
  - Searches popular repositories by query

- **Open‑Meteo API** (100% free, no API key)
  - City geocoding
  - Current weather information

- **Gemini LLM**
  - Used only by Planner (and optionally Verifier)
  - Structured JSON output enforced

---

## 📁 Project Structure

```text
ai_ops_assistant/
├── agents/
│   ├── planner.py      # LLM‑based task planning
│   ├── executor.py     # Tool execution logic
│   └── verifier.py     # Output validation & formatting
│
├── tools/
│   ├── github_tool.py  # GitHub API integration
│   └── weather_tool.py # Open‑Meteo API integration
│
├── llm/
│   └── client.py       # Gemini LLM client
│
├── schemas.py          # FastAPI request/response models
├── main.py             # FastAPI entry point
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd ai_ops_assistant
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables
Create a `.env` file from `.env.example`:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

⚠️ Open‑Meteo does **not** require an API key.

---

## ▶️ Running the Application

```bash
uvicorn main:app --reload
```

The API will be available at:
- **Base URL:** `http://127.0.0.1:8000`
- **Swagger UI:** `http://127.0.0.1:8000/docs`

---

## 📡 API Usage

### Endpoint
`POST /task`

### Request Body
```json
{
  "task": "Find popular GenAI GitHub repositories and tell me the weather in Bangalore"
}
```

### Example Response
```json
{
  "status": "success",
  "results": [
    {
      "tool": "github_search",
      "result": [
        {
          "name": "awesome-generative-ai",
          "stars": 12000,
          "url": "https://github.com/...",
          "description": "Curated GenAI resources"
        }
      ],
      "error": null
    },
    {
      "tool": "weather",
      "result": {
        "city": "Bangalore",
        "temperature_c": 28.4,
        "windspeed_kmh": 7.1
      },
      "error": null
    }
  ],
  "errors": []
}
```

---

## ✅ Key Design Decisions

- **Agent separation** ensures clean reasoning vs execution
- **Strict JSON planning** avoids monolithic prompts
- **Free APIs only** guarantee evaluator reliability
- **FastAPI + Pydantic** provide type‑safe, self‑documenting APIs
- **Retry + caching** improve external API robustness

---

## 📊 Evaluation Criteria Coverage

| Requirement | Status |
|------------|--------|
| Multi‑agent architecture | ✅ |
| LLM‑powered reasoning | ✅ |
| ≥ 2 real API integrations | ✅ |
| Local runnable demo | ✅ |
| Clean code & structure | ✅ |
| Documentation | ✅ |

---

## 🚧 Future Improvements

- Parallel tool execution
- Response caching layer
- Cost & latency tracking
- Authentication & rate limiting
- UI frontend

---

## 👤 Author
**Rudriya Bansal**  
B.Tech CSE | GenAI & Backend Engineering Enthusiast

---

## 🏁 Final Note
This project is designed to reflect **real‑world AI system design**, not just a demo. It emphasizes clarity, reliability, and production‑ready thinking.

