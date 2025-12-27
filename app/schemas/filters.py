from datetime import datetime

from fastapi import Query
from pydantic import BaseModel


class EmployeeFilterParams(BaseModel):
    """
    Схема для параметров фильтров сотрудников
    """

    name: str | None
    email: str | None
    company: str | None
    job_title: str | None
    gender: str | None

    age_min: int | None
    age_max: int | None

    salary_min: int | None
    salary_max: int | None

    join_date_from: datetime | None
    join_date_to: datetime | None

    @classmethod
    def as_query(cls):
        def dependency(
            name: str | None = Query(
                None, description="Фильтр по имени", examples=["Flynn Vang"]
            ),
            email: str | None = Query(
                None, description="Фильтр по email", examples=["user@example.com"]
            ),
            company: str | None = Query(
                None, description="Фильтр по компании", examples=["Twitter"]
            ),
            job_title: str | None = Query(
                None, description="Фильтр по должности", examples=["janitor"]
            ),
            gender: str | None = Query(
                None, description="Фильтр по полу", examples=["female"]
            ),
            age_min: int | None = Query(
                None, ge=0, description="Минимальный возраст", examples=[30]
            ),
            age_max: int | None = Query(
                None, ge=0, description="Максимальный возраст", examples=[65]
            ),
            salary_min: int | None = Query(
                None, ge=0, description="Минимальная зарплата", examples=[3000]
            ),
            salary_max: int | None = Query(
                None, ge=0, description="Максимальная зарплата", examples=[10000]
            ),
            join_date_from: datetime | None = Query(
                None, description="Дата трудоустройства от"
            ),
            join_date_to: datetime | None = Query(
                None, description="Дата трудоустройства до"
            ),
        ):
            return cls(
                name=name,
                email=email,
                company=company,
                job_title=job_title,
                gender=gender,
                age_min=age_min,
                age_max=age_max,
                salary_min=salary_min,
                salary_max=salary_max,
                join_date_from=join_date_from,
                join_date_to=join_date_to,
            )

        return dependency

    def to_mongo(self) -> dict:
        query: dict = {}

        if self.name:
            query["name"] = {"$regex": self.name, "$options": "i"}
        if self.email:
            query["email"] = {"$regex": self.email, "$options": "i"}
        if self.company:
            query["company"] = self.company
        if self.job_title:
            query["job_title"] = {"$regex": self.job_title, "$options": "i"}
        if self.gender:
            query["gender"] = self.gender

        if self.age_min or self.age_max:
            query["age"] = {}
            if self.age_min:
                query["age"]["$gte"] = self.age_min
            if self.age_max:
                query["age"]["$lte"] = self.age_max

        if self.salary_min or self.salary_max:
            query["salary"] = {}
            if self.salary_min:
                query["salary"]["$gte"] = self.salary_min
            if self.salary_max:
                query["salary"]["$lte"] = self.salary_max

        if self.join_date_from or self.join_date_to:
            query["join_date"] = {}
            if self.join_date_from:
                query["join_date"]["$gte"] = self.join_date_from
            if self.join_date_to:
                query["join_date"]["$lte"] = self.join_date_to

        return query
