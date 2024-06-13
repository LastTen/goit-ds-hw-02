from sqlite3 import Error
from connect import create_connection, database


def create_user(conn, project):
    sql = """
    INSERT INTO users(fullname,email) VALUES(?,?);
    """
    cur = conn.cursor()
    try:
        cur.executemany(sql, project)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid


def create_status(conn, task):
    sql = """
    INSERT INTO status(name) VALUES(?);
    """
    cur = conn.cursor()
    try:
        cur.executemany(sql, task)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid


def create_task(conn, task):
    sql = """
    INSERT INTO tasks(title,description,status_id,user_id) VALUES(?,?,?,?);
    """
    cur = conn.cursor()
    try:
        cur.executemany(sql, task)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid


if __name__ == "__main__":
    with create_connection(database) as conn:
        # Statuses
        status = [("new",), ("in progress",), ("completed",)]
        create_status(conn, status)
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
        create_status(conn, status)
        create_user(conn, users)
        create_task(conn, task)

        print("all complete")
