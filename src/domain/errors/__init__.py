from typing import Any, Dict
from fastapi import HTTPException


class NotFound(HTTPException):
    def __init__(
        self,
        status_code: int = 404,
        detail: Any = "Item not found",
        headers: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code, detail, headers)


class CouldntFindAuthInRequest(HTTPException):
    def __init__(
        self,
        status_code: int = 500,
        detail: Any = "Error while trying to get auth params in request",
        headers: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code, detail, headers)
