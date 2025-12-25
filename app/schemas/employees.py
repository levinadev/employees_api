from datetime import datetime

from pydantic import BaseModel, EmailStr


class Employee(BaseModel):
    """Схема сотрудника для ответа API."""

    name: str
    email: EmailStr
    age: int
    company: str
    join_date: datetime
    job_title: str
    gender: str
    salary: int
