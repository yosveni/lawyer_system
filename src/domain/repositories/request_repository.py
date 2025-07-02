from sqlalchemy.orm import Session
from ..models.request import Request
from ...application.dtos.request_dto import RequestCreate

class RequestRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_request(self, request: RequestCreate, tenant_id: str) -> Request:
        db_request = Request(**request.dict(), tenant_id=tenant_id)
        self.db.add(db_request)
        self.db.commit()
        self.db.refresh(db_request)
        return db_request