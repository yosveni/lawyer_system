from pydantic import BaseModel

class MatterCreate(BaseModel):
    case_number: str
    description: str

class MatterResponse(BaseModel):
    id: str
    case_number: str
    description: str
    tenant_id: str