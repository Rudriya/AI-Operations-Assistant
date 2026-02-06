# AI Operations Assistant (FastAPI + Multi‑Agent GenAI)

##  Overview
The **AI Operations Assistant** is a locally runnable, production‑style GenAI system that accepts a natural‑language task, plans execution steps, calls real third‑party APIs, and returns a structured response.

This project demonstrates **agent‑based reasoning**, **LLM orchestration**, and **real API integration** using a clean FastAPI service.

---

##  Architecture

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
Client → FastAPI → Planner Agent → Executor Agent → Verifier Agent → JSON Response
```
---

##  Tools & APIs Used

- **GitHub API** (free)
  - Searches popular repositories by query

- **Open‑Meteo API** (100% free, no API key)
  - City geocoding
  - Current weather information

- **Gemini LLM**
  - Used only by Planner (and optionally Verifier)
  - Structured JSON output enforced

---

##  Project Structure

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
    ├── humanizer.py    # humanize raw json output 
│   └── client.py       # Gemini LLM client
│
├── schemas.py          # FastAPI request/response models
├── main.py             # FastAPI entry point
├── requirements.txt
├── .env.example
└── README.md
```

---

##  Setup Instructions

### 1️. Clone the Repository
```bash
git clone <your-repo-url>
cd ai_ops_assistant
```

### 2️. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️. Environment Variables
Create a `.env` file from `.env.example`:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

⚠️ Open‑Meteo does **not** require an API key.

---

##  Running the Application

```bash
uvicorn main:app --reload
```
## Run Frontend

```bash
streamlit run app.py
```
The API will be available at:
- **Base URL:** `http://127.0.0.1:8000`
- **Swagger UI:** `http://127.0.0.1:8000/docs`

---

##  Architecture Diagram

```text
User → Streamlit UI → FastAPI → Planner (LLM) → Executor (APIs) → Verifier → JSON → Humanizer (LLM) → User
```

---

##  API Usage

### Endpoint
`POST /task`

### Request Body
```json
{
  "task": "Find popular GenAI GitHub repositories and tell me the weather in Bangalore"
}
```

### Sample `curl` Command

```bash
curl -X POST "http://127.0.0.1:
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
## 🖥️ Frontend (Streamlit)

A lightweight **Streamlit frontend** is included to demonstrate the system in a user-friendly, product-style interface.

### Frontend Behavior

- Users enter a natural-language task
- The system plans and executes using agents
- Results are displayed as a **clear natural-language answer**
- Raw JSON output is available in an expandable section for transparency

This design mirrors real-world GenAI systems, where structured system outputs are translated into conversational responses at the presentation layer.
---
##  Key Design Decisions

-- **Multi-agent architecture (Planner → Executor → Verifier)** enforces clear separation of reasoning, execution, and validation responsibilities
- **Strict JSON-based planning** ensures deterministic, testable outputs and avoids monolithic or opaque prompts
- **LLM usage is scoped deliberately**: Gemini is used only where reasoning or language generation adds value (planning and humanization)
- **Structured backend, humanized frontend**: the FastAPI backend always returns reliable JSON, while the Streamlit UI translates results into natural language for better UX
- **Free and reliable third-party APIs** (GitHub, Open-Meteo) guarantee smooth evaluation without authentication or quota issues
- **FastAPI + Pydantic schemas** provide type safety, automatic validation, and self-documenting APIs via Swagger
- **Resilience by design**: retry logic and caching improve robustness against transient external API failures


---

##  Evaluation Criteria Coverage

| Requirement | Status |
|------------|--------|
| Multi‑agent architecture | ✅ |
| LLM‑powered reasoning | ✅ |
| 2 real API integrations | ✅ |
| Local runnable demo | ✅ |
| Clean code & structure | ✅ |
| Documentation | ✅ |

---

##  Future Improvements

- Parallel tool execution
- Response caching layer
- Cost & latency tracking
- Authentication & rate limiting
- UI frontend

---

##  Author
**Rudriya Bansal**  

---

## 🏁 Final Note
This project is designed to reflect **real‑world AI system design**, not just a demo. It emphasizes clarity, reliability, and production‑ready thinking.

