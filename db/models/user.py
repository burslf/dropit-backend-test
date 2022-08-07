import json
from datetime import datetime
from pymongo.collection import Collection
from pymongo.collection import ObjectId


def session_add_new_user(collection: Collection, user):
    add_user_in_db = collection.insert_one(user)
    user["_id"] = add_user_in_db.inserted_id

    return user


def session_get_user_by_name(collection: Collection, name: str):
    user = collection.find_one({"name": name})

    return user


def session_get_user_by_id(collection: Collection, _id: ObjectId):
    user = collection.find_one({"_id": _id})

    return user


def get_user_to_insert(name: str):
    return {
        "created_at": datetime.utcnow(),
        "name": name
    }
