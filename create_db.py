from connect import create_connection, database
from sql_query import create_table


sql_create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    fullname VARCHAR(100),
    email VARCHAR(100) UNIQUE
);
"""

sql_create_status_table = """
CREATE TABLE IF NOT EXISTS status (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) UNIQUE
);
"""

sql_create_tasks_table = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    status_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (status_id) REFERENCES status (id)
    ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (id)
    ON DELETE CASCADE
);
"""

with create_connection(database) as conn:
    if conn is not None:
        # create tables
        create_table(conn, sql_create_users_table)
        create_table(conn, sql_create_status_table)
        create_table(conn, sql_create_tasks_table)

    else:
        print("Error! cannot create the database connection.")
