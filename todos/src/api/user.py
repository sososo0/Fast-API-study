from fastapi import APIRouter, Depends

from schema.request import SignUpRequeest
from schema.response import UserSchema
from service.user import UserService
from database.repository import UserRepository
from database.orm import User

router = APIRouter(prefix="/users")


@router.post("/sign-up", status_code=201)
def user_sign_up_handler(
    request: SignupRequest,
    user_service: UserService = Depends(),
    user_repo: UserRepository = Depends(),
):
    hashed_password: str = user_service.hash_password(
        plain_password=request.password
    )
    user: User = UserService.create(
        username=request.username,
        hashed_password =request.hashed_password
    )
    user: User = user_repo.save_user(user=user) # id=int
    return UserSchema.from_orm(user)
