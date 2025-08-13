import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    print("Connection successful!")
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
