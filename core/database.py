from core.config import get_db_engine, get_database_config
import sqlite3


def get_connection():
    engine = get_db_engine()
    config = get_database_config()

    if engine == "sqlite":
        return sqlite3.connect(config["NAME"])

