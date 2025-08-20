from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from enum import Enum

class TaskStatus(str, Enum):
    CREATED = "created"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: str
    status: TaskStatus = TaskStatus.CREATED

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None
