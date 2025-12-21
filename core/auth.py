from core.database import get_connection
from core.security import verify_password


def authenticate(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    #  اول فقط با username رکورد رو می‌گیریم
    cursor.execute("""
        SELECT id, password, role, is_active
        FROM users
        WHERE username = ?
    """, (username,))

    row = cursor.fetchone()
    conn.close()

    if not row:
        return None  # یوزر وجود ندارد

    user_id, hashed_password, role, is_active = row

    #  مقایسه پسورد واقعی با هش
    if not verify_password(password, hashed_password):
        return None  # پسورد اشتباه
    user = user_id, role, is_active
    return user


