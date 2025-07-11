import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

def get_cursor():
    conn = pyodbc.connect(
        'Driver={SQL Server};'
        f'Server={os.getenv("DB_SERVER")};'
        f'Database={os.getenv("DB_NAME")};'
        'Trusted_Connection=yes;'
    )
    return conn.cursor()
