import bcrypt
from datetime import datetime, timedelta
from jose import jwt

class UserService:
    encoding: str = "UTF-8"
    secret_key: str = "65e759cc2e7d75d44c1ffa263bbee80f7974a7e3aadb9695b29a3a61a999726f"
    jwt_algorithm:str = "HS256"

    def hash_password(self, plain_password: str) -> str:
        hashed_password: bytes = bcrypt.hashpw(
            plain_password.encode(self.encoding),
            salt=bcrypt.gensalt(),
        )
        return hashed_password.decode(self.encoding)


    def verify_password(
        self, plain_password: str, hashed_password: str
    ) -> bool:
        return bcrypt.checkpw(
            plain_password.encode(self.encoding),
            hashed_password.encode(self.encoding)
        )


    def create_jwt(self, username: str) -> str:
        return jwt.encode(
            {
                "sub": username,
                "exp": datetime.now() + timedelta(days=1),
            },
            self.secret_key,
            algorithm=self.jwt_algorithm,
        )
