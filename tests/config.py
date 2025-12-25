from pymongo import MongoClient

TEST_MONGO_HOST = "mongo_test"
TEST_MONGO_PORT = 27017
TEST_MONGO_DB = "test_db"

client = MongoClient(
    host=TEST_MONGO_HOST,
    port=TEST_MONGO_PORT,
)

db = client[TEST_MONGO_DB]
employees_collection = db["employees"]
