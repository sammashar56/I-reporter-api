#standard lib
import os
import datetime as dt


import jwt

from werkzeug.exceptions import Unauthorized, BadRequest, NotFound

#local imports
from app.api.v2.model.user import ModelUser

model = ModelUser()

key = os.getenv("SECRET_KEY")

class Token:
    """ encoding and decoding token"""
    def __init__ (self):
        pass

    @staticmethod
    def encode_auth_token(user_id):
        """generate token"""
        payload = {
            'exp': dt.datetime.utcnow() + dt.timedelta(minutes=30),
            'iat': dt.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            key,
            algorithm='HS256'
        )

    @staticmethod
    def decode_auth_token(auth_token):
        """decodes tokens"""
        try:
            payload = jwt.decode(auth_token, key)
        except jwt.ExpiredSignatureError:
            raise Unauthorized ('Your session is expired')
        except jwt.InvalidTokenEror:
            raise Unauthorized ('Your session is not recognized login to get a valid one')
        
        return payload['sub']
            


  