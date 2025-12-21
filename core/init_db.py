from core.database import get_connection
from core.schema import USER_TABLE_SQL, DOCUMENT_TABLE_SQL


def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(USER_TABLE_SQL)
    cursor.execute(DOCUMENT_TABLE_SQL)
    conn.commit()
    conn.close()
