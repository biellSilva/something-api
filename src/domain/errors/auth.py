from typing import Any, Dict

from fastapi import HTTPException, status


class WrongEmailFormat(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail: Any = "Wrong email format",
        headers: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code, detail, headers)


class WrongPasswordFormat(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail: Any = "Wrong password format (must contain at least 8 characteres, 1 uppercase and 1 lowercase letter, numbers/digits and 1 special character)",
        headers: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code, detail, headers)


class WrongCpfFormat(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail: Any = "Wrong CPF format",
        headers: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code, detail, headers)


class WrongLoginParams(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_401_UNAUTHORIZED,
        detail: Any = "Wrong email/password",
        headers: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code, detail, headers)


class EmailNotExists(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_404_NOT_FOUND,
        detail: Any = "Email doesn't exists",
        headers: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code, detail, headers)


class EmailAlreadyExists(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_409_CONFLICT,
        detail: Any = "Email already exists",
        headers: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code, detail, headers)


class UnauthorizedUser(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_401_UNAUTHORIZED,
        detail: Any = "Access token is invalid or missing",
        headers: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(status_code, detail, headers)
