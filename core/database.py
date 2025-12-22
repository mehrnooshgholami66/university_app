from core.config import get_db_engine, get_database_config
import sqlite3

def get_connection():
    """
    اتصال به دیتابیس محلی.
    فقط در محیط dev فعال است.
    در prod از API استفاده می‌شود و اتصال دیتابیس غیر فعال است.
    """
    engine = get_db_engine()
    config = get_database_config()

    if engine == "sqlite":
        return sqlite3.connect(
            config["NAME"],
            check_same_thread=False
        )




