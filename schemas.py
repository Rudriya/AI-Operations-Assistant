from pydantic import BaseModel
from typing import List, Optional, Any


# ---------- Request Schema ----------

class TaskRequest(BaseModel):
    task: str


# ---------- Tool Result Schemas ----------

class ToolResult(BaseModel):
    tool: str
    result: Optional[Any] = None
    error: Optional[str] = None


# ---------- Final Response Schema ----------

class TaskResponse(BaseModel):
    status: str
    results: List[ToolResult]
    errors: List[ToolResult]