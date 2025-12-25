from pydantic_settings import BaseSettings, SettingsConfigDict
from pymongo import AsyncMongoClient


class Settings(BaseSettings):
    MONGO_HOST: str = "mongo"
    MONGO_PORT: int = 27017
    MONGO_DB: str = "employees_db"

    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()

mongo_client = AsyncMongoClient(
    host=settings.MONGO_HOST,
    port=settings.MONGO_PORT,
)

mongo_db = mongo_client[settings.MONGO_DB]

employees_collection = mongo_db["employees"]
