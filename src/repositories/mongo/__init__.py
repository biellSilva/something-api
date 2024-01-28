from typing import Any, Type, TypeVar

from src.models.base import EntityBase
from src.repositories.connections.mongo import MongoConnection
from src.repositories.interface import IRepository

Model = TypeVar("Model", bound=EntityBase)


class MongoRepository(IRepository[Model]):
    def __init__(self, model: Type[Model]) -> None:
        self.__collection = MongoConnection.get_collection(model.get_tablename())

    async def count(self, *, filter: dict[str, Any] = {}):
        return self.__collection.count_documents(filter=filter)

    async def get_by_id(self, *, id: str, **kwargs: dict[str, Any]):
        return self.__collection.find_one(filter={"id": id}, **kwargs)

    async def get_all(self, **kwargs: dict[str, Any]):
        return list(self.__collection.find(**kwargs))

    async def get_by(self, *, filter: dict[str, Any], **kwargs: dict[str, Any]):
        return self.__collection.find_one(filter=filter, **kwargs)

    async def get_all_by(self, *, filter: dict[str, Any], **kwargs: dict[str, Any]):
        return list(self.__collection.find(filter=filter, **kwargs))

    async def insert(self, *, data: dict[str, Any]):
        return self.__collection.insert_one(document=data)

    async def insert_many(self, *, datas: list[dict[str, Any]]):
        return self.__collection.insert_many(documents=datas, ordered=False)

    async def update(
        self, *, filter: dict[str, Any], data: dict[str, Any], **kwargs: dict[str, Any]
    ):
        return self.__collection.find_one_and_update(
            filter=filter, update=data, return_document=True, kwargs=kwargs
        )

    async def update_by_id(
        self, *, id: str, data: dict[str, Any], **kwargs: dict[str, Any]
    ):
        return self.__collection.find_one_and_update(
            filter={"id": id}, update=data, return_document=True, kwargs=kwargs
        )

    async def update_many(
        self, *, filter: dict[str, Any], data: dict[str, Any], **kwargs: dict[str, Any]
    ):
        return self.__collection.find_one_and_update(
            filter=filter, update=data, return_document=True, kwargs=kwargs
        )

    async def delete(self, *, filter: dict[str, Any], **kwargs: dict[str, Any]):
        return self.__collection.delete_one(filter=filter)

    async def delete_many(self, *, filter: dict[str, Any], **kwargs: dict[str, Any]):
        return self.__collection.delete_many(filter=filter)
