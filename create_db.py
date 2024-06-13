from connect import create_connection, database
from sql_query import create_table


def create_db():

    with open("tables.sql", "r") as f:
        sql = f.read()

    with create_connection(database) as conn:
        if conn is not None:
            create_table(conn, sql)

        else:
            print("Error! cannot create the database connection.")


if __name__ == "__main__":
    create_db()
