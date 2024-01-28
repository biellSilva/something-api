from functools import lru_cache
from hashlib import md5

from jwt import decode as jwt_decode  # type: ignore
from jwt import encode as jwt_encode  # type: ignore

from src.domain import config
from src.schemas.auth import AccessToken


class Encrypter:
    @classmethod
    def encode(cls, payload: AccessToken):
        return jwt_encode(
            payload=payload.model_dump(mode="json"),
            key=config.crypt_key,
            algorithm="HS256",
        )

    @classmethod
    @lru_cache
    def decode(cls, payload: str):
        return jwt_decode(jwt=payload, key=config.crypt_key, algorithms=["HS256"])

    @classmethod
    def hash(cls, payload: str):
        return md5(string=str(payload + config.crypt_key).encode()).hexdigest()
