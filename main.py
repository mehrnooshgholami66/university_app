import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))

from ui_form.login import LoginForm
from PyQt5 import QtWidgets

class Login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = LoginForm()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()