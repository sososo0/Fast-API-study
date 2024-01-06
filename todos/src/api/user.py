from fastapi import APIRouter, Depends, HTTPException

from schema.request import SignUpRequest, LogInRequest, CreateOTPRequest
from schema.response import UserSchema, JWTResponse
from service.user import UserService
from database.repository import UserRepository
from database.orm import User

from security import get_access_token

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


@router.post("/log-in")
def user_log_in_handler(
    request: LogInRequest,
    user_service: UserService = Depends(),
    user_repo: UserRepository = Depends(),
):
    user: User | None = user_repo.get_user_by_username(
        username=request.username
    )
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")

    verified: bool = user_service.verify_password(
        plain_password=request.password,
        hashed_password=user.password,
    )
    if not verified:
        raise HTTPException(status_code=401, detail="Not Authorized")

    access_toekn: str = user_service.create_jwt(username=user.username)
    return JWTResponse(access_toekn=access_toekn)


@router.post("/email/otp")
def create_otp_handler(
    request: CreateOTPRequest,
    access_token: str = Depends(get_access_token),
    user_service: UserService = Depends(),
):
    # 1. access_token
    # 2. request body(email)
    # 3. otp create(random 4 digit)
    otp: int = user_service.create_otp()

    # 4. redis otp(email, 1234, exp=3min)
    # 5. send otp to email
    return


@router.post("/email/otp/verify")
def create_otp_handler():
    return
