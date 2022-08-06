import os
import urllib.parse
import requests
from requests.structures import CaseInsensitiveDict

geoapify_url = "https://api.geoapify.com/v1/geocode/search?"
geoapify_key = os.environ.get("GEOAPIFY_KEY")


def format_text_to_urlencoded(text:str) -> str:
    return urllib.parse.quote(text)


def get_formatted_address(raw_address: str):
    if geoapify_key is None:
        raise Exception("API Key is null")

    url = f'{geoapify_url}text={format_text_to_urlencoded(raw_address)}&apiKey={geoapify_key}'

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    try:
        resp = requests.get(url, headers=headers)
        resp.raise_for_status()
        res = resp.json()
        formatted_addresses = res.get("features")

        if len(formatted_addresses) == 0:
            raise Exception("No address found for this text")

        first_formatted_address_found = formatted_addresses[0]
        formatted_address = first_formatted_address_found.get("properties")

        if not formatted_address:
            raise Exception("Cannot find properties field in formatted address")

        return {
            "street": formatted_address.get("street"),
            "line1": formatted_address.get("address_line1"),
            "line2": formatted_address.get("address_line2"),
            "country": formatted_address.get("country"),
            "postcode": formatted_address.get("postcode")
        }

    except Exception as e:
        raise e

