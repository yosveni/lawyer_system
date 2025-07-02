from ...domain.repositories.task_repository import TaskRepository
from ...application.dtos.task_dto import TaskCreate, TaskResponse

class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def create_task(self, task: TaskCreate, tenant_id: str) -> TaskResponse:
        db_task = self.repo.create_task(task, tenant_id)
        return TaskResponse(**db_task.__dict__)