from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field


class EmployeeFilterParams(BaseModel):
    """
    Схема фильтров для запроса сотрудников
    """

    name: str | None = Annotated[
        None, Field(description="Фильтр по имени", examples=["Flynn Vang"])
    ]
    email: str | None = Annotated[
        None, Field(description="Фильтр по email", examples=["user@example.com"])
    ]
    company: str | None = Annotated[
        None, Field(description="Фильтр по компании", examples=["Twitter"])
    ]
    job_title: str | None = Annotated[
        None, Field(description="Фильтр по должности", examples=["janitor"])
    ]
    gender: str | None = Annotated[
        None, Field(description="Фильтр по полу", examples=["female"])
    ]

    age_min: int | None = Annotated[
        None, Field(description="Минимальный возраст", examples=[30])
    ]
    age_max: int | None = Annotated[
        None, Field(description="Максимальный возраст", examples=[65])
    ]

    salary_min: int | None = Annotated[
        None, Field(description="Минимальная зарплата", examples=[3000])
    ]
    salary_max: int | None = Annotated[
        None, Field(description="Максимальная зарплата", examples=[10000])
    ]

    join_date_from: datetime | None = Annotated[
        None,
        Field(description="Дата трудоустройства от", examples=["2000-01-01T00:00:00Z"]),
    ]
    join_date_to: datetime | None = Annotated[
        None,
        Field(description="Дата трудоустройства до", examples=["2024-01-01T00:00:00Z"]),
    ]
