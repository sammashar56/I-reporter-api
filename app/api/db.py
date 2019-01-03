#system libraries
import os

#installed libs
import psycopg2
#use psycopg2.extra to get the data as a dictionary 
import psycopg2.extras

class Database:
    """database connection"""
    def __init__(self):

        try:
            self.conn = psycopg2.connect( os.getenv("DATABASE_URL"))
            self.cursor = self.conn.cursor(cursor_factory= psycopg2.extras.DictCursor)
            #print('connected to db')
        except:
            print('cannot connect to database')
        
    def commiting(self):
        """commit to database"""
        self.conn.commit()

    def close_db(self):
        """closing the connection""" 
        self.cursor.close() 