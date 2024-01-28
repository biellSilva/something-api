from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from src.models.base import EntityBase


T = TypeVar("T", bound=EntityBase)


class IRepository(ABC, Generic[T]):
    _cache: dict[str, dict[str, T]] = {}

    def __init__(self, model: T) -> None:
        ...

    @abstractmethod
    async def count(self, *, filter: dict[str, Any] = {}) -> int:
        ...

    @abstractmethod
    async def get_by_id(self, *, id: str, **kwargs: dict[str, Any]) -> Any:
        ...

    @abstractmethod
    async def get_all(self, *, sort: dict[str, Any], **kwargs: dict[str, Any]) -> Any:
        ...

    @abstractmethod
    async def get_by(self, *, filter: dict[str, Any], **kwargs: dict[str, Any]) -> Any:
        ...

    @abstractmethod
    async def get_all_by(
        self, *, filter: dict[str, Any], sort: dict[str, Any], **kwargs: dict[str, Any]
    ) -> Any:
        ...

    @abstractmethod
    async def insert(self, *, data: dict[str, Any]) -> Any:
        ...

    @abstractmethod
    async def insert_many(self, *, datas: list[dict[str, Any]]) -> Any:
        ...

    @abstractmethod
    async def update(
        self, *, filter: dict[str, Any], data: dict[str, Any], **kwargs: dict[str, Any]
    ) -> Any:
        ...

    @abstractmethod
    async def update_by_id(
        self, *, id: str, data: dict[str, Any], **kwargs: dict[str, Any]
    ) -> Any:
        ...

    @abstractmethod
    async def update_many(
        self, *, filter: dict[str, Any], data: dict[str, Any], **kwargs: dict[str, Any]
    ) -> Any:
        ...

    @abstractmethod
    async def delete(self, *, filter: dict[str, Any], **kwargs: dict[str, Any]) -> Any:
        ...

    @abstractmethod
    async def delete_many(
        self, *, filter: dict[str, Any], **kwargs: dict[str, Any]
    ) -> Any:
        ...
