import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        sslmode=os.getenv("DB_SSLMODE"),
        options="-c search_path=catalog"
    )

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    with open("schema.sql", "r") as file:
        cur.execute(file.read())

    conn.commit()
    cur.close()
    conn.close()