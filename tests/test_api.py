import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Task, TaskStatus

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={
        "title": "Test Task",
        "description": "Test Description"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["status"] == "created"

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_task():
    create_resp = client.post("/tasks", json={"title": "Sample", "description": ""})
    task_id = create_resp.json()["id"]
    
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id

def test_update_task():
    create_resp = client.post("/tasks", json={"title": "Old", "description": ""})
    task_id = create_resp.json()["id"]
    
    update_resp = client.put(f"/tasks/{task_id}", json={
        "title": "New Title",
        "status": "in_progress"
    })
    assert update_resp.status_code == 200
    assert update_resp.json()["title"] == "New Title"
    assert update_resp.json()["status"] == "in_progress"

def test_delete_task():
    create_resp = client.post("/tasks", json={"title": "To delete", "description": ""})
    task_id = create_resp.json()["id"]
    
    delete_resp = client.delete(f"/tasks/{task_id}")
    assert delete_resp.status_code == 200
    
    get_resp = client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 404
