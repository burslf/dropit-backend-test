import json
from datetime import datetime
from pymongo.collection import Collection
from pymongo.collection import ObjectId


def as_dict(model):
    return json.loads(json.dumps(model.__dict__, default=str))


class User:
    def __init__(self, name):
        self.created_at = datetime.utcnow()
        self.name = name

    def to_json(self):
        return as_dict(self)


def add_user(collection: Collection, name: str):
    conditional_fields = [name]

    if None in conditional_fields:
        raise Exception("Missing required fields")

    try:
        user = User(name=name).to_json()

        add_user_in_db = collection.insert_one(user)
        user["_id"] = add_user_in_db.inserted_id

    except Exception as e:
        raise e

    return user


def session_get_user_by_name(collection: Collection, name: str):
    user = collection.find_one({"name": name})

    return user


def session_get_user_by_id(collection: Collection, _id: str):
    user = collection.find_one({"_id": ObjectId(_id)})

    return user
