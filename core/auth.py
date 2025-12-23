from core.database import get_connection
from core.security import verify_password
from core.config import APP_ENV, API_URL_LOGIN
import requests

def authenticate(username, password):
    if APP_ENV == "dev":
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT id, password, role, is_active FROM users WHERE username=?",
            (username,)
        )
        row = cursor.fetchone()
        conn.close()

        if not row:
            return None  # یوزر وجود ندارد

        user_id, hashed_password, role, is_active = row

        if not verify_password(password, hashed_password):
            return None  # پسورد اشتباه
        user = user_id, role, is_active, "__no_token__"
        return user
    elif APP_ENV == "prod":
        response = requests.post(
            API_URL_LOGIN,
            json={"username": username, "password": password}
        )
        if response.status_code != 200:
            return None  # خطا در احراز هویت
        data = response.json()
        user = data.get("user_id"), data.get("role"), data.get("is_active"), data.get("token")
        return user

