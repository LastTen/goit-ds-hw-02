from src.modules.sql_query import execute_query, insert_data


def get_all_user_task(id):
    sql = """
        SELECT title, description, s.name as status FROM tasks as t
        join status s on s.id = t.status_id
        WHERE t.user_id = ?
        """

    return execute_query(sql, [str(id)])


def get_all_task_by_status(status):
    sql = """
        SELECT title, description FROM tasks as t
        join status s on s.id = t.status_id
        WHERE s.name = ?
        """
    return execute_query(sql, [status])


# def update_task_status(status, task_id):
#     sql = """
#         UPDATE tasks as t
#         SET status_id = (SELECT s.id FROM status as s WHERE s.name = ?)
#         WHERE t.id = ?
#         """
#     execute_query(sql, [status, str(task_id)])
#     return f"status task with id {task_id} updated to {status}"


def add_task(title, deck, user_id):
    sql = """
        INSERT INTO tasks(title, description, status_id, user_id)
        VALUES(?, ?, 1, ?)
        """
    insert_data(sql, [(title, deck, str(user_id))])


def get_user_wo_task():
    sql = """
        SELECT u.fullname, u.email FROM users as u
        WHERE u.id NOT IN (SELECT t.user_id FROM tasks as t)
        """
    return execute_query(sql)


def get_no_complete_task():
    sql = """
        SELECT t.title, t.description FROM tasks t
        where t.status_id IS NOT 3
        """
    return execute_query(sql)


# sql = """
#     DELETE FROM tasks
#     where id = ?
#     """


def get_user_with_email(email):
    sql = """
        SELECT u.fullname, u.email FROM users u
        WHERE u.email LIKE ?
        """
    return execute_query(sql, [f"%{email}%"])


# def update_user_name(new_fullname, id):
#     sql = """
#         UPDATE users
#         SET fullname = ?
#         WHERE id = ?
#     """
#     execute_query(sql, [f"'{new_fullname}'", str(id)])


def get_count_task_each_status():
    sql = """
        SELECT s.name as status, COUNT(t.id) as count_task FROM tasks as t
        JOIN status as s ON s.id = t.status_id
        GROUP BY t.status_id
        """
    return execute_query(sql)


def get_tasks_by_user_email_domain(domain):
    sql = """
        SELECT title, description, s.name as status FROM tasks as t
        JOIN status s on s.id = t.status_id
        JOIN users u on u.id = t.user_id
        WHERE u.email LIKE ?
        """
    return execute_query(sql, [f"%@{domain}"])


def get_tasks_wo_description():
    sql = """
        SELECT t.title FROM tasks t
        WHERE t.description ISNULL
        """
    return execute_query(sql)


def get_tasks_in_progress():
    sql = """
        SELECT u.fullname, t.title, t.description FROM users u
        JOIN tasks t ON t.user_id = u.id
        JOIN status s ON s.id = t.status_id AND s.name = 'in progress'
        """
    return execute_query(sql)


def get_count_task_for_each_user():
    sql = """
        SELECT u.fullname as user, COUNT(t.id) as count_task FROM users as u
        LEFT JOIN tasks t ON t.user_id = u.id
        GROUP BY u.id
        """
    return execute_query(sql)


if __name__ == "__main__":
    # print(get_all_user_task(1))
    # print(get_all_task_by_status("new"))
    # print(update_task_status("new", 2))
    # print(get_user_wo_task())
    # print(get_no_complete_task())
    # print(get_user_with_email("77"))
    # print(get_count_task_each_status())
    # print(get_tasks_by_user_email_domain("example.net"))
    # print(get_tasks_wo_description())
    # print(get_tasks_in_progress())
    # print(get_count_task_for_each_user())

    add_task("new_task1", "bdb", 1)
