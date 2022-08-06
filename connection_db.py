import psycopg2
from psycopg2 import pool
import commands_init_tables as commands


def init_connection_pool():
    return psycopg2.pool.SimpleConnectionPool(1, 20, user="postgres",
                                              password="admin",
                                              host="localhost",
                                              port="5432",
                                              database="postgres")


def create_tables(postgres_pool: psycopg2.pool.SimpleConnectionPool):
    conn = None
    try:
        conn = postgres_pool.getconn()
        cur = conn.cursor()
        for command in commands.commands_init_tables:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
