from src.connect import create_connection, database
from src.modules.sql_query import create_table


def create_db():
    """The function reads the SQL commands from a file named 'tables.sql'.
    It then creates a connection to the database using the 'create_connection' function.
    If the connection is successful, it executes the SQL commands using the 'create_table' function.
    If the connection fails, it prints an error message."""

    with open("tables.sql", "r") as f:
        sql = f.read()

    with create_connection(database) as conn:
        if conn is not None:
            create_table(conn, sql)

        else:
            print("Error! cannot create the database connection.")


if __name__ == "__main__":
    create_db()
