from ...domain.repositories.activity_repository import ActivityRepository
from ...application.dtos.activity_dto import ActivityCreate, ActivityResponse

class ActivityService:
    def __init__(self, repo: ActivityRepository):
        self.repo = repo

    def create_activity(self, activity: ActivityCreate, tenant_id: str) -> ActivityResponse:
        db_activity = self.repo.create_activity(activity, tenant_id)
        return ActivityResponse(**db_activity.__dict__)