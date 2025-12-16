from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

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