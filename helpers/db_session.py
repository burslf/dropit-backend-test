import os


def get_session():
    from pymongo import MongoClient

    connection_string = os.environ["DB_URL"]

    client = MongoClient(connection_string)

    return client['be_dropit']
