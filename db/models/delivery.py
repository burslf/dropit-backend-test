import json
from datetime import datetime
from pymongo.collection import Collection, ReturnDocument
from pymongo.collection import ObjectId


def as_dict(model):
    return json.loads(json.dumps(model.__dict__, default=str))


class Delivery:
    def __init__(self, status, timeslot_id):
        self.created_at = datetime.utcnow()
        self.timeslot_id = timeslot_id
        self.status = status

    def to_json(self):
        return as_dict(self)


def add_delivery(collection: Collection, timeslot_id: int):
    conditional_fields = [timeslot_id]

    if None in conditional_fields:
        raise Exception("Missing required fields")
    try:
        delivery = Delivery(timeslot_id=timeslot_id, status=False).to_json()

        add_delivery_in_db = collection.insert_one(delivery)
        delivery["_id"] = add_delivery_in_db.inserted_id

    except Exception as e:
        raise e

    return delivery


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
