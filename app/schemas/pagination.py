from enum import StrEnum
from typing import Annotated

from fastapi import Query
from pydantic import BaseModel, Field


class SortOrder(StrEnum):
    ASC = "asc"
    DESC = "desc"


class PaginatedParams(BaseModel):

    limit: int
    page: int
    sort: str
    order: str

    @classmethod
    def as_query(cls):
        def dependency(
            limit: int = Query(
                10,
                ge=1,
                description="Количество записей на одной странице",
                examples=[10],
            ),
            page: int = Query(
                1,
                ge=1,
                description="Номер страницы",
                examples=[1],
            ),
            sort: str = Query(
                "name",
                description="Поле для сортировки. Доступные поля: name, age, salary и т.д.",
                examples=["name"],
            ),
            order: SortOrder = Query(
                SortOrder.ASC,
                description="Направление сортировки",
                examples=[SortOrder.ASC, SortOrder.DESC],
            ),
        ):
            return cls(limit=limit, page=page, sort=sort, order=order)

        return dependency


class PaginationResponse(BaseModel):

    total: Annotated[
        int,
        Field(description="Общее количество элементов в коллекции", examples=[42]),
    ]
    limit: Annotated[
        int,
        Field(description="Количество элементов на одной странице", examples=[10]),
    ]
    current_page: Annotated[
        int,
        Field(description="Текущий номер страницы", examples=[1]),
    ]
    last_page: Annotated[
        int,
        Field(description="Номер последней страницы", examples=[5]),
    ]
    sort: Annotated[
        str,
        Field(
            description="Поле, по которому выполнялась сортировка", examples=["name"]
        ),
    ]
    order: Annotated[
        str,
        Field(description="Направление сортировки: 'asc' или 'desc'", examples=["asc"]),
    ]
