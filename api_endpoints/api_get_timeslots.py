import json

from datetime import datetime
from helpers.custom_log import get_logger
from helpers.decorators.api_gateway_handler import api_gateway_handler
from helpers.utils import get_body_from_event
from utils.holiday_api import get_holidays

logger = get_logger()


@api_gateway_handler
def api_get_timeslots(event: {}, context: {}):
    body = get_body_from_event(event=event)
    formatted_address = body.get("address")

    if not formatted_address:
        raise Exception("Missing required field: address")

    postcode = formatted_address.get("postcode")

    if not postcode:
        raise Exception("postcode is required in formatted address")

    # Open courier static json file
    courier_api_file = open('utils/courier_api.json')
    courier_timeslots = json.load(courier_api_file)

    available_timeslots = []

    # Fetch all available timeslots for this postcode
    for timeslot_id, timeslot in courier_timeslots.items():
        postcodes = timeslot["postcodes"]
        if postcode in postcodes:
            available_timeslots.extend(timeslot["time_slots"])

    # Handle timeslot falling on holidays
    holidays = get_holidays()
    available_timeslots_without_holiday = []

    for available_timeslot in available_timeslots:
        if not is_timeslot_fall_during_holiday(start_time=available_timeslot["start_time"], holidays=holidays):
            available_timeslots_without_holiday.append(available_timeslot)

    return available_timeslots_without_holiday


def is_timeslot_fall_during_holiday(start_time, holidays):
    is_holiday = False

    start_day = datetime.fromisoformat(start_time).day
    start_month = datetime.fromisoformat(start_time).month
    start_year = datetime.fromisoformat(start_time).year

    for holiday in holidays:
        holiday_date = holiday["date"]
        holiday_date_parsed = datetime.fromisoformat(holiday_date)
        holiday_day = holiday_date_parsed.day
        holiday_month = holiday_date_parsed.month
        holiday_year = holiday_date_parsed.year

        if holiday_day == start_day and holiday_month == start_month and holiday_year == start_year:
            is_holiday = True
            break

    return is_holiday

