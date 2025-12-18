from core.database import get_connection
def authenticate(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, role, is_active
        FROM users
        WHERE username=? AND password=?
    """, (username, password))

    user = cursor.fetchone()
    conn.close()

    return user  # None یا (id, role, is_active)

