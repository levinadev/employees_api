from fastapi.testclient import TestClient
from app.main import app

def test_get_employees(seed_db):
    with TestClient(app) as client:
        response = client.get("/employees/")

    assert response.status_code == 200

    data = response.json()["data"]
    assert len(data) == len(seed_db)

    names = [e["name"] for e in data]
    for item in seed_db:
        assert item["name"] in names
