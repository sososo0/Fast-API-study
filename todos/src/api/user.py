from fastapi import APIRouter

router = APIRouter(prefix="/users")


@router.post("/sign-up")
def user_sign_up_handler():
    return True
