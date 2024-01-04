from fastapi import APIRouter

from api import todo, user

router = APIRouter(prefix="/users")
app.include_router(todo.router)
app.include_router(user.router)


@router.post("/sign-up")
def user_sign_up_handler():
    return True
