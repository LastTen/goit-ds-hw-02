from sqlite3 import Error
from connect import create_connection, database

sql_user = "INSERT INTO users(fullname,email) VALUES(?,?);"
sql_status = "INSERT INTO status(name) VALUES(?);"
sql_task = "INSERT INTO tasks(title,description,status_id,user_id) VALUES(?,?,?,?);"


def insert_data(conn, sql, data):
    cur = conn.cursor()
    try:
        cur.executemany(sql, data)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return "create"


if __name__ == "__main__":
    with create_connection(database) as conn:
        # Statuses
        status = [("new",), ("in progress",), ("completed",)]
        # Users
        users = [
            ("John Smit", "smith@gmail.com"),
            ("John Brown", "brown@gmail.com"),
            ("John Black", "black@gmail.com"),
        ]
        # Task
        task = (
            ("test1", "some desc", 1, 1),
            ("test2", "some desc", 2, 3),
            ("test3", "some desc", 2, 2),
            ("test4", "some desc", 3, 1),
            ("test5", "some desc", 1, 2),
        )

        insert_data(conn, sql_status, status)
        insert_data(conn, sql_user, users)
        insert_data(conn, sql_task, task)

        print("all complete")
