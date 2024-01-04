from pydantic import BaseModel


class CreateToDoRequest(BaseModel):
    contents: str
    is_done: bool


class SignUpRequeest(BaseModel):
    username: str
    password: str
