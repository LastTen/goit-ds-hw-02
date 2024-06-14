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


def insert_data(sql, data):
    """
    This function is used to insert multiple records into a database table.

    Parameters:
    sql (str): The SQL INSERT statement with placeholders for the data.
    data (list of tuples): A list of tuples, where each tuple represents a record to be inserted.

    Returns:
    str: Returns 'ok' if the data is successfully inserted, otherwise it prints the error message.
    """
    with create_connection(database) as conn:
        if conn is not None:
            cur = conn.cursor()
            try:
                cur.executemany(sql, data)
                conn.commit()
                return "ok"
            except Error as e:
                print(e)
        else:
            print("Error! cannot create the database connection.")


def get_info_from_db(sql, params=[]):
    """This function retrieves data from a database using a given SQL query and parameters.

    Parameters:
    sql (str): The SQL query to be executed.
    params (list, optional): A list of parameters to be used in the SQL query. Defaults to an empty list.

    Returns:
    list: A list of tuples, where each tuple represents a record fetched from the database.
    """
    with create_connection(database) as con:
        if con is not None:
            cur = con.cursor()
            cur.execute(sql, params)

            return cur.fetchall()
        else:
            print("Error! cannot create the database connection.")


def delete_info_from_db(sql, data):
    """This function deletes records from a database using a given SQL query and data.

    Parameters:
    sql (str): The SQL DELETE statement with placeholders for the data.
    data (list of tuples): A list of tuples, where each tuple represents a record to be deleted.

    Returns:
    str: Returns 'deleted successfully' if the data is successfully deleted, otherwise it prints the error message.
    """
    with create_connection(database) as conn:
        if conn is not None:
            cur = conn.cursor()
            try:
                cur.executemany(sql, data)
                conn.commit()
                return "deleted successfully"
            except Error as e:
                print(e)
        else:
            print("Error!")


def update_data_from_db(sql, data):
    """This function updates records in a database using a given SQL query and data.

    Parameters:
    sql (str): The SQL UPDATE statement with placeholders for the data.
    data (list of tuples): A list of tuples, where each tuple represents a record to be updated.

    Returns:
    str: Returns 'updated successfully' if the data is successfully updated, otherwise it prints the error message.
    """
    with create_connection(database) as conn:
        if conn is not None:
            cur = conn.cursor()
            try:
                cur.executemany(sql, data)
                conn.commit()
                return "updated successfully"
            except Error as e:
                print(e)
        else:
            print("Error!")
