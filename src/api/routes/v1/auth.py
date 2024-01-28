from fastapi import APIRouter, Body

from src.domain.controllers.auth import AuthController
from src.models.user import UserWithToken
from src.schemas.auth import SignIn, SignUp

router = APIRouter(prefix="/auth", tags=["Auth"])

RESPONSE_EXCLUDE = {"password"}


@router.post(
    path="/login",
    name="Login",
    response_model=UserWithToken,
    response_model_exclude=RESPONSE_EXCLUDE,
)
async def auth_login(body: SignIn = Body(description="User login")):
    """
    Login description
    """
    return await AuthController.login(body=body)


@router.post(
    path="/register",
    name="Register",
    response_model=UserWithToken,
    response_model_exclude=RESPONSE_EXCLUDE,
)
async def auth_register(
    body: SignUp = Body(description="User data"),
):
    """
    Register description
    """
    return await AuthController.register(body=body, image=None)
