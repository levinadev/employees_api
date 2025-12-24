from fastapi import FastAPI

from app.api.routers import main_router

app = FastAPI(
    title="Employees API",
    description="Микросервис для получения сотрудников.",
    version="1.0.0",
)
app.include_router(main_router)
