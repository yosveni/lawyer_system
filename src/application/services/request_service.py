from ...domain.repositories.request_repository import RequestRepository
from ...application.dtos.request_dto import RequestCreate, RequestResponse

class RequestService:
    def __init__(self, repo: RequestRepository):
        self.repo = repo

    def create_request(self, request: RequestCreate, tenant_id: str) -> RequestResponse:
        db_request = self.repo.create_request(request, tenant_id)
        return RequestResponse(**db_request.__dict__)