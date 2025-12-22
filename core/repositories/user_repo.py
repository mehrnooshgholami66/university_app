from core.database import get_connection
from core.config import APP_ENV, API_URL_LOGIN
import requests

def get_professors():
    if APP_ENV == "dev":
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
    else:
        pass


def get_documents_by_professor(professor_id):
    if APP_ENV == "dev":
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT title, file_type, file_name, file_path
            FROM documents
            WHERE professor_id = ?
        """, (professor_id,))
        rows = cur.fetchall()
        conn.close()
        return rows
    else:
        pass

