from math import ceil

from fastapi import APIRouter, Depends

from app.crud.employees import employees_crud
from app.schemas.employees import EmployeeListResponse
from app.schemas.pagination import PaginatedParams, PaginationResponse

router = APIRouter()


@router.get("/", response_model=EmployeeListResponse)
async def get_employees(
    pagination: PaginatedParams = Depends(PaginatedParams.as_query()),
) -> EmployeeListResponse:

    items, total = await employees_crud.get_all(
        limit=pagination.limit,
        page=pagination.page,
        sort=pagination.sort,
        order=pagination.order,
    )

    last_page = ceil(total / pagination.limit) if total else 1

    return EmployeeListResponse(
        data=items,
        pagination=PaginationResponse(
            total=total,
            limit=pagination.limit,
            current_page=pagination.page,
            last_page=last_page,
            sort=pagination.sort,
            order=pagination.order,
        ),
    )
