from sqlite3 import Error
from dotenv import load_dotenv
import os
import pyodbc
load_dotenv()

class Database:
    def getDB():
        conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
        'Server='+os.getenv('SERVER_NAME')+';'
        'Database='+os.getenv('DB_NAME')+';'
        'UID='+os.getenv('USER_NAME')+';'
        'PWD='+os.getenv('USER_PASSWORD')+'')
        return conn