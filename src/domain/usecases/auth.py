from src.domain.errors.auth import UnauthorizedUser, WrongLoginParams
from src.domain.security.auth import Encrypter
from src.models.user import User, UserWithToken
from src.repositories.mongo import MongoRepository
from src.schemas.auth import AccessToken, SignIn, SignUp


class AuthUsecase:
    USER_REPO = MongoRepository(User)

    @classmethod
    async def register_user(cls, body: SignUp):
        user = UserWithToken(
            password=Encrypter.hash(body.password),
            **body.model_dump(exclude={"password"}),
        )

        user.token = Encrypter.encode(payload=AccessToken(**user.model_dump()))

        await cls.USER_REPO.insert(data=user.model_dump(mode="json", exclude={"token"}))

        return user

    @classmethod
    async def is_email_registred(cls, body: SignUp):
        return await cls.USER_REPO.count(filter={"email": body.email})

    @classmethod
    async def login_user(cls, body: SignIn):
        if data := await cls.USER_REPO.get_by(filter={"email": body.email}):
            user = UserWithToken(**data)

            if user.password == Encrypter.hash(body.password):
                user.token = Encrypter.encode(AccessToken(**user.model_dump()))
                return user

        raise WrongLoginParams

    @classmethod
    async def validate_token(cls, data: AccessToken):
        if _ := await cls.USER_REPO.get_by_id(id=data.id, projection={"id": True}):
            return True

        raise UnauthorizedUser
