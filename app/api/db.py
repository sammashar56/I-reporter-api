#system libraries
import os

#installed libs
import psycopg2


class Database:
    """database connection"""
    def __init__(self):

        try:
            self.conn = psycopg2.connect(os.getenv("DATABASE_URL"))
            self.cursor = self.conn.cursor()
            print('connected to db')
        except:
            print('cannot connect to database')
        
    def commiting(self):
        """commit to database"""
        self.conn.commit()

    def close_db(self):
        """closing the connection""" 
        self.cursor.close()