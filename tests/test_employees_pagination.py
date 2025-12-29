async def test_pagination_default(seed_db, test_client):
    """Проверка стандартной пагинации без параметров"""
    response = await test_client.get("/employees/")
    data = response.json()["data"]
    pagination = response.json()["pagination"]

    assert len(data) <= pagination["limit"]
    assert pagination["total"] == 600
    assert pagination["limit"] == 10
    assert pagination["current_page"] == 1
    assert pagination["last_page"] == 60
    assert pagination["sort"] == "name"
    assert pagination["order"] == "asc"


async def test_pagination_custom_limit(seed_db, test_client):
    """Проверка пагинации с пользовательским лимитом"""
    limit = 20
    response = await test_client.get(f"/employees/?limit={limit}")
    data = response.json()["data"]
    pagination = response.json()["pagination"]
    assert len(data) <= limit
    assert pagination["limit"] == limit
    assert pagination["current_page"] == 1


async def test_pagination_second_page(seed_db, test_client):
    """Проверка пагинации на второй странице и уникальности элементов"""
    page1 = 1
    page2 = 2

    response1 = await test_client.get(f"/employees/?page={page1}")
    data_page1 = response1.json()["data"]
    names_page1 = {e["name"] for e in data_page1}

    response2 = await test_client.get(f"/employees/?page={page2}")
    data_page2 = response2.json()["data"]
    pagination = response2.json()["pagination"]
    names_page2 = {e["name"] for e in data_page2}

    assert pagination["current_page"] == page2
    assert len(data_page2) <= pagination["limit"]
    assert (
        not names_page1 & names_page2
    ), "Элементы на второй странице пересекаются с первой!"


async def test_pagination_page_beyond_last(seed_db, test_client):
    """Проверка пагинации при запросе страницы больше последней"""
    page = 1000
    response = await test_client.get(f"/employees/?page={page}")
    data = response.json()["data"]
    pagination = response.json()["pagination"]
    assert pagination["current_page"] == page
    assert data == []


async def test_pagination_limit_one(seed_db, test_client):
    """Проверка пагинации с limit=1"""
    limit = 1
    response = await test_client.get(f"/employees/?limit={limit}")

    data = response.json()["data"]
    pagination = response.json()["pagination"]

    assert len(data) <= limit
    assert pagination["limit"] == limit
