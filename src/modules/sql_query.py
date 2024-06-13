from sqlite3 import Error
from src.connect import create_connection, database


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.executescript(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


def insert_data(conn, sql, data):
    cur = conn.cursor()
    try:
        cur.executemany(sql, data)
        conn.commit()
    except Error as e:
        print(e)

    return "ok"


def execute_query(sql, params=[]):
    with create_connection(database) as con:
        cur = con.cursor()
        cur.execute(sql, params)

        return cur.fetchall()
