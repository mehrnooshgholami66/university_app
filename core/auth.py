from core.database import get_connection, placeholder
from core.security import verify_password

ph = placeholder()


def authenticate(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT id, password, role, is_active FROM users WHERE username={ph}",
        (username,)
    )
    row = cursor.fetchone()
    conn.close()

    if not row:
        return None  # یوزر وجود ندارد

    user_id, hashed_password, role, is_active = row

    if not verify_password(password, hashed_password):
        return None  # پسورد اشتباه
    user = user_id, role, is_active
    return user
