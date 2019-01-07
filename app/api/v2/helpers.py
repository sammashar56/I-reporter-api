from app.api.v2.token import Token as token
from app.api.v2.model.user import ModelUser

from flask import request

user_model = ModelUser()

class Helper:
    def __init__(self):
        pass

    @staticmethod
    def default_user():
        """default user"""
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[0]
        else:
            auth_token = ''
        if auth_token:
            response = token.decode_auth_token(auth_token)
            if isinstance(response, str):
                user_credentials = user_model.check_user_id(response)
                print(user_credentials)
                if user_credentials:
                    return user_credentials[0]
