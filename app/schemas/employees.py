from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, EmailStr, Field

from .pagination import PaginationResponse


class EmployeeResponse(BaseModel):
    """
    Схема ответа при получении сотрудника
    """

    name: Annotated[str, Field(description="Имя", examples=["Flynn Vang"])]
    email: Annotated[
        EmailStr,
        Field(description="Электронная почта", examples=["turpis.non@Nunc.edu"]),
    ]
    age: Annotated[int, Field(description="Возраст", examples=[69])]
    company: Annotated[str, Field(description="Компания", examples=["Twitter"])]
    join_date: Annotated[
        datetime,
        Field(
            description="Дата трудоустройства", examples=["2003-12-28T18:18:10-08:00"]
        ),
    ]
    job_title: Annotated[str, Field(description="Должность", examples=["janitor"])]
    gender: Annotated[str, Field(description="Пол", examples=["female"])]
    salary: Annotated[int, Field(description="Заработная плата", examples=[9632])]


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


class EmployeeListResponse(BaseModel):
    """
    Схема ответа при получении списка сотрудников
    """

    data: Annotated[
        list[EmployeeResponse],
        Field(description="Список сотрудников на текущей странице"),
    ]
    pagination: Annotated[
        PaginationResponse, Field(description="Информация о пагинации")
    ]
