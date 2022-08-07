import json
from datetime import datetime
from pymongo.collection import Collection
from pymongo.collection import ObjectId


def session_add_user(collection: Collection, name: str):
    conditional_fields = [name]

    if None in conditional_fields:
        raise Exception("Missing required fields")

    try:
        # user = User(name=name).to_json()
        user_to_insert = get_user_to_insert(name=name)
        add_user_in_db = collection.insert_one(user_to_insert)
        user_to_insert["_id"] = add_user_in_db.inserted_id

    except Exception as e:
        raise e

    return user_to_insert


def session_get_user_by_name(collection: Collection, name: str):
    user = collection.find_one({"name": name})

    return user


def session_get_user_by_id(collection: Collection, _id: str):
    user = collection.find_one({"_id": ObjectId(_id)})

    return user


def get_user_to_insert(name: str):
    return {
        "created_at": datetime.utcnow(),
        "name": name
    }
