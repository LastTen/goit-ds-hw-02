from sqlite3 import Error


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
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
    finally:
        cur.close()

    return "ok"
