from functools import wraps
import os

from flask import request, jsonify
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized
import jwt

from app.api.v2.token import Token
from app.api.v2.model.user import ModelUser

user_model = ModelUser()
token = Token()


def check_admin(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[0]
        else:
            auth_token = ''
        if auth_token:
            response = token.decode_auth_token(auth_token)
            if isinstance(response, str):
                user_credentials = user_model.check_admin1(response)
                #print(user_credentials) 
                if not user_credentials:
                    raise Unauthorized("you need to sign up or login")
                return f(*args, **kwargs)
            else:
                raise Unauthorized("Please login")
        else:
            raise Unauthorized("it seems you are not logged in")
    return decorator


def auth_required(f):
    @wraps(f)
    def decorator(*args, **kwargs): 
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[0]
        else:
            auth_token = ''
        if auth_token:
            response = token.decode_auth_token(auth_token)
            if isinstance(response, str):
                user_credentials = user_model.check_user_id(response) # check_admin1(response)
                #print(user_credentials) 
                if not user_credentials:
                    raise Unauthorized("you need to sign up or login")
                return f(*args, **kwargs)
            else:
                raise Unauthorized("Please login")
        else:
            raise Unauthorized("it seems you are not logged in")
    return decorator

            