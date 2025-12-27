

async def test_get_employees(seed_db, test_client):

    response = await test_client.get("/employees/")

    assert response.status_code == 200

    data = response.json()["data"]
    assert len(data) == len(seed_db)

    names = [e["name"] for e in data]
    for item in seed_db:
        assert item["name"] in names
