import json
from llm.client import call_llm

SYSTEM_PROMPT = """
You are a Planner Agent.

Your job is to convert a user's task into a step-by-step execution plan.

Rules:
- You MUST output ONLY valid JSON
- DO NOT explain anything
- DO NOT add extra text
- Use ONLY the allowed tools
- Each step must include an action and input

Allowed tools:
1. github_search → for GitHub repository queries
2. weather → for weather information by city
"""

def planner_agent(user_task: str) -> dict:
    user_prompt = f"""
User task:
{user_task}

Output JSON schema:
{{
  "steps": [
    {{
      "action": "tool_name",
      "input": "string"
    }}
  ]
}}
"""

    response = call_llm(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_prompt,
        temperature=0
    )

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        raise ValueError("Planner returned invalid JSON")