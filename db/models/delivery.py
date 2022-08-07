import json
from datetime import datetime
from pymongo.collection import Collection, ReturnDocument
from pymongo.collection import ObjectId


def as_dict(model):
    return json.loads(json.dumps(model.__dict__, default=str))


def add_delivery(collection: Collection, timeslot_id: str, user_id: ObjectId):
    conditional_fields = [timeslot_id, user_id]

    if None in conditional_fields:
        raise Exception("Missing required fields")
    try:

        delivery_to_insert = get_delivery_to_insert(timeslot_id=timeslot_id, user_id=user_id)

        add_delivery_in_db = collection.insert_one(delivery_to_insert)
        delivery_to_insert["_id"] = add_delivery_in_db.inserted_id

    except Exception as e:
        raise e

    return delivery_to_insert


def set_delivery_completed(collection: Collection, delivery_id: str):
    conditional_fields = [delivery_id]

    if None in conditional_fields:
        raise Exception("Missing required fields")

    try:
        updated_delivery = collection.find_one_and_update({'_id': ObjectId(delivery_id)},
                                                          {"$set": {'status': True}},
                                                          return_document=ReturnDocument.AFTER)
        return updated_delivery

    except Exception as e:
        raise e


def session_get_delivery_by_id(collection: Collection, _id: str):
    delivery = collection.find_one({"_id": _id})

    return delivery


def get_delivery_to_insert(timeslot_id: str, user_id: ObjectId, status=False):
    return {
        "created_at": datetime.utcnow(),
        "timeslot_id": timeslot_id,
        "user_id": user_id,
        "status": status
    }
