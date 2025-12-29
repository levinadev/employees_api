import json
from typing import AsyncGenerator

import pytest
from httpx import ASGITransport, AsyncClient
from pymongo import AsyncMongoClient
from pymongo.asynchronous.collection import AsyncCollection

from app.core.db import get_employees_collection
from app.core.settings import settings
from app.main import app

TEST_DATA_FILE = settings.TEST_DATA_FILE
TEST_MONGO_HOST = settings.TEST_MONGO_HOST
TEST_MONGO_PORT = settings.TEST_MONGO_PORT
TEST_MONGO_DB = settings.TEST_MONGO_DB
TEST_BASE_URL = settings.TEST_BASE_URL


@pytest.fixture(scope="function", autouse=True)
async def async_mongo_db():
    mongo_client = AsyncMongoClient(
        host=TEST_MONGO_HOST,
        port=TEST_MONGO_PORT,
    )
    mongo_db = mongo_client[TEST_MONGO_DB]
    yield mongo_db
    await mongo_client.close()


@pytest.fixture(autouse=True)
async def test_collection(async_mongo_db):
    collection = async_mongo_db["employees"]
    yield collection


@pytest.fixture(scope="function", autouse=True)
async def seed_db(test_collection):
    with open(TEST_DATA_FILE, encoding="utf-8") as f:
        test_data = json.load(f)

    await test_collection.delete_many({})
    await test_collection.insert_many(test_data)

    yield test_data

    await test_collection.delete_many({})


@pytest.fixture
async def test_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        transport=ASGITransport(app),
        base_url=TEST_BASE_URL,
    ) as client:
        yield client


@pytest.fixture(autouse=True)
async def override_dep(test_collection):
    mongo_client = AsyncMongoClient(
        host=TEST_MONGO_HOST,
        port=TEST_MONGO_PORT,
    )

    mongo_db = mongo_client[TEST_MONGO_DB]

    async def _override_dep() -> AsyncGenerator[AsyncCollection, None]:
        collection = mongo_db["employees"]
        yield collection

    app.dependency_overrides[get_employees_collection] = _override_dep
    yield

    app.dependency_overrides.clear()
