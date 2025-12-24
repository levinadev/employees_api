from fastapi import APIRouter

from app.api.endpoints import employees_router

main_router = APIRouter()

main_router.include_router(employees_router, prefix="/employees", tags=["employees"])
