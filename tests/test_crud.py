from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_item():
    data = {
        "title": "pytest",
        "description": "test with pytest",
        "status": "created",
    }
    response = client.post("/tasks/", json=data)
    assert response.status_code == 201
    result = response.json()
    assert result["title"] == data["title"]
    assert result["description"] == data["description"]
    assert result["status"] == data["status"]
    assert "id" in result


def test_get_item():
    data = {
        "title": "first task",
        "description": "hello!",
        "status": "in progress",
    }
    response = client.post("/tasks/", json=data)
    task_id = response.json()["id"]
    # проверяем наличие объекта
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 200
    result = get_response.json()
    assert result["title"] == data["title"]
    assert result["description"] == data["description"]


def test_get_list_items():
    response = client.get("/tasks/")
    assert response.status_code == 200
    result = response.json()
    assert isinstance(result, list)


def test_change_status():
    data = {"title": "task", "description": "desc", "status": "created"}
    response = client.post("/tasks/", json=data)
    task_id = response.json()["id"]
    # проверяем статус
    patch_response = client.patch(
        f"/tasks/{task_id}", json={"status": "in process"},
    )
    assert patch_response.status_code == 200
    result = patch_response.json()
    assert result["status"] == "in process"


def test_delete():
    data = {
        "title": "pytest",
        "description": "test with pytest",
        "status": "created",
    }
    response = client.post("/tasks/", json=data)
    assert response.status_code == 201
    task_id = response.json()["id"]
    # удаляем
    del_response = client.delete(f"/tasks/{task_id}")
    assert del_response.status_code == 204
    # проверяем удаление
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404
