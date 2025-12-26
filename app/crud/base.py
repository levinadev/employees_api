class BaseMongoCRUD:
    def __init__(self, collection):
        self.collection = collection

    async def get_all(
        self,
        *,
        limit: int,
        page: int,
        sort: str,
        order: str,
        filters: dict | None = None,
    ) -> tuple[list[dict], int]:
        """
        Получение списка документов с пагинацией, сортировкой и фильтрацией
        """
        skip = (page - 1) * limit
        sort_direction = 1 if order == "asc" else -1
        query_filter = filters or {}

        cursor = (
            self.collection.find(query_filter, {"_id": 0})
            .sort(sort, sort_direction)
            .skip(skip)
            .limit(limit)
        )

        items = await cursor.to_list(length=limit)
        total = await self.collection.count_documents(query_filter)

        return items, total
