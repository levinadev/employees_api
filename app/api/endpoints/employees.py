from fastapi import APIRouter, Depends
from pymongo.asynchronous.collection import AsyncCollection

from app.core.db import get_employees_collection
from app.crud.employees import EmployeesCRUD
from app.schemas.employees import EmployeeListResponse
from app.schemas.filters import EmployeeFilterParams
from app.schemas.pagination import PaginatedParams, PaginationResponse

router = APIRouter()


@router.get("/", response_model=EmployeeListResponse)
async def get_employees(
    pagination: PaginatedParams = Depends(PaginatedParams.as_query()),
    filters: EmployeeFilterParams = Depends(EmployeeFilterParams.as_query()),
    db_collection: AsyncCollection = Depends(get_employees_collection),
) -> EmployeeListResponse:
    employees_crud = EmployeesCRUD(collection=db_collection)

    items, pagination_dict = await employees_crud.get_all_with_pagination(
        limit=pagination.limit,
        page=pagination.page,
        sort=pagination.sort,
        order=pagination.order,
        filters=filters.to_mongo(),
    )

    return EmployeeListResponse(
        data=items,
        pagination=PaginationResponse(**pagination_dict),
    )
