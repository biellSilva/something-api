from fastapi import UploadFile

from src.domain.usecases.auth import AuthUsecase
from src.schemas.auth import AccessToken, SignIn, SignUp

# route -> controller (validar dados da route) -> service -> <- scrapper (retorna dados)
#                                                   |-> <- entity (validar e modificar dados)
#                                                   |
#


class AuthController:
    AUTH_SERVICE = AuthUsecase

    @classmethod
    async def login(cls, body: SignIn):
        return await cls.AUTH_SERVICE.login_user(body=body)

    @classmethod
    async def register(cls, body: SignUp, image: UploadFile | None):
        await cls.AUTH_SERVICE.is_email_registred(body=body)
        return await cls.AUTH_SERVICE.register_user(body=body)

    @classmethod
    async def validate_token(cls, data: AccessToken):
        return await cls.AUTH_SERVICE.validate_token(data=data)
