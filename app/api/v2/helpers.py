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
                # print(user_credentials[0])
                if user_credentials:
                    return user_credentials[0]
    @staticmethod
    def user_serializer(data):
        data = {
            "id":data[0],
            "fisrtname":data[1],
            "lastname":data[2],
            "email":data[3],
            "phoneNumber":data[4],
            "is_admin":data[5],
            "password":data[6]
        }
        return data

    @staticmethod
    def incident_serializer(incident):
        incident = {
            "id":incident[0],
            "type_of_incident":incident[1],
            "title":incident[2],
            "comment":incident[3],
            "description":incident[4],
            "location":incident[5],
            "time":incident[6],
            "user_id":incident[7]
        }
        return incident

