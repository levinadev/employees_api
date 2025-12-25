from fastapi import APIRouter

from app.crud.employees import employees_crud
from app.schemas.employees import Employee

router = APIRouter()


@router.get("/", response_model=list[Employee])
async def read_employees() -> list[Employee]:
    return await employees_crud.get_all()
