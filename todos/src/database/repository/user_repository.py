from database.connection import get_db
from database.orm.user_orm import User
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session


    def get_user_by_username(self, username: str) -> User | None:
        return self.session.scalar(
            select(User).where(User.username == username)
        )


    def save_user(self, user: User) -> User:
        self.session.add(instance=user)
        self.session.commit()  # db save
        self.session.refresh(instance=user)
        return user
