from uuid import UUID
from app.models import Task, TaskStatus

class Database:
    def __init__(self):
        self.tasks: dict[UUID, Task] = {}

    def get_tasks(self) -> list[Task]:
        return list(self.tasks.values())

    def get_task(self, task_id: UUID) -> Task | None:
        return self.tasks.get(task_id)

    def create_task(self, task: Task) -> Task:
        self.tasks[task.id] = task
        return task

    def update_task(self, task_id: UUID, task_update: TaskUpdate) -> Task | None:
        if task := self.tasks.get(task_id):
            update_data = task_update.dict(exclude_unset=True)
            updated_task = task.copy(update=update_data)
            self.tasks[task_id] = updated_task
            return updated_task

    def delete_task(self, task_id: UUID) -> bool:
        return bool(self.tasks.pop(task_id, None))

db = Database()
