from fastapi import APIRouter, Depends, Path, Request

from src.domain.controllers.user import UserController
from src.domain.dependencies.auth import AuthDepends
from src.domain.utils import get_auth_from_request
from src.models.user import User

router = APIRouter(
    prefix="/user", tags=["User"], dependencies=[Depends(AuthDepends.validate_token)]
)

EXCLUDE = {"password"}


@router.get(
    "", name="Get self user", response_model=User, response_model_exclude=EXCLUDE
)
async def get_self_user(request: Request):
    """
    GET self user description
    """
    user_auth = get_auth_from_request(request=request)
    return await UserController.get_user(id=user_auth.id)


@router.get(
    "/{id}", name="Get user", response_model=User, response_model_exclude=EXCLUDE
)
async def get_user(request: Request, id: str = Path(description="User ID")):
    """
    GET user description
    """
    return await UserController.get_user(id=id)
