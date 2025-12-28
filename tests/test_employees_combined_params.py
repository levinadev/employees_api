async def test_combined_filters_sort_pagination_single_result(seed_db, test_client):
    """
    Проверка комбинации: фильтр по name + company + gender
    + сортировка
    + пагинация (один ожидаемый результат)
    """
    params = {
        "limit": 5,
        "page": 1,
        "sort": "salary",
        "order": "desc",
        "name": "Slade",
        "company": "Google",
        "gender": "male",
    }

    query = "&".join(f"{k}={v}" for k, v in params.items())

    response = await test_client.get(f"/employees/?{query}")
    assert response.status_code == 200

    resp_json = response.json()
    data = resp_json["data"]
    pagination = resp_json["pagination"]

    assert len(data) == 1, "Ожидалась ровно одна запись"

    employee = data[0]

    assert employee == {
        "name": "Slade Bowman",
        "email": "et@vitae.com",
        "age": 44,
        "company": "Google",
        "join_date": "2013-02-10T00:27:48-08:00",
        "job_title": "manager",
        "gender": "male",
        "salary": 5808,
    }

    assert pagination == {
        "total": 1,
        "limit": 5,
        "current_page": 1,
        "last_page": 1,
        "sort": "salary",
        "order": "desc",
    }
