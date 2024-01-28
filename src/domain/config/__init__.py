__all__ = ("config",)

from datetime import datetime
from os import environ
from typing import Any

from dotenv import load_dotenv
from pytz import timezone

from src.domain.errors.config import MissingEnvKey


def _get_key(key: str, default: Any | None = None) -> Any:
    
    load_dotenv()

    for k, v in environ.items():
        if key.lower() == k.lower():
            return v

    if default != None:
        return default

    raise MissingEnvKey(key=key)


class _Config:
    def __init__(self):
        # APP FUNCTIONALITY (prod, stage, test, dev)
        self.env: str = _get_key("env")

        # APP INFO
        self.app_url: str = _get_key("app_url", "http://127.0.0.1:8000")
        self.app_host: str = _get_key("app_host", "0.0.0.0")
        self.app_port: int = int(_get_key("app_port", "8080"))

        # PROJECT INFO
        self.project_version: str = _get_key("project_version", "0.0.1")
        self.project_name: str = _get_key("project_name", "FastAPI")
        self.project_summary: str = _get_key("project_summary", "")
        self.project_desc: str = (
            f"[Interactive docs]({self.app_url}/docs) \t\n"
            f"[Detailed docs]({self.app_url}/redoc) \t\n"
            "\n"
            f'Last restart: {datetime.now(timezone("UTC")).strftime("%a %d %b %Y, %H:%M:%S %Z%z")}'
        )
        self.project_contact: dict[str, str] = {
            "name": "Contact",
            "url": "https://www.example.com/contact",
            "email": "example@email.com",
        }

        # AUTH
        self.crypt_key: str = _get_key("crypt_key")
        "encrypt secret key"
        self.token_expire: int = int(_get_key("token_expire", "1"))
        "default time to token expire (in days)"

        # CORS
        self.cors_origins: list[str] = ["*"]

        # DATABASE
        self._db_engine_mapper: dict[str, str] = {"mongodb": "mongodb+srv"}
        self._env_collection_mapper: dict[str, str] = {
            "prod": "db_prod",
            "stage": "db_stage",
            "test": "db_test",
            "dev": "db_dev",
        }
        self.db_colletion: str = self._env_collection_mapper.get(self.env, "missing")

        self.db_type: str = _get_key("db_type")
        self.db_user: str = _get_key("db_user")
        self.db_password: str = _get_key("db_password")
        self.db_route: str = _get_key("db_route")

        self._db_format: str = "{db_engine}://{user}:{password}@{route}"

        self.db_uri: str = self._db_format.format(
            db_engine=self._db_engine_mapper.get(self.db_type or "", "missing"),
            user=self.db_user,
            password=self.db_password,
            route=self.db_route,
        )

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({', '.join([f'{var}: {getattr(self, var)}'.replace('\n', '') for var in vars(self)])})'

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({', '.join([f'{var}: {getattr(self, var)}' for var in vars(self)])})'


config = _Config()


