import json
import datetime
from pymongo.collection import Collection, ReturnDocument, ObjectId


def as_dict(model):
    return json.loads(json.dumps(model.__dict__, default=str))


class BusinessCapacity:
    def __init__(self, created_at, date, updated_at=None, capacity=0):
        self.created_at = created_at
        self.updated_at = updated_at
        self.date = date
        self.capacity = capacity

    def to_json(self):
        return as_dict(self)


def add_business_capacity(collection: Collection):
    try:
        date_now = datetime.datetime.utcnow()
        business_capacity = BusinessCapacity(created_at=date_now, date=date_now).to_json()

        add_business_capacity_in_db = collection.insert_one(business_capacity)
        business_capacity["_id"] = add_business_capacity_in_db.inserted_id

    except Exception as e:
        raise e

    return business_capacity


def update_business_capacity(collection: Collection, business_capacity_id: str):
    conditional_fields = [business_capacity_id]

    if None in conditional_fields:
        raise Exception("Missing required fields")

    try:
        updated_business_capacity = collection.find_one_and_update({'_id': ObjectId(business_capacity_id)},
                                                                   {"$increment": {'capacity': 1}},
                                                                   return_document=ReturnDocument.AFTER)
        return updated_business_capacity

    except Exception as e:
        raise e


def session_get_business_capacity_by_date(collection: Collection, date: str):
    date_parsed = datetime.datetime.strptime(date, "%Y-%m-%d")
    next_day = date_parsed + datetime.timedelta(days=1)
    date_format = datetime.datetime.isoformat(date_parsed)
    next_day_format = datetime.datetime.isoformat(next_day)

    business_capacity = collection.find_one({"date": {"$gte": date_format, "$lt": next_day_format}})

    return business_capacity
