from pymongo import AsyncMongoClient

from app.core.settings import settings

mongo_client = AsyncMongoClient(
    host=settings.MONGO_HOST,
    port=settings.MONGO_PORT,
)

mongo_db = mongo_client[settings.MONGO_DB]

employees_collection = mongo_db["employees"]
