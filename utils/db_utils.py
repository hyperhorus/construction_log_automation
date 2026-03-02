import mysql.connector
from utils.config import Config

class Database:

    def __init__(self):
        self.connection = mysql.connector.connect(**Config.DB_CONFIG)
        self.cursor = self.connection.cursor(dictionary=True)

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def execute_update(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()