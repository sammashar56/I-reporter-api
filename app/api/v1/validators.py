import re
from werkzeug.exceptions import BadRequest, NotFound

"""validation for valid input"""

class Validators():
    """contains methods that validate various criteria"""
    def __init__(self):
        pass
        
    def return_message_on_empty_field(self, string):
        """should return a string on an empty list"""
        if not isinstance(string, str):
            return 'field should be a string'

    def check_id_valid(self, id):
        """checks the validity of an id"""
        if id < 0:
            return 'invalid id'
        elif not isinstance(id, int):
            return 'provide an int id'
        else:
            return id

    def check_email(self, email):
        """ Check email validity """
        if not re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
            email):
                raise BadRequest("Please provide a valid email")
        return email

    def check_password(self, password):
        """ Check password length """
        if len(password) < 6:
            raise BadRequest("Password is too short, minimum is 6 characters")
        elif len(password) > 12:
            raise BadRequest("Password is too long, maximum is 12 characters")
        
        return password