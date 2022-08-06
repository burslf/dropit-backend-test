from helpers.custom_log import get_logger
from helpers.decorators.api_gateway_handler import api_gateway_handler
from helpers.utils import get_body_from_event
from utils.geoloc_api import get_formatted_address

logger = get_logger()


@api_gateway_handler
def api_resolve_address(event: {}, context: {}):
    body = get_body_from_event(event=event)
    raw_address = body.get("searchTerm")

    if not raw_address:
        raise Exception("Missing required field: searchTerm")

    formatted_address = get_formatted_address(raw_address=raw_address)

    return formatted_address
