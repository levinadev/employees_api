from app.core.db import employees_collection
from app.crud.base import BaseMongoCRUD


class EmployeesCRUD(BaseMongoCRUD):
    """Репозиторий сотрудников"""

    def __init__(self):
        super().__init__(employees_collection)


employees_crud = EmployeesCRUD()
