from core.database import get_connection, placeholder

ph = placeholder()  # بازگرداندن placeholder مناسب

def get_professors():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, username
        FROM users
        WHERE role = 'professor' AND is_active = 1
    """)
    rows = cur.fetchall()
    conn.close()
    return rows


def get_documents_by_professor(professor_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"""
        SELECT title, file_type, file_name, file_path
        FROM documents
        WHERE professor_id = {ph}
    """, (professor_id,))
    rows = cur.fetchall()
    conn.close()
    return rows

