from app.api.db import Database
from werkzeug.security import generate_password_hash, check_password_hash

class ModelDb(Database):
    """model database"""
    def __init__(self):
        super().__init__()

    def add_user(self, data):
        """insert a user in the db"""
        hashed_password = generate_password_hash(data['password'])
        self.cursor.execute(
            """ INSERT INTO users(firstname, lastname, email, 
            phone_no, is_admin, password) 
            VALUES('%s','%s','%s','%s','%s','%s')
        """%(data['firstname'], 
        data['lastname'], data['email'], data['phone_no'], data['is_admin'],hashed_password))
        self.commiting()
        return data

