from datetime import datetime

from fastapi import Depends, Request
from fastapi.security import APIKeyHeader
from pytz import timezone

from src.domain.controllers.auth import AuthController
from src.domain.errors.auth import UnauthorizedUser
from src.domain.security.auth import Encrypter
from src.schemas.auth import AccessToken


class AuthDepends:
    @classmethod
    async def validate_token(
        cls,
        request: Request,
        token: str = Depends(
            APIKeyHeader(
                name="token",
                auto_error=False,
            )
        ),
    ):
        try:
            unhashed = AccessToken(**Encrypter.decode(token))

            if unhashed.expire_at > datetime.now(timezone("UTC")):
                await AuthController.validate_token(data=unhashed)
                request.__dict__.update({"user_auth": unhashed})
                return unhashed

            raise UnauthorizedUser
        except:
            raise UnauthorizedUser
