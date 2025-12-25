class BaseMongoCRUD:
    def __init__(self, collection):
        self.collection = collection

    async def get_all(self) -> list[dict]:
        """Получить все документы коллекции без _id"""
        return await self.collection.find({}, {"_id": 0}).to_list(length=None)
