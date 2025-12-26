from typing import Annotated

from fastapi import Query
from pydantic import BaseModel, Field


class PaginatedParams(BaseModel):
    """
    Схема для параметров запроса пагинации и сортировки
    """

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
            page: int = Query(1, ge=1, description="Номер страницы", examples=[1]),
            sort: str = Query(
                "name", description="Поле для сортировки", examples=["name"]
            ),
            order: str = Query(
                "asc",
                pattern="^(asc|desc)$",
                description="Направление сортировки",
                examples=["asc"],
            ),
        ):
            return cls(limit=limit, page=page, sort=sort, order=order)

        return dependency


class PaginationResponse(BaseModel):
    """
    Схема ответа с информацией о пагинации
    """

    total: Annotated[
        int, Field(description="Общее количество элементов в коллекции", example=42)
    ]
    limit: Annotated[
        int, Field(description="Количество элементов на одной странице", example=10)
    ]
    current_page: Annotated[int, Field(description="Текущий номер страницы", example=1)]
    last_page: Annotated[int, Field(description="Номер последней страницы", example=5)]
    sort: Annotated[
        str,
        Field(description="Поле, по которому выполнялась сортировка", example="name"),
    ]
    order: Annotated[
        str,
        Field(description="Направление сортировки: 'asc' или 'desc'", example="asc"),
    ]
