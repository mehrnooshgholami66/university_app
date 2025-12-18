import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from PyQt5.QtWidgets import QMessageBox


class MessageBox:

    @staticmethod
    def success(parent, text, title="success full"):
        QMessageBox.information(parent, title, text)

    @staticmethod
    def warning(parent, text, title="warning"):
        QMessageBox.warning(parent, title, text)
        
    @staticmethod
    def error(parent, text, title="error"):
        QMessageBox.critical(parent, title, text)

    @staticmethod
    def info(parent, text, title="info"):
        QMessageBox.information(parent, title, text)

        MessageBox.success()
        
        
        



