from core.auth import authenticate
from core.messages import MessageBox
from ui_form.admin import AdminForm
from ui_form.professor import ProfessorForm
from ui_form.student import studentFrom
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from core.utils import resource_path


class LoginForm(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(322, 147)
        Form.setWindowIcon(QIcon(str(resource_path("assets/icons/login.png"))))
        #------------windows size fixed----------------
        Form.setMinimumSize(QtCore.QSize(322, 147))
        Form.setMaximumSize(QtCore.QSize(322, 147))
        # (تنظیم اندازه فرم به صورت ثابت)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 221, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 60, 221, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 110, 92, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 110, 92, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(self.close_ui)
        self.pushButton_2.clicked.connect(self.login) #<--------------

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.label.setText(_translate("Form", "username:"))
        self.label_2.setText(_translate("Form", "password:"))
        self.pushButton.setText(_translate("Form", "cancel"))
        self.pushButton_2.setText(_translate("Form", "login"))

    def close_ui(self):
        self.Form.close()

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        # My idea
        if not username or not password:
            MessageBox.warning(self.Form, "Please enter your username and password!")
            return
        #-------------------------------------
        user = authenticate(username, password)
        if not user:
            MessageBox.error(self.Form, "The username or password is incorrect!")
            return
        self.user_id, role, is_active = user
        if role == "admin" and is_active == 1:
            MessageBox.success(self.Form,"You have successfully logged in.",on_ok=self.show_admin_ui)
        elif role == "student" and is_active == 1:
            MessageBox.success(self.Form,"You have successfully logged in.",on_ok=self.show_student_ui)
        elif role == "professor" and is_active == 1:
            MessageBox.success(self.Form,"You have successfully logged in.",on_ok=self.show_professor_ui)
        elif role == "student" and is_active == 0:
            MessageBox.warning(self.Form, "user is blocked . please contact admin")
        elif role == "professor" and is_active == 0:
            MessageBox.warning(self.Form, "user is blocked . please contact admin")
       
    
    def show_admin_ui(self):
        self.Form.close()
        self.admin_window = QtWidgets.QWidget()
        self.admin_ui = AdminForm()
        self.admin_ui.setupUi(self.admin_window)
        self.admin_window.show()
        
    def show_student_ui(self):
        self.Form.close()
        self.student_window = QtWidgets.QWidget()
        self.student_ui =studentFrom(student_id=self.user_id)
        self.student_ui.setupUi(self.student_window)
        self.student_window.show()
    
    def show_professor_ui(self):
        self.Form.close()
        self.professor_window = QtWidgets.QWidget()
        self.professor_ui = ProfessorForm(professor_id=self.user_id)
        self.professor_ui.setupUi(self.professor_window)
        self.professor_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = LoginForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
