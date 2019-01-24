from app.api.db import Database
from werkzeug.security import generate_password_hash
from werkzeug.exceptions import Forbidden, NotFound

class ModelUser(Database):
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
        #print(data)

    def check_admin1(self,user_id):
        """check for admin"""
        self.cursor.execute("SELECT * FROM users WHERE user_id='%s'" % user_id
        )
        result = self.cursor.fetchone()
        if result:
            if result[5] == True:
                return result
            else:
                raise Forbidden("Admins ONLY access this")
        else:
            raise NotFound("no user of that id")

    def get_user_password(self, email):
        """get a password"""
        self.cursor.execute("SELECT * FROM users WHERE email='%s'" %(email))
        result = self.cursor.fetchone() 
        return result
        
    def check_email(self, email):
        """Check if an email exists """
        self.cursor.execute(
            "SELECT * FROM users WHERE email='%s'" % email
        )
        user = self.cursor.fetchone()
        return user

    def get_all_users(self):
        """get all users"""
        self.cursor.execute("SELECT * FROM users")
        result = self.cursor.fetchall()
        return result

    def check_user_id(self, user_id):
        """get user by id"""
        self.cursor.execute("SELECT * FROM users WHERE user_id='%s'" %user_id)
        result = self.cursor.fetchone()
        return result