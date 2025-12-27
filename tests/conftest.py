import json
from typing import AsyncGenerator
from httpx import AsyncClient, ASGITransport
import pytest
from pymongo import AsyncMongoClient
from pymongo.asynchronous.collection import AsyncCollection

from app.core.db import get_employees_collection
from app.main import app
from app.core.settings import settings

DATA_FILE = "mongo-init/employees.json"
TEST_MONGO_HOST = "localhost"
TEST_MONGO_PORT = 27018
TEST_MONGO_DB = "test_db"


@pytest.fixture(scope="function", autouse=True)
async def async_mongo_db():
    mongo_client = AsyncMongoClient(
        host=settings.MONGO_HOST,
        port=settings.MONGO_PORT,
    )

    mongo_db = mongo_client[settings.MONGO_DB]
    return mongo_db


@pytest.fixture(autouse=True)
async def test_collection(async_mongo_db):
    collection = async_mongo_db["employees"]
    yield collection


@pytest.fixture(scope="function", autouse=True)
async def seed_db(test_collection):
    with open(DATA_FILE, encoding="utf-8") as f:
        test_data = json.load(f)

    await test_collection.delete_many({})
    await test_collection.insert_many(test_data)

    yield test_data

    await test_collection.delete_many({})


@pytest.fixture
async def test_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
            transport=ASGITransport(app),
            base_url="http://web:8000",
    ) as client:
        yield client


@pytest.fixture(autouse=True)
async def override_dep(test_collection):
    mongo_client = AsyncMongoClient(
        host=settings.MONGO_HOST,
        port=settings.MONGO_PORT,
    )

    mongo_db = mongo_client[settings.MONGO_DB]

    async def _override_dep() -> AsyncGenerator[AsyncCollection, None]:
        collection = mongo_db["employees"]
        yield collection

    app.dependency_overrides[get_employees_collection] = _override_dep
    yield

    app.dependency_overrides.clear()
