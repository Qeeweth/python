import psycopg2
from psycopg2 import pool

SELECT_BY_TAG = """
select i.* 
from public.info i left join public.tag_info_merge ti 
on i.id = ti.info_id
left join public.tag t on ti.tag_id = t.id
where t.tag = '{tag}';
"""


def get_by_tag(postgres_pool: psycopg2.pool.SimpleConnectionPool, tag):
    conn = None
    try:
        conn = postgres_pool.getconn()
        cur = conn.cursor()
        cur.execute(SELECT_BY_TAG.format(tag=tag))
        info = cur.fetchmany(10)
        print("Displaying rows from mobile table")
        cur.close()
        return info
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


