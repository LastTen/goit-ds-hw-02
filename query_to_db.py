from sqlite3 import Error
from src.connect import create_connection, database
from src.modules.sql_query import execute_query


sql = """
    SELECT title, description, s.name as status FROM tasks as t
    join status s on s.id = t.status_id
    WHERE t.user_id = ?
    """


sql = """
    SELECT title, description FROM tasks as t
    join status s on s.id = t.status_id
    WHERE s.name = ?
    """


sql = """
    UPDATE tasks as t
    SET status_id = (SELECT s.id FROM status as s WHERE s.name = ?)
    WHERE t.id = ?
    """


sql = """
    INSERT INTO tasks(title, description, status_id, user_id)
    VALUES(?, ?, 1, ?)
    """


sql = """
    SELECT u.fullname, u.email FROM users as u 
    WHERE u.id NOT IN (SELECT t.user_id FROM tasks as t)
    """


sql = """
    SELECT t.title, t.description FROM tasks t
    where t.status_id IS NOT 3
    """


sql = """
    DELETE FROM tasks 
    where id = ?
    """


sql = """
    SELECT u.fullname, u.email FROM users u 
    WHERE u.email LIKE ?
    """


sql = """
    UPDATE users 
    SET fullname = ? 
    WHERE id = ?
"""


sql = """
    SELECT s.name as status, COUNT(t.id) as count_task FROM tasks as t
    JOIN status as s ON s.id = t.status_id 
    GROUP BY t.status_id 
    """


sql = """
    SELECT title, description, s.name as status FROM tasks as t
    JOIN status s on s.id = t.status_id
    JOIN users u on u.id = t.user_id 
    WHERE u.email LIKE ?
    """


sql = """
    SELECT t.title FROM tasks t
    WHERE t.description ISNULL 
    """


sql = """
    SELECT u.fullname, t.title, t.description FROM users u
    JOIN tasks t ON t.user_id = u.id 
    JOIN status s ON s.id = t.status_id AND s.name = 'in progress'
    """


sql = """
    SELECT u.fullname as user, COUNT(t.id) as count_task FROM users as u
    LEFT JOIN tasks t ON t.user_id = u.id
    GROUP BY u.id 
    """
