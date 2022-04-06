from dotenv import load_dotenv
from os import getenv

import psycopg2

load_dotenv()

configs = {
    "host": getenv('HOST'),
    "database": getenv('DATABASE'),
    "user": getenv("DATA_USER"),
    "password": getenv("DATA_PASSWORD"),
}

def conn_cur():
    conn = psycopg2.connect(**configs)
    cur = conn.cursor()

    return conn, cur

def commit_and_close(conn,cur):
    conn.commit()
    cur.close()
    conn.close()
