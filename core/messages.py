from PyQt5.QtWidgets import QMessageBox


class MessageBox:

    @staticmethod
    def success(parent, text, title="Success", on_ok=None):
        msg = QMessageBox(parent)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(title)
        msg.setText(text)
        if msg.exec_() == QMessageBox.Ok:
            if on_ok:
                on_ok()

    @staticmethod
    def error(parent, text, title="error", on_ok=None):
        msg = QMessageBox(parent)
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(text)
        if msg.exec_() == QMessageBox.Ok:
            if on_ok:
                on_ok()

    @staticmethod
    def warning(parent, text, title="warning", on_ok=None):
        msg = QMessageBox(parent)
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle(title)
        msg.setText(text)
        if msg.exec_() == QMessageBox.Ok:
            if on_ok:
                on_ok()
        
        
        



