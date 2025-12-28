from math import ceil


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
        skip = (page - 1) * limit
        sort_direction = 1 if order == "asc" else -1
        query_filter = filters or {}

        cursor = (
            self.collection.find(query_filter, {"_id": 0})
            .sort(sort, sort_direction)
            .skip(skip)
            .limit(limit)
        )

        items = await cursor.to_list()
        total = await self.collection.count_documents(query_filter)

        return items, total

    async def get_all_with_pagination(
        self,
        *,
        limit: int,
        page: int,
        sort: str,
        order: str,
        filters: dict | None = None,
    ) -> tuple[list[dict], dict]:
        items, total = await self.get_all(
            limit=limit,
            page=page,
            sort=sort,
            order=order,
            filters=filters,
        )
        last_page = ceil(total / limit) if total else 1
        pagination = {
            "total": total,
            "limit": limit,
            "current_page": page,
            "last_page": last_page,
            "sort": sort,
            "order": order,
        }
        return items, pagination
