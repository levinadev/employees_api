const dbName = "employees_db";
const collectionName = "employees";

const db = db.getSiblingDB(dbName);

const data = JSON.parse(
  require("fs").readFileSync("/docker-entrypoint-initdb.d/employees.json", "utf8")
);

db[collectionName].insertMany(data);
