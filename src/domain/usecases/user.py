from src.domain.errors import NotFound
from src.models.user import User
from src.repositories.mongo import MongoRepository


class UserUsecase:
    REPO = MongoRepository(User)

    @classmethod
    async def get_user(cls, id: str):
        if data := await cls.REPO.get_by_id(id=id):
            return User(**data)

        raise NotFound
