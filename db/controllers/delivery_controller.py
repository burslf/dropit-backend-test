from db.models.delivery import session_set_delivery_status, get_delivery_to_insert, session_add_delivery, \
    session_get_delivery_by_id, session_delete_delivery
from pymongo.database import Database
from pymongo.collection import ObjectId


def add_new_delivery(session: Database, timeslot_id: str, user_id: str):
    conditional_fields = [timeslot_id, user_id]

    if None in conditional_fields:
        raise Exception("Missing required fields")

    try:
        delivery_collection = session["delivery"]
        delivery_to_insert = get_delivery_to_insert(timeslot_id=timeslot_id, user_id=ObjectId(user_id))
        delivery_in_db = session_add_delivery(collection=delivery_collection, delivery=delivery_to_insert)

        return delivery_in_db

    except Exception as e:
        raise e


def set_delivery_completed(session: Database, delivery_id: str):
    conditional_fields = [delivery_id]

    if None in conditional_fields:
        raise Exception("Missing required fields")

    try:
        delivery_collection = session["delivery"]
        updated_delivery = session_set_delivery_status(collection=delivery_collection,
                                                       delivery_id=ObjectId(delivery_id), status=True)

        if updated_delivery is None:
            raise Exception("No delivery found for this id")

        return updated_delivery

    except Exception as e:
        raise e


def get_delivery_by_id(session: Database, delivery_id: str):
    conditional_fields = [delivery_id]

    if None in conditional_fields:
        raise Exception("Missing required fields")

    try:
        delivery_collection = session["delivery"]
        delivery = session_get_delivery_by_id(collection=delivery_collection, _id=ObjectId(delivery_id))

        return delivery

    except Exception as e:
        raise e


def cancel_delivery(session: Database, delivery_id: str):
    conditional_fields = [delivery_id]

    if None in conditional_fields:
        raise Exception("Missing required fields")

    try:
        delivery_collection = session["delivery"]
        deleted_delivery = session_delete_delivery(collection=delivery_collection, delivery_id=ObjectId(delivery_id))

        if deleted_delivery is None:
            raise Exception("No delivery found for this id")

        return deleted_delivery

    except Exception as e:
        raise e
