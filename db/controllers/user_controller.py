import datetime

from pymongo.database import Database
from pymongo.collection import ObjectId
from db.models.user import session_add_new_user, session_get_user_by_id, session_get_user_by_name, \
    User


def add_new_user(session: Database, name: str):
    conditional_fields = [name]

    if None in conditional_fields:
        raise Exception("Missing required fields")

    try:
        user_collection = session["user"]
        user = User(
            name=name,
            created_at=datetime.datetime.utcnow()
        )
        print(user)
        user_in_db = session_add_new_user(collection=user_collection, user=user)

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
