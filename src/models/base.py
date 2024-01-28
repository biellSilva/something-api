from datetime import datetime
from uuid import uuid4

from pydantic import BaseModel, Field
from pytz import timezone


class EntityBase(BaseModel):
    id: str = Field(
        default_factory=lambda: uuid4().__str__(), frozen=True, description="UUID4"
    )
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone("UTC")),
        frozen=True,
        description="Datetime of creation",
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone("UTC")),
        description="Datetime of last of update",
    )

    @classmethod
    def get_tablename(cls) -> str:
        ...
