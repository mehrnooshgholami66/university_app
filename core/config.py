import os
from pathlib import Path

# ----------------------
# ریشه پروژه
# ----------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------
# محیط پروژه: "dev" یا "prod"
# ----------------------
APP_ENV = "dev"

# ----------------------
# اطلاعات سرور / API
# ----------------------
BASE_SERVER = "http://127.0.0.1:8000"
API_URL_LOGIN = f"{BASE_SERVER}/api/auth/login/"
API_CREATE_USER = f"{BASE_SERVER}/api/auth/create-user/"
API_DOCUMENT_UPLOAD = f"{BASE_SERVER}/api/documents/upload/"
API_PROFESSORS_VIEW = f"{BASE_SERVER}/api/auth/professors/"
def get_professor_documents_api(professor_id):
    return f"{BASE_SERVER}/api/documents/professor/{professor_id}/"
def block_user_api(username):
    return f"{BASE_SERVER}/api/auth/block-user/{username}/"
def unblock_user_api(username):
    return f"{BASE_SERVER}/api/auth/unblock-user/{username}/"
def delete_user_api(username):
    return f"{BASE_SERVER}/api/auth/delete-user/{username}/"

# ----------------------
# اطلاعات برنامه
# ----------------------
APP_NAME = "University Management System"

# ----------------------
# تنظیمات دیتابیس
# فقط برای محیط توسعه نیاز است (prod از API استفاده می‌کند)
# ----------------------
DATABASES = {
    "dev": {  # توسعه → SQLite
        "ENGINE": "sqlite",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}

# ----------------------
# توابع کمکی
# ----------------------
def get_app_name():
    return APP_NAME

def get_db_engine():
    """فقط در dev استفاده می‌شود"""
    return "sqlite"

def get_database_config():
    """فقط در dev استفاده می‌شود"""
    return DATABASES[APP_ENV]


