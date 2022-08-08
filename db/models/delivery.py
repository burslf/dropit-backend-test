import json
from datetime import datetime
from pymongo.collection import Collection, ReturnDocument
from pymongo.collection import ObjectId


def session_add_delivery(collection: Collection, delivery):
    add_delivery_in_db = collection.insert_one(delivery)
    delivery["_id"] = add_delivery_in_db.inserted_id

    return delivery


def session_set_delivery_status(collection: Collection, delivery_id: ObjectId, status: bool):
    updated_delivery = collection.find_one_and_update({'_id': ObjectId(delivery_id)},
                                                      {"$set": {'status': status}},
                                                      return_document=ReturnDocument.AFTER)
    return updated_delivery


def session_get_delivery_by_id(collection: Collection, _id: ObjectId):
    delivery = collection.find_one({"_id": _id})

    return delivery


def session_delete_delivery(collection: Collection, delivery_id: ObjectId):
    updated_delivery = collection.find_one_and_delete({'_id': delivery_id})
    return updated_delivery


def get_delivery_to_insert(timeslot_id: str, user_id: ObjectId, status=False):
    return {
        "created_at": datetime.utcnow(),
        "timeslot_id": timeslot_id,
        "user_id": user_id,
        "status": status
    }
