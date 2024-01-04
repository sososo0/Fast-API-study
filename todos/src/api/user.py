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
    # 1. request body로 username과 password 받기 - 우선은 중복체크는 하지 않을 거임
    # 2. password를 hashing을 통해 암호화하기 - hashed_password를 통해 암호화하기
    hashed_password: str = user_service.hash_password(
        plain_password=request.password
    )

    # 3. User(username, hashed_password)를 통해 User 생성
    user: User = UserService.create(
        username=request.username,
        hashed_password =request.hashed_password
    )

    # 4. 생성해준 User를 db에 저장
    user: User = user_repo.save_user(user=user) # id=int

    # 5. user response를 응답해주기 - return user(id, username)
    return UserSchema.from_orm(user)
