from sqlite3 import Error
from connect import create_connection, database
from fakeData import generate_fake_data

SQL_USER = "INSERT INTO users(fullname,email) VALUES(?,?);"
SQL_STATUS = "INSERT INTO status(name) VALUES(?);"
SQL_TASK = "INSERT INTO tasks(title,description,status_id,user_id) VALUES(?,?,?,?);"

status, users, tasks = generate_fake_data(5, 10, 3)


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
        insert_data(conn, SQL_STATUS, status)
        insert_data(conn, SQL_USER, users)
        insert_data(conn, SQL_TASK, tasks)

        print("all complete")
