from pydantic import BaseModel
from datetime import datetime

class TaskCreate(BaseModel):
    description: str
    due_date: datetime

class TaskResponse(BaseModel):
    id: str
    description: str
    due_date: datetime
    tenant_id: str