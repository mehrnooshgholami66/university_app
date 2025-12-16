from university_app import settings

def get_app_name():
    return settings.APP_NAME

def is_debug():
    return settings.DEBUG

def get_db_engine():
    return settings.DB_ENGINE
