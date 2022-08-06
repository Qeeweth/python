import uuid
import psycopg2
from psycopg2 import pool

SQL_SAVE = """
INSERT INTO public.tag(id, tag)
VALUES ('{tag_id}', '{tag}');
INSERT INTO public.info(id, description)
VALUES ('{info_id}', '{info}');
INSERT INTO public.tag_info_merge(id, tag_id, info_id)
VALUES ('{merge_id}', '{tag_id}', '{info_id}');
"""


def save(postgres_pool: psycopg2.pool.SimpleConnectionPool, tag, info):
    conn = None
    try:
        conn = postgres_pool.getconn()
        cur = conn.cursor()
        cur.execute(SQL_SAVE.format(tag_id=uuid.uuid4(), info_id=uuid.uuid4(), merge_id=uuid.uuid4(), tag=tag, info=info))
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
