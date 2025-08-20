from fastapi import FastAPI, HTTPException
from uuid import UUID
from app.models import Task, TaskUpdate, TaskStatus
from app.database import db

app = FastAPI(title="Task Manager API")

@app.get("/tasks", response_model=list[Task])
def get_tasks(status: TaskStatus | None = None):
    tasks = db.get_tasks()
    if status:
        return [t for t in tasks if t.status == status]
    return tasks

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: Task):
    return db.create_task(task)

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: UUID):
    if task := db.get_task(task_id):
        return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: UUID, task_update: TaskUpdate):
    if updated_task := db.update_task(task_id, task_update):
        return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: UUID):
    if not db.delete_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
