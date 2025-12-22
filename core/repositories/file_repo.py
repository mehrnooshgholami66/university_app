from core.database import get_connection
from core.config import APP_ENV, API_URL_LOGIN, API_DOCUMENT_UPLOAD
import requests

def create_document(title, file_type, professor_id, file_name, file_path):
    if APP_ENV == "dev":
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO documents (title, file_type, professor_id, file_name, file_path) VALUES (?, ?, ?, ?, ?)",
            (title, file_type, professor_id, file_name, file_path)
        )
        conn.commit()
        conn.close()
    else:
        pass

