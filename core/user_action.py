from core.database import get_connection
from core.config import APP_ENV, API_CREATE_USER
from core.security import hash_password
import requests

def create_user_role(username, password, role):
    if APP_ENV == "dev":
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, hash_password(password), role)
        )
        conn.commit()
        conn.close()
    elif APP_ENV == "prod":
        response = requests.post(
            API_CREATE_USER,
            json={"username": username, "password": password, "role": role}
        )
        if response.status_code != 201:
            raise Exception("Failed to create user in production environment")


def block_user(username):
    if APP_ENV == "dev":
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE users SET is_active = 0 WHERE username=?",
            (username,)
        )
        conn.commit()
        conn.close()
    else:
        pass


def unblock_user(username):
    if APP_ENV == "dev":
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE users SET is_active = 1 WHERE username=?",
            (username,)
        )
        conn.commit()
        conn.close()
    else:
        pass


def delete_user(username):
    if APP_ENV == "dev":
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            f"DELETE FROM users WHERE username=?",
            (username,)
        )
        conn.commit()
        conn.close()
    else:
        pass


def exists_user(username):
    if APP_ENV == "dev":
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT COUNT(*) FROM users WHERE username=?",
            (username,)
        )
        count = cursor.fetchone()[0]
        conn.close()
        return count > 0
    else:
        pass


def is_block(username):
    if APP_ENV == "dev":
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT is_active FROM users WHERE username=?",
            (username,)
        )
        is_active = cursor.fetchone()[0]
        conn.close()
        return not is_active
    else:
        pass


def is_unblock(username):
    if APP_ENV == "dev":
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT is_active FROM users WHERE username=?",
            (username,)
        )
        is_active = cursor.fetchone()[0]
        conn.close()
        return is_active
    else:
        pass
