"""
VERSION 1 ROUTES
"""

from fastapi import APIRouter, Depends

from src.api.routes.v1 import auth, user
from src.domain.dependencies.auth import AuthDepends

router = APIRouter(prefix="/v1")

router.include_router(auth.router)
router.include_router(user.router, dependencies=[Depends(AuthDepends.validate_token)])
