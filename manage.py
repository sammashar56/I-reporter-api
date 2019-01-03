# system libs
import os

# installed libs
import psycopg2 as p

# local modules
from query import queries

class TableCreation:
    """creation of the tables"""
    def __init__(self):
        self.conn = p.connect(os.getenv("DATABASE_URL"))
        self.cursor = self.conn.cursor()
    
    def create_table(self):
        """loop through query creating the tables"""
        for q in queries:
            self.cursor.execute(q)
        self.conn.commit()
        self.cursor.close()

    def kill(self):
        """killing the tables"""
        user = "DROP TABLE IF EXISTS users CASCADE"
        incident = "DROP TABLE IF EXISTS incidents CASCADE"
        tear_tables = [user, incident]
        for tear in tear_tables:
            self.cursor.execute(tear)
        self.conn.commit()
        self.cursor.close()

if __name__== '__main__':
    TableCreation().kill()
    TableCreation().create_table()