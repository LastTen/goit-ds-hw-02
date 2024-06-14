import sqlite3
from contextlib import contextmanager

database = "./sqlite_project.db"


@contextmanager
def create_connection(db_file):
    """
    Create a database connection to a SQLite database.

    Parameters:
    db_file (str): The path to the SQLite database file.

    Yields:
    sqlite3.Connection: A connection object to the SQLite database.

    Note:
    The connection is automatically rolled back in case of any exception.
    After the context block is exited, the connection is closed.
    """
    conn = sqlite3.connect(db_file)
    yield conn
    conn.rollback()
    conn.close()
