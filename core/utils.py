import sys
from pathlib import Path

def resource_path(relative_path: str) -> Path:
    """
    بازگرداندن مسیر درست فایل‌ها برای PyInstaller
    """
    if getattr(sys, 'frozen', False):
        # وقتی exe ساخته شد
        base_path = Path(sys._MEIPASS)
    else:
        # حالت dev
        base_path = Path(__file__).resolve().parent.parent
    return base_path / relative_path
