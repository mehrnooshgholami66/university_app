from core.database import get_connection, placeholder

ph = placeholder()

def create_document(title, file_type, professor_id, file_name, file_path):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO documents (title, file_type, professor_id, file_name, file_path) VALUES ({ph}, {ph}, {ph}, {ph}, {ph})",
        (title, file_type, professor_id, file_name, file_path)
    )
    conn.commit()
    conn.close()

