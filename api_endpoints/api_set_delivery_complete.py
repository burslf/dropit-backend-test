from db.controllers.delivery_controller import get_delivery_by_id, set_delivery_completed
from helpers.custom_log import get_logger
from helpers.db_session import get_session
from helpers.decorators.api_gateway_handler import api_gateway_handler
from helpers.utils import get_path_param_from_event

logger = get_logger()


@api_gateway_handler
def api_set_delivery_complete(event: {}, context: {}):
    delivery_id = get_path_param_from_event(event=event, path_param="delivery_id")

    if not delivery_id:
        raise Exception("Missing required field: delivery_id")

    session = get_session()
    delivery_obj = set_delivery_completed(session=session, delivery_id=delivery_id)

    logger.info(f"Delivery set completed: {delivery_obj}")

    return delivery_obj
