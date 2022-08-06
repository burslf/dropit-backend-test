import os
import holidayapi

holiday_api_key = os.environ.get("HOLIDAY_API_KEY")


def get_holidays():
    if holiday_api_key is None:
        raise Exception("API Key is null")

    hapi = holidayapi.v1(holiday_api_key)
    res = None

    try:
        holidays = hapi.holidays({
            'country': 'IL',
            'year': '2021'
        })

        res = holidays.get("holidays")

    except Exception as e:
        raise e

    return res
