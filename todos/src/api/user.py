from fastapi import APIRouter, Depends

from schema.request import SignUpRequest, LogInRequest
from schema.response import UserSchema
from service.user import UserService
from database.repository import UserRepository
from database.orm import User

router = APIRouter(prefix="/users")


@router.post("/sign-up", status_code=201)
def user_sign_up_handler(
    request: SignUpRequest,
    user_service: UserService = Depends(),
    user_repo: UserRepository = Depends(),
):
    hashed_password: str = user_service.hash_password(
        plain_password=request.password
    )
    user: User = User.create(
        username=request.username,
        hashed_password =hashed_password
    )
    user: User = user_repo.save_user(user=user) # id=int
    return UserSchema.from_orm(user)


@router.post("log-in")
def user_log_in_handler(
    request: LoginRequest,
):
    # 1. request body로 username과 password 입력 받기
    # 2. database에서 username을 통해 user를 읽는다.
    # 3. user의 password(해싱된 pw)와 입력으로 받은 request의 password(일반 pw)가 같은지 확인
    # -> bcrypt.checkpw를 통해 검증
    # 4. 유효한 user면 jwt를 생성해서 return 하기
    return True
