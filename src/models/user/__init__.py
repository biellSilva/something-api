from datetime import date

from pydantic import EmailStr, Field
from src.enums import UserRoleEnum

from src.models.base import EntityBase


class User(EntityBase):
    role: UserRoleEnum = Field(description="User role")

    name: str = Field(description="User name")
    lastname: str = Field(description="User lastname")

    email: EmailStr = Field(
        description="User email", examples=["user@email.com.br", "user@email.com"]
    )
    password: str = Field(description="User hashed password")

    image: str | None = Field(default=None, description="User profile picture")
    birthdate: date | None = Field(default=None, description="User birthdate")

    @classmethod
    def get_tablename(cls) -> str:
        return "users"


class UserWithToken(User):
    token: str = ""
