from sqlite3 import Error
from connect import create_connection, database


def create_user(conn, project):
    sql = """
    INSERT INTO users(fullname,email) VALUES(?,?);
    """
    cur = conn.cursor()
    try:
        cur.execute(sql, project)
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
        cur.execute(sql, task)
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
        cur.execute(sql, task)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cur.close()

    return cur.lastrowid


if __name__ == "__main__":
    with create_connection(database) as conn:
        # Statuses
        status_new = ("new",)
        status_progress = ("in progress",)
        status_completed = ("completed",)
        # create status
        create_status(conn, status_new)
        create_status(conn, status_progress)
        create_status(conn, status_completed)

        # Users
        user1 = ("John Smit", "smith@gmail.com")
        user2 = ("John Brown", "brown@gmail.com")
        user3 = ("John Black", "black@gmail.com")
        # create users
        create_user(conn, user1)
        create_user(conn, user2)
        create_user(conn, user3)

        # Task
        task_1 = ("test1", "some desc", 1, 1)
        task_2 = ("test2", "some desc", 2, 3)
        task_3 = ("test3", "some desc", 2, 2)
        task_4 = ("test4", "some desc", 3, 1)
        task_5 = ("test5", "some desc", 1, 2)
        # create task
        create_task(conn, task_1)
        create_task(conn, task_2)
        create_task(conn, task_3)
        create_task(conn, task_4)
        create_task(conn, task_5)

        print("all complete")
