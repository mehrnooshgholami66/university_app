import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from core.user_action import create_user_role, delete_user, block_user, unblock_user, exist_user