
async def test_pagination_default(seed_db, test_client):
    """Проверка стандартной пагинации без параметров"""
    response = await test_client.get("/employees/")

    assert response.status_code == 200
    resp_json = response.json()

    data = resp_json["data"]
    pagination = resp_json["pagination"]

    assert len(data) <= 10
    assert pagination["current_page"] == 1
    assert pagination["limit"] == 10
    assert pagination["sort"] == "name"
    assert pagination["order"] == "asc"
