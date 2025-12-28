from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    MONGO_HOST: str = "mongo"
    MONGO_PORT: int = 27017
    MONGO_DB: str = "employees_db"

    TEST_MONGO_HOST: str = "localhost"
    TEST_MONGO_PORT: int = 27018
    TEST_MONGO_DB: str = "test_db"
    TEST_DATA_FILE: str = "app/data/employees.json"
    TEST_BASE_URL: str = "http://web:8000"

    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
