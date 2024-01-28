from enum import StrEnum


class UserRoleEnum(StrEnum):
    USER = "USER"
    MODERATOR = "MODERATOR"
    ADMIN = "ADMIN"
    OWNER = "OWNER"
