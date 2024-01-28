from typing import Any, Mapping

from pymongo import MongoClient
from pymongo.server_api import ServerApi

from src.domain import config


class MongoConnection:
    client: MongoClient[Mapping[str, Any]] = MongoClient(
        config.db_uri, server_api=ServerApi("1")
    )

    try:
        client.admin.command("ping")
    except Exception as err:
        print("Mongo connection error: ", err)
        exit()

    db = client.get_database(config.db_colletion)

    @classmethod
    def get_collection(cls, collection_name: str):
        return cls.db.get_collection(collection_name)
