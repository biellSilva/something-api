from src.domain.usecases.user import UserUsecase


class UserController:
    SERVICE = UserUsecase()

    @classmethod
    async def get_user(cls, id: str):
        return await cls.SERVICE.get_user(id=id)
