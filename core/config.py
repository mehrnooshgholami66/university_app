from core import constants
from settings import APP_NAME, DEBUG, DB_ENGINE, DATABASES

def get_app_name():
    return APP_NAME

def is_debug():
    return DEBUG

def get_db_engine():
    return DB_ENGINE

def get_database_config():
    return DATABASES[DB_ENGINE]

