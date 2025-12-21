from core.config import get_db_engine, get_database_config
import sqlite3

try:
    import mysql.connector
except ImportError:
    mysql = None


def get_connection():
    engine = get_db_engine()
    config = get_database_config()

    if engine == "sqlite":
        return sqlite3.connect(
            config["NAME"],
            check_same_thread=False
        )
    elif engine == "mysql":
        if mysql is None:
            raise ImportError("mysql-connector-python is not installed")
        return mysql.connector.connect(
            host=config["HOST"],
            user=config["USER"],
            password=config["PASSWORD"],
            database=config["NAME"],
            port=config["PORT"],
            autocommit=True
        )
    else:
        raise ValueError(f"Unsupported DB_ENGINE: {engine}")


def placeholder():
    """ باز می‌گرداند placeholder مناسب driver """
    engine = get_db_engine()
    if engine == "sqlite":
        return "?"
    elif engine == "mysql":
        return "%s"
    else:
        raise ValueError(f"Unsupported DB_ENGINE: {engine}")


