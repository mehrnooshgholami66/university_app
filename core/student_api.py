import requests
from core.config import BASE_SERVER

def api_get_professors():
    resp = requests.get(f"{BASE_SERVER}/api/auth/professors/")
    resp.raise_for_status()
    return resp.json()

def api_get_documents(professor_id):
    resp = requests.get(
        f"{BASE_SERVER}/api/documents/professor/{professor_id}/"
    )
    resp.raise_for_status()
    return resp.json()

# core/api/student_api.py

def api_get_documents_by_professor(professor_id):
    resp = requests.get(
        f"{BASE_SERVER}/api/documents/professor/{professor_id}/"
    )
    resp.raise_for_status()
    return resp.json()

