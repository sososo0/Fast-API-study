from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class JWTResponse(BaseModel):
    access_toekn: str
