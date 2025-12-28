async def test_filter_name(seed_db, test_client):
    """Проверка фильтра по имени"""
    name = "Aaron"
    response = await test_client.get(f"/employees/?name={name}")
    data = response.json()["data"]
    assert response.status_code == 200
    assert len(data) > 0, "Фильтр по имени не вернул записи"
    assert all(name in e["name"] for e in data)


async def test_filter_email(seed_db, test_client):
    """Проверка фильтра по email"""
    email = "Praesent.eu@ipsumleo.net"
    response = await test_client.get(f"/employees/?email={email}")
    data = response.json()["data"]
    assert response.status_code == 200
    assert len(data) > 0, "Фильтр по email не вернул записи"
    assert all(email in e["email"] for e in data)


async def test_filter_company(seed_db, test_client):
    """Проверка фильтра по компании"""
    company = "Google"
    response = await test_client.get(f"/employees/?company={company}")
    data = response.json()["data"]
    assert response.status_code == 200
    assert len(data) > 0, "Фильтр по компании не вернул записи"
    assert all(e["company"] == company for e in data)


async def test_filter_job_title(seed_db, test_client):
    """Проверка фильтра по должности"""
    job_title = "director"
    response = await test_client.get(f"/employees/?job_title={job_title}")
    data = response.json()["data"]
    assert response.status_code == 200
    assert len(data) > 0, "Фильтр по должности не вернул записи"
    assert all(job_title in e["job_title"] for e in data)


async def test_filter_gender(seed_db, test_client):
    """Проверка фильтра по полу"""
    gender = "male"
    response = await test_client.get(f"/employees/?gender={gender}")
    data = response.json()["data"]
    assert response.status_code == 200
    assert len(data) > 0, "Фильтр по полу не вернул записи"
    assert all(e["gender"] == gender for e in data)


async def test_filter_age_range(seed_db, test_client):
    """Проверка фильтра по диапазону возраста"""
    age_min, age_max = 30, 50
    response = await test_client.get(f"/employees/?age_min={age_min}&age_max={age_max}")
    data = response.json()["data"]
    assert response.status_code == 200
    assert len(data) > 0, "Фильтр по возрасту не вернул записи"
    assert all(age_min <= e["age"] <= age_max for e in data)


async def test_filter_salary_range(seed_db, test_client):
    """Проверка фильтра по диапазону зарплаты"""
    salary_min, salary_max = 3000, 5000
    response = await test_client.get(f"/employees/?salary_min={salary_min}&salary_max={salary_max}")
    data = response.json()["data"]
    assert response.status_code == 200
    assert len(data) > 0, "Фильтр по зарплате не вернул записи"
    assert all(salary_min <= e["salary"] <= salary_max for e in data)


async def test_filter_join_date_range(seed_db, test_client):
    """Проверка фильтра по дате трудоустройства"""
    join_date_from = "2000-01-01T00:00:00Z"
    join_date_to = "2010-12-31T23:59:59Z"
    response = await test_client.get(
        f"/employees/?join_date_from={join_date_from}&join_date_to={join_date_to}"
    )
    data = response.json()["data"]
    assert response.status_code == 200
    assert len(data) > 0, "Фильтр по датам не вернул записи"
    for e in data:
        assert join_date_from <= e["join_date"] <= join_date_to


async def test_filter_no_match(seed_db, test_client):
    """Проверка фильтра по отсутствующему значению"""
    name = "NonexistentName"
    response = await test_client.get(f"/employees/?name={name}")
    data = response.json()["data"]
    assert response.status_code == 200
    assert data == []


async def test_filter_invalid_age(seed_db, test_client):
    """Проверка неверного значения фильтра age_min"""
    age_min = -1
    response = await test_client.get(f"/employees/?age_min={age_min}")
    assert response.status_code == 422
    assert "detail" in response.json()
