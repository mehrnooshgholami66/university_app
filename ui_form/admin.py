import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from PyQt5 import QtCore, QtGui, QtWidgets
from core.user_action import (
     create_user_role, delete_user, block_user,
     unblock_user, exists_user, is_block, is_unblock)
from core.messages import MessageBox


class AdminForm(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(603, 431)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("10_(50).jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 581, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.createuser_radio = QtWidgets.QRadioButton(self.groupBox)
        self.createuser_radio.setGeometry(QtCore.QRect(10, 40, 95, 20))
        self.createuser_radio.setObjectName("createuser_radio")
        self.blockunblock_radio = QtWidgets.QRadioButton(self.groupBox)
        self.blockunblock_radio.setGeometry(QtCore.QRect(210, 40, 131, 20))
        self.blockunblock_radio.setObjectName("blockunblock_radio")
        self.deleteuser_radio = QtWidgets.QRadioButton(self.groupBox)
        self.deleteuser_radio.setGeometry(QtCore.QRect(450, 40, 95, 20))
        self.deleteuser_radio.setObjectName("deleteuser_radio")
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 581, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.createstudent_radio = QtWidgets.QRadioButton(self.groupBox_2)
        self.createstudent_radio.setGeometry(QtCore.QRect(20, 40, 95, 20))
        self.createstudent_radio.setObjectName("createstudent_radio")
        self.createprofessor_radio = QtWidgets.QRadioButton(self.groupBox_2)
        self.createprofessor_radio.setGeometry(QtCore.QRect(20, 80, 95, 20))
        self.createprofessor_radio.setObjectName("createprofessor_radio")
        self.createuser_username = QtWidgets.QLabel(self.groupBox_2)
        self.createuser_username.setGeometry(QtCore.QRect(160, 30, 71, 16))
        self.createuser_username.setObjectName("createuser_username")
        self.createuser_password = QtWidgets.QLabel(self.groupBox_2)
        self.createuser_password.setGeometry(QtCore.QRect(160, 70, 61, 16))
        self.createuser_password.setObjectName("createuser_password")
        self.inputusername_createuser = QtWidgets.QLineEdit(self.groupBox_2)
        self.inputusername_createuser.setGeometry(QtCore.QRect(250, 30, 171, 22))
        self.inputusername_createuser.setObjectName("inputusername_createuser")
        self.inputpassword_createuser = QtWidgets.QLineEdit(self.groupBox_2)
        self.inputpassword_createuser.setGeometry(QtCore.QRect(250, 70, 171, 22))
        self.inputpassword_createuser.setObjectName("inputpassword_createuser")
        self.createuserButton = QtWidgets.QPushButton(self.groupBox_2)
        self.createuserButton.setGeometry(QtCore.QRect(450, 40, 111, 41))
        self.createuserButton.setObjectName("createuserButton")
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 230, 581, 101))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.blockuser_radio = QtWidgets.QRadioButton(self.groupBox_3)
        self.blockuser_radio.setGeometry(QtCore.QRect(20, 30, 95, 20))
        self.blockuser_radio.setObjectName("blockuser_radio")
        self.unblockuser_radio = QtWidgets.QRadioButton(self.groupBox_3)
        self.unblockuser_radio.setGeometry(QtCore.QRect(20, 70, 95, 20))
        self.unblockuser_radio.setObjectName("unblockuser_radio")
        self.blockuser_username = QtWidgets.QLabel(self.groupBox_3)
        self.blockuser_username.setGeometry(QtCore.QRect(170, 40, 61, 16))
        self.blockuser_username.setObjectName("blockuser_username")
        self.inputusername_blockuser = QtWidgets.QLineEdit(self.groupBox_3)
        self.inputusername_blockuser.setGeometry(QtCore.QRect(250, 40, 171, 22))
        self.inputusername_blockuser.setObjectName("inputusername_blockuser")
        self.commituserButton = QtWidgets.QPushButton(self.groupBox_3)
        self.commituserButton.setGeometry(QtCore.QRect(450, 30, 111, 41))
        self.commituserButton.setObjectName("commituserButton")
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 340, 581, 81))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.horizontalLayoutWidget_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.deleteuser_username = QtWidgets.QLabel(self.groupBox_4)
        self.deleteuser_username.setGeometry(QtCore.QRect(30, 30, 61, 16))
        self.deleteuser_username.setObjectName("deleteuser_username")
        self.inputusername_deleteuser = QtWidgets.QLineEdit(self.groupBox_4)
        self.inputusername_deleteuser.setGeometry(QtCore.QRect(120, 30, 181, 22))
        self.inputusername_deleteuser.setObjectName("inputusername_deleteuser")
        self.deleteuserButton = QtWidgets.QPushButton(self.groupBox_4)
        self.deleteuserButton.setGeometry(QtCore.QRect(452, 20, 111, 41))
        self.deleteuserButton.setObjectName("deleteuserButton")
        self.horizontalLayout_3.addWidget(self.groupBox_4)
        
        # updated the admin panel as given instructions

        self.groupBox_2.setDisabled(True)
        self.groupBox_3.setDisabled(True)
        self.groupBox_4.setDisabled(True)
        self.createuser_radio.clicked.connect(self.active_create_user_box)
        self.blockunblock_radio.clicked.connect(self.active_block_user_box)
        self.deleteuser_radio.clicked.connect(self.active_delete_user_box)
        self.createuserButton.clicked.connect(self.create_user)
        self.commituserButton.clicked.connect(self.block_or_unblock_user)
        self.deleteuserButton.clicked.connect(self.delete_user)



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "admin panel"))
        self.groupBox.setTitle(_translate("Form", "which option"))
        self.createuser_radio.setText(_translate("Form", "create user"))
        self.blockunblock_radio.setText(_translate("Form", "block and unblock"))
        self.deleteuser_radio.setText(_translate("Form", "delete user"))
        self.groupBox_2.setTitle(_translate("Form", "create user"))
        self.createstudent_radio.setText(_translate("Form", "student"))
        self.createprofessor_radio.setText(_translate("Form", "professor"))
        self.createuser_username.setText(_translate("Form", "username"))
        self.createuser_password.setText(_translate("Form", "password"))
        self.createuserButton.setText(_translate("Form", "create"))
        self.groupBox_3.setTitle(_translate("Form", "block or unblock"))
        self.blockuser_radio.setText(_translate("Form", "block user"))
        self.unblockuser_radio.setText(_translate("Form", "unblock user"))
        self.blockuser_username.setText(_translate("Form", "username"))
        self.commituserButton.setText(_translate("Form", "commit"))
        self.groupBox_4.setTitle(_translate("Form", "delete user"))
        self.deleteuser_username.setText(_translate("Form", "username"))
        self.deleteuserButton.setText(_translate("Form", "delete"))




    def active_create_user_box(self):
        self.groupBox_2.setDisabled(False)
        self.groupBox_3.setDisabled(True)
        self.groupBox_4.setDisabled(True)

    def active_block_user_box(self):
        self.groupBox_2.setDisabled(True)
        self.groupBox_3.setDisabled(False)
        self.groupBox_4.setDisabled(True)

    def active_delete_user_box(self):
        self.groupBox_2.setDisabled(True)
        self.groupBox_3.setDisabled(True)
        self.groupBox_4.setDisabled(False)
    
    def block_or_unblock_user(self):
        username = self.inputusername_blockuser.text()
        if not exists_user(username):
            MessageBox.error(self.Form, "user does not exist")
            return
        if self.blockuser_radio.isChecked():
            if is_block(username):
                MessageBox.error(self.Form, "user is already blocked")
                return
            block_user(username)
            self.inputusername_blockuser.setText("")
            MessageBox.success(self.Form, "user blocked successfully") 
        elif self.unblockuser_radio.isChecked():
            if is_unblock(username):
                MessageBox.error(self.Form, "user is already unblocked")
                return
            unblock_user(username)
            self.inputusername_blockuser.setText("")
            MessageBox.success(self.Form, "user unblocked successfully") 
        else:
            MessageBox.error(self.Form, "please select one of block or unblock")

    def create_user(self):
        username = self.inputusername_createuser.text()
        password = self.inputpassword_createuser.text()
        if self.createstudent_radio.isChecked():
            role = "student"
        elif self.createprofessor_radio.isChecked():
            role = "professor"
        else:
            MessageBox.error(self.Form, "please select one of student or professor role")
            return
        if exists_user(username):
            MessageBox.error(self.Form, "user already exists")
            return
        create_user_role(username, password, role)
        self.inputusername_createuser.setText("")
        self.inputpassword_createuser.setText("")
        MessageBox.success(self.Form, "user created successfully") 
        

    def delete_user(self):
        username = self.inputusername_deleteuser.text()
        if not exists_user(username):
            MessageBox.error(self.Form, "user does not exist")
            return
        delete_user(username)
        self.inputusername_deleteuser.setText("")
        MessageBox.success(self.Form, "user deleted successfully") 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = AdminForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
