async def test_sorting_default(seed_db, test_client):
    """Проверка сортировки по умолчанию: по name asc"""
    response = await test_client.get("/employees/")
    data = response.json()["data"]
    names = [e["name"] for e in data]
    assert names == sorted(names)


async def test_sorting_by_age_desc(seed_db, test_client):
    """Проверка сортировки по age по убыванию"""
    response = await test_client.get("/employees/?sort=age&order=desc")
    data = response.json()["data"]
    ages = [e["age"] for e in data]
    assert ages == sorted(ages, reverse=True)


async def test_sorting_invalid_params(seed_db, test_client):
    """Проверка неверных значений sort и order"""
    response = await test_client.get("/employees/?sort=nonexistent_field&order=up")
    assert response.status_code == 422
    assert "detail" in response.json()
