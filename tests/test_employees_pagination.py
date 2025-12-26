from fastapi.testclient import TestClient
from app.main import app

def test_pagination_default(seed_db):
    """Проверка стандартной пагинации без параметров"""
    with TestClient(app) as client:
        response = client.get("/employees/")

    assert response.status_code == 200
    resp_json = response.json()

    data = resp_json["data"]
    pagination = resp_json["pagination"]

    assert len(data) <= 10
    assert pagination["current_page"] == 1
    assert pagination["limit"] == 10
    assert pagination["sort"] == "name"
    assert pagination["order"] == "asc"
