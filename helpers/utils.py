import json


def get_from_query_params(event: dict, param: str):
    query = None
    query_params = event.get("queryStringParameters", None)
    if query_params is not None:
        query = query_params.get(param, None)
    return query


def get_body_from_event(event: dict):
    body = event.get("body")
    parsed_body = json.loads(body)
    return parsed_body
