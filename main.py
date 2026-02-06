from fastapi import FastAPI

app = FastAPI(title="AI Operations Assistant")


from fastapi import FastAPI, HTTPException
from agents.planner import planner_agent
from agents.executor import executor_agent
from agents.verifier import verifier_agent
from schemas import TaskRequest, TaskResponse

app = FastAPI(title="AI Operations Assistant")


@app.post("/task", response_model=TaskResponse)
def run_task(payload: TaskRequest):
    try:
        plan = planner_agent(payload.task)
        executor_results = executor_agent(plan)
        final_response = verifier_agent(executor_results)
        return final_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))   


@app.get("/")
def health_check():
    return {"status": "ok"}