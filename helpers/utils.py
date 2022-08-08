import json


def get_from_query_params(event: dict, param: str):
    query = None
    query_params = event.get("queryStringParameters", None)
    if query_params is not None:
        query = query_params.get(param, None)
    return query


def get_path_param_from_event(event: dict, path_param: str):
    param = None
    path_params = event.get("pathParameters", None)
    if path_params is not None:
        param = path_params.get(path_param, None)

    return param


def get_body_from_event(event: dict):
    body = event.get("body")
    parsed_body = json.loads(body)
    return parsed_body
