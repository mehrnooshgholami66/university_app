import os
from pathlib import Path

# ----------------------
# ریشه پروژه
# ----------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------
# محیط پروژه: dev یا prod
# ----------------------
APP_ENV = "dev"
# or "prod" for deployment and production

# ----------------------
# اطلاعات برنامه
# ----------------------
APP_NAME = "University Management System"
DEBUG = APP_ENV == "dev"

# ----------------------
# تنظیمات دیتابیس
# ----------------------
DATABASES = {
    "dev": {  # توسعه → SQLite
        "ENGINE": "sqlite",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "prod": {  # پروداکشن → MySQL
        "ENGINE": "mysql",
        "NAME": "university_db",
        "USER": "root",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": 3306,
    }
}

# ----------------------
# توابع کمکی
# ----------------------
def get_app_name():
    return APP_NAME

def is_debug():
    return DEBUG

def get_db_engine():
    return DATABASES[APP_ENV]["ENGINE"]

def get_database_config():
    return DATABASES[APP_ENV]

