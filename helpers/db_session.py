import os
from pymongo.database import Database


def get_session() -> Database:
    from pymongo import MongoClient

    connection_string = os.environ["DB_URL"]

    client = MongoClient(connection_string)

    return client['be_dropit']
