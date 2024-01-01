from database.orm import ToDo


def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}


def test_get_todos(client, mocker):
    # order = ASC
    mocker.patch("main.get_todos", return_value=[
        ToDo(id=1, contents="FastAPI Section 0", is_done=True),
        ToDo(id=2, contents="FastAPI Section 1", is_done=False)
    ])
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == {
        "todos": [
            {"id": 1, "contents": "FastAPI Section 0", "is_done": True},
            {"id": 2, "contents": "FastAPI Section 1", "is_done": False}
        ]
    }

    # order = DESC
    response = client.get("/todos?order=DESC")
    assert response.status_code == 200
    assert response.json() == {
        "todos": [
            {"id": 2, "contents": "FastAPI Section 1", "is_done": False},
            {"id": 1, "contents": "FastAPI Section 0", "is_done": True}
        ]
    }


def test_get_todo(client, mocker):
    mocker.patch(
        "main.get_todo_by_todo_id",
        return_value=ToDo(id=1, contents="todo", is_done=True)
    )

    # 200
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "contents": "todo", "is_done": True}

    # 404
    mocker.patch(
        "main.get_todo_by_todo_id",
        return_value=None
    )

    response = client.get("/todos/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "ToDo Not Found"}
