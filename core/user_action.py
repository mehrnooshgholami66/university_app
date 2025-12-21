from core.database import get_connection, placeholder

ph = placeholder()


def create_user_role(username, password, role):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO users (username, password, role) VALUES ({ph}, {ph}, {ph})",
        (username, password, role)
    )
    conn.commit()
    conn.close()


def block_user(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"UPDATE users SET is_active = 0 WHERE username={ph}",
        (username,)
    )
    conn.commit()
    conn.close()


def unblock_user(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"UPDATE users SET is_active = 1 WHERE username={ph}",
        (username,)
    )
    conn.commit()
    conn.close()


def delete_user(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"DELETE FROM users WHERE username={ph}",
        (username,)
    )
    conn.commit()
    conn.close()


def exists_user(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT COUNT(*) FROM users WHERE username={ph}",
        (username,)
    )
    count = cursor.fetchone()[0]
    conn.close()
    return count > 0


def is_block(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT is_active FROM users WHERE username={ph}",
        (username,)
    )
    is_active = cursor.fetchone()[0]
    conn.close()
    return not is_active


def is_unblock(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT is_active FROM users WHERE username={ph}",
        (username,)
    )
    is_active = cursor.fetchone()[0]
    conn.close()
    return is_active
