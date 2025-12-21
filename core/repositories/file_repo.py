from core.database import get_connection


def create_document(title, file_type, professor_id, file_name, file_path):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO documents (title, file_type, professor_id, file_name, file_path)
        VALUES (?, ?, ?, ?, ?)
    """, (title, file_type, professor_id, file_name, file_path))

    conn.commit()
    conn.close()
