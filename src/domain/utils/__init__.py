from fastapi import Request
from src.domain.errors import CouldntFindAuthInRequest

from src.schemas.auth import AccessToken


def get_auth_from_request(request: Request) -> AccessToken:
    if auth := request.__dict__.get("user_auth", None):
        return auth

    raise CouldntFindAuthInRequest
