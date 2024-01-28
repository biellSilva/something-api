__all__ = ("SignIn", "SignUp")

import re
from datetime import date, datetime, timedelta
from typing import Annotated

from pydantic import BaseModel, BeforeValidator, Field, field_validator
from pytz import timezone
from src.domain import config

from src.domain.errors.auth import WrongEmailFormat, WrongPasswordFormat
from src.enums import UserRoleEnum


class SignIn(BaseModel):
    email: Annotated[str, BeforeValidator(lambda x: str(x).strip())] = Field(
        examples=["user@email.com.br", "user@email.com"], description="User email"
    )
    password: Annotated[str, BeforeValidator(lambda x: str(x).strip())] = Field(
        description="User password"
    )

    @field_validator("email")
    @classmethod
    def email_validator(cls, value: str):
        if re.match(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", value
        ):
            return value

        raise WrongEmailFormat

    @field_validator("password")
    @classmethod
    def password_validator(cls, value: str):
        has_upper = any(letter.isupper() for letter in value)
        has_lower = any(letter.islower() for letter in value)
        has_digit = any(letter.isdigit() for letter in value)
        has_symbol = any(not letter.isalnum() for letter in value)

        if has_upper and has_lower and has_digit and has_symbol and len(value) >= 8:
            return value

        raise WrongPasswordFormat


class SignUp(BaseModel):
    name: str = Field(description="User name")
    lastname: str = Field(description="User lastname")
    role: UserRoleEnum = Field(default=UserRoleEnum.USER, description="User role")
    email: Annotated[str, BeforeValidator(lambda x: str(x).strip())] = Field(
        examples=["user@email.com.br", "user@email.com"], description="User email"
    )
    password: Annotated[str, BeforeValidator(lambda x: str(x).strip())] = Field(
        description="User password"
    )
    birthdate: date | None = Field(default=None, description="User birthdate")

    @field_validator("email")
    @classmethod
    def email_validator(cls, value: str):
        if re.match(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", value
        ):
            return value

        raise WrongEmailFormat

    @field_validator("password")
    @classmethod
    def password_validator(cls, value: str):
        has_upper = any(letter.isupper() for letter in value)
        has_lower = any(letter.islower() for letter in value)
        has_digit = any(letter.isdigit() for letter in value)
        has_symbol = any(not letter.isalnum() for letter in value)

        if has_upper and has_lower and has_digit and has_symbol and len(value) >= 8:
            return value

        raise WrongPasswordFormat


class AccessToken(BaseModel):
    id: str
    email: str
    expire_at: datetime = Field(
        default_factory=lambda: (
            datetime.now(timezone("UTC")) + timedelta(days=config.token_expire)
        )
    )
