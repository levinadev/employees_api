from typing import AsyncGenerator

from pymongo import AsyncMongoClient
from pymongo.asynchronous.collection import AsyncCollection

from app.core.settings import settings

mongo_client = AsyncMongoClient(
    host=settings.MONGO_HOST,
    port=settings.MONGO_PORT,
)


def get_db():
    mongo_db = mongo_client[settings.MONGO_DB]
    return mongo_db


async def get_employees_collection() -> AsyncGenerator[AsyncCollection, None]:
    db = get_db()
    collection = db["employees"]
    yield collection
