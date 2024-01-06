from pydantic import BaseModel, EmailStr


class SignUpRequest(BaseModel):
    username: str
    password: str


class LogInRequest(BaseModel):
    username: str
    password: str


class CreateOTPRequest(BaseModel):
    email: EmailStr


class VerifyOTPRequest(BaseModel):
    email: EmailStr
    otp: int
