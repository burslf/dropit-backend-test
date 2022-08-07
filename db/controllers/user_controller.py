from pymongo.database import Database
from pymongo.collection import ObjectId
from db.models.user import get_user_to_insert, session_add_new_user, session_get_user_by_id, session_get_user_by_name


def add_new_user(session: Database, name: str):
    conditional_fields = [name]

    if None in conditional_fields:
        raise Exception("Missing required fields")

    try:
        user_collection = session["user"]
        user_to_insert = get_user_to_insert(name=name)
        user_in_db = session_add_new_user(collection=user_collection, user=user_to_insert)

        return user_in_db

    except Exception as e:
        raise e


def get_user_by_id(session: Database, _id: str):
    conditional_fields = [_id]

    if None in conditional_fields:
        raise Exception("Missing required fields")

    try:
        user_collection = session["user"]
        user = session_get_user_by_id(collection=user_collection, _id=ObjectId(_id))

        return user

    except Exception as e:
        raise e


def get_user_by_name(session: Database, name: str):
    conditional_fields = [name]

    if None in conditional_fields:
        raise Exception("Missing required fields")

    try:
        user_collection = session["user"]
        user = session_get_user_by_name(collection=user_collection, name=name)

        return user

    except Exception as e:
        raise e
