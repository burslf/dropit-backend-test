# import os
from helpers.load_env import load_environment_variables

load_environment_variables(env="develop", parent_level=0)

# from api_endpoints.api_resolve_address import api_resolve_address
# from utils.geoloc_api import get_formatted_address
# from datetime import datetime
# from db.models.user import User, find_user_by_email, add_user
# from helpers.db_session import get_session

# session = get_session()
# user_collection = session["user"]

# add_new_user = add_user(session=user_collection, email="yoel.developer@gmail.com", phone="088888")
# print(add_new_user)
# find_user = find_user_by_email(session=user_collection, email="yoelzerbib7@gmail.com")

# res = get_formatted_address(raw_address="kambuyyy reiu euu")
# print(res)

# res = api_resolve_address(event={"body": "{\"hello\":\"world\"}"}, context={})
# print(res)
