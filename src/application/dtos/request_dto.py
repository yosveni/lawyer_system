from pydantic import BaseModel

class RequestCreate(BaseModel):
    description: str
    status: str

class RequestResponse(BaseModel):
    id: str
    description: str
    status: str
    tenant_id: str