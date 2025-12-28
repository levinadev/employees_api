from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, EmailStr, Field

from .pagination import PaginationResponse


class EmployeeResponse(BaseModel):

    name: Annotated[
        str,
        Field(description="Имя", examples=["Flynn Vang"]),
    ]
    email: Annotated[
        EmailStr,
        Field(description="Электронная почта", examples=["turpis.non@Nunc.edu"]),
    ]
    age: Annotated[
        int,
        Field(description="Возраст", examples=[69]),
    ]
    company: Annotated[
        str,
        Field(description="Компания", examples=["Twitter"]),
    ]
    join_date: Annotated[
        datetime,
        Field(
            description="Дата трудоустройства", examples=["2003-12-28T18:18:10-08:00"]
        ),
    ]
    job_title: Annotated[
        str,
        Field(description="Должность", examples=["janitor"]),
    ]
    gender: Annotated[
        str,
        Field(description="Пол", examples=["female"]),
    ]
    salary: Annotated[
        int,
        Field(description="Заработная плата", examples=[9632]),
    ]


class EmployeeListResponse(BaseModel):

    data: Annotated[
        list[EmployeeResponse],
        Field(description="Список сотрудников на текущей странице"),
    ]
    pagination: Annotated[
        PaginationResponse, Field(description="Информация о пагинации")
    ]
