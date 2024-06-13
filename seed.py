from src.connect import create_connection, database
from src.modules.fakeData import generate_fake_data
from src.modules.sql_query import insert_data

SQL_USER = "INSERT INTO users(fullname,email) VALUES(?,?);"
SQL_STATUS = "INSERT INTO status(name) VALUES(?);"
SQL_TASK = "INSERT INTO tasks(title,description,status_id,user_id) VALUES(?,?,?,?);"

status = [("new",), ("in progress",), ("completed",)]
users, tasks = generate_fake_data(5, 25, len(status))


with create_connection(database) as conn:
    if conn is not None:
        insert_data(conn, SQL_STATUS, status)
        insert_data(conn, SQL_USER, users)
        insert_data(conn, SQL_TASK, tasks)

    print("all data is filled in")
