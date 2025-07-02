from ...domain.repositories.schedule_repository import ScheduleRepository
from ...application.dtos.schedule_dto import ScheduleCreate, ScheduleResponse

class ScheduleService:
    def __init__(self, repo: ScheduleRepository):
        self.repo = repo

    def create_schedule(self, schedule: ScheduleCreate, tenant_id: str) -> ScheduleResponse:
        db_schedule = self.repo.create_schedule(schedule, tenant_id)
        return ScheduleResponse(**db_schedule.__dict__)