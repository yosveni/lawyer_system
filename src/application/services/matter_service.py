from ...domain.repositories.matter_repository import MatterRepository
from ...application.dtos.matter_dto import MatterCreate, MatterResponse

class MatterService:
    def __init__(self, repo: MatterRepository):
        self.repo = repo

    def create_matter(self, matter: MatterCreate, tenant_id: str) -> MatterResponse:
        db_matter = self.repo.create_matter(matter, tenant_id)
        return MatterResponse(**db_matter.__dict__)