from math import ceil

from fastapi import APIRouter, Depends

from app.crud.employees import employees_crud
from app.schemas.employees import (
    EmployeeFilterParams,
    EmployeeListResponse,
)
from app.schemas.pagination import PaginatedParams, PaginationResponse

router = APIRouter()


@router.get("/", response_model=EmployeeListResponse)
async def get_employees(
    pagination: PaginatedParams = Depends(PaginatedParams.as_query()),
    filters: EmployeeFilterParams = Depends(),
) -> EmployeeListResponse:

    query_filter: dict = {}

    # string filters (regex)
    if filters.name:
        query_filter["name"] = {"$regex": filters.name, "$options": "i"}

    if filters.email:
        query_filter["email"] = {"$regex": filters.email, "$options": "i"}

    if filters.company:
        query_filter["company"] = filters.company

    if filters.job_title:
        query_filter["job_title"] = {"$regex": filters.job_title, "$options": "i"}

    if filters.gender:
        query_filter["gender"] = filters.gender

    # numeric ranges
    if filters.age_min or filters.age_max:
        query_filter["age"] = {}
        if filters.age_min:
            query_filter["age"]["$gte"] = filters.age_min
        if filters.age_max:
            query_filter["age"]["$lte"] = filters.age_max

    if filters.salary_min or filters.salary_max:
        query_filter["salary"] = {}
        if filters.salary_min:
            query_filter["salary"]["$gte"] = filters.salary_min
        if filters.salary_max:
            query_filter["salary"]["$lte"] = filters.salary_max

    # date range
    if filters.join_date_from or filters.join_date_to:
        query_filter["join_date"] = {}
        if filters.join_date_from:
            query_filter["join_date"]["$gte"] = filters.join_date_from
        if filters.join_date_to:
            query_filter["join_date"]["$lte"] = filters.join_date_to

    items, total = await employees_crud.get_all(
        limit=pagination.limit,
        page=pagination.page,
        sort=pagination.sort,
        order=pagination.order,
        filters=query_filter,
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
