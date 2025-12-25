import pytest
from datetime import datetime
from tests.config import employees_collection

@pytest.fixture(scope="function", autouse=True)
def seed_db():

    test_data = [
        {
            "name": "Flynn Vang",
            "email": "flynn.vang@test.com",
            "age": 69,
            "company": "Twitter",
            "join_date": datetime.fromisoformat("2003-12-28T18:18:10-08:00"),
            "job_title": "janitor",
            "gender": "female",
            "salary": 9632,
        },
        {
            "name": "Cedric Page",
            "email": "cedric.page@test.com",
            "age": 63,
            "company": "Yandex",
            "join_date": datetime.fromisoformat("2001-06-10T19:08:52-07:00"),
            "job_title": "janitor",
            "gender": "male",
            "salary": 9688,
        },
    ]

    employees_collection.delete_many({})
    employees_collection.insert_many(test_data)

    yield test_data

    employees_collection.delete_many({})
