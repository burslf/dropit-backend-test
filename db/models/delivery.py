import json
from datetime import datetime
from typing import TypedDict

from pymongo.collection import Collection, ReturnDocument
from pymongo.collection import ObjectId


class Delivery(TypedDict):
    created_at: datetime
    timeslot_id: str
    user_id: ObjectId
    status: bool


def session_add_delivery(collection: Collection, delivery: Delivery) -> Delivery:
    add_delivery_in_db = collection.insert_one(delivery)
    delivery["_id"] = add_delivery_in_db.inserted_id

    return delivery


def session_set_delivery_status(collection: Collection, delivery_id: ObjectId, status: bool) -> Delivery:
    updated_delivery = collection.find_one_and_update({'_id': ObjectId(delivery_id)},
                                                      {"$set": {'status': status}},
                                                      return_document=ReturnDocument.AFTER)
    return updated_delivery


def session_get_delivery_by_id(collection: Collection, _id: ObjectId) -> Delivery:
    delivery = collection.find_one({"_id": _id})

    return delivery


def session_delete_delivery(collection: Collection, delivery_id: ObjectId) -> Delivery:
    deleted_delivery = collection.find_one_and_delete({'_id': delivery_id})

    return deleted_delivery


def session_get_latest_delivery(collection: Collection) -> Delivery:
    latest_delivery = None
    delivery = list(collection.find().sort("created_at", -1).limit(1))

    if delivery:
        latest_delivery = delivery[0]

    return latest_delivery
