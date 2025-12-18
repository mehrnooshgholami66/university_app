from pathlib import Path
# ریشه پروژه
BASE_DIR = Path(__file__).resolve().parent.parent

APP_NAME = "University Management System"
DEBUG = True

DB_ENGINE = "sqlite"  # sqlite | mysql

DATABASES = {
    "sqlite": {
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "mysql": {
        "NAME": "university_db",
        "USER": "root",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": 3306,
    }
}


def get_app_name():
    return APP_NAME


def is_debug():
    return DEBUG


def get_db_engine():
    return DB_ENGINE


def get_database_config():
    return DATABASES[DB_ENGINE]

