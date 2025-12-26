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
    ) -> tuple[list[dict], int]:
        """
        Получение списка документов с пагинацией и сортировкой
        """
        skip = (page - 1) * limit
        sort_direction = 1 if order == "asc" else -1

        cursor = (
            self.collection.find({}, {"_id": 0})
            .sort(sort, sort_direction)
            .skip(skip)
            .limit(limit)
        )

        items = await cursor.to_list(length=limit)
        total = await self.collection.count_documents({})

        return items, total
