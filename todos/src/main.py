from fastapi import FastAPI, Body, HTTPException, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from database.repository import get_todos
from database.repository import get_todo_by_todo_id
from database.repository import create_todo
from database.repository import update_todo
from database.orm import ToDo
from schema.response import ToDoSchema
from schema.response import ListToDoResponse
from schema.request import CreateToDoRequest

app = FastAPI()


@app.get("/")
def health_check_handler():
    return {"ping": "pong"}


todo_data = {
    1: {
        "id": 1,
        "contents": "실전! FastAPI 섹션 0 수강",
        "is_done": True
    },
    2: {
        "id": 2,
        "contents": "실전! FastAPI 섹션 1 수강",
        "is_done": False
    },
    3: {
        "id": 3,
        "contents": "실전! FastAPI 섹션 2 수강",
        "is_done": False
    }
}


@app.get("/todos", status_code=200)
def get_todos_handler(
    order: str | None = None,
    session: Session = Depends(get_db),
) -> ListToDoResponse:
    todos: List[ToDo] = get_todos(session=session)
    if order and order == "DESC":
        return ListToDoResponse(
            todos = [ToDoSchema.from_orm(todo) for todo in todos[::-1]]
        )
    return ListToDoResponse(
        todos = [ToDoSchema.from_orm(todo) for todo in todos]
    )


@app.get("/todos/{todo_id}", status_code=200)
def get_todo_handler(
    todo_id: int,
    session: Session = Depends(get_db),
) -> ToDoSchema:
    todo: ToDo | None = get_todo_by_todo_id(session=session, todo_id=todo_id)
    if todo:
        return ToDoSchema.from_orm(todo)
    raise HTTPException(status_code=404, detail="ToDo Not Found")


@app.post("/todos", status_code=201)
def create_todo_handler(
    request: CreateToDoRequest,
    session: Session = Depends(get_db),
) -> ToDoSchema:
    todo: ToDo = ToDo.create(request=request) # id = None
    todo: ToDo = create_todo(session=session, todo=todo) # id = int
    return ToDoSchema.from_orm(todo)


@app.patch("/todos/{todo_id}", status_code=200)
def update_todo_handler(
    todo_id: int,
    is_done: bool = Body(..., embed=True),
    session: Session = Depends(get_db),
) -> ToDoSchema:
    todo: ToDo | None = get_todo_by_todo_id(session=session, todo_id=todo_id)
    if todo:
        todo.done() if is_done else todo.undone()
        todo: ToDo = update_todo(session=session, todo=todo)
        return ToDoSchema.from_orm(todo)
    raise HTTPException(status_code=404, detail="ToDo Not Found")


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo_handler(todo_id: int):
    todo = todo_data.pop(todo_id, None)
    if todo:
        return
    raise HTTPException(status_code=404, detail="ToDo Not Found")
