from pydantic import BaseModel, EmailStr

class ContactCreate(BaseModel):
    name: str
    email: EmailStr

class ContactResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    tenant_id: str