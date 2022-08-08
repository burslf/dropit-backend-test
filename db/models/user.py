import json
from datetime import datetime
from typing import TypedDict

from pymongo.collection import Collection
from pymongo.collection import ObjectId


class User(TypedDict):
    created_at: datetime
    name: str


def session_add_new_user(collection: Collection, user: User):
    add_user_in_db = collection.insert_one(user)
    user["_id"] = add_user_in_db.inserted_id

    return user


def session_get_user_by_name(collection: Collection, name: str):
    user = collection.find_one({"name": name})

    return user


def session_get_user_by_id(collection: Collection, _id: ObjectId):
    user = collection.find_one({"_id": _id})

    return user
