import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from core.repositories.user_repo import (
    get_professors,
    get_documents_by_professor
)
from core.messages import MessageBox
from PyQt5.QtWidgets import QPushButton
import shutil


class studentFrom(object):
    """
    Student UI for download documents
    """
    def __init__(self, student_id):
        # student_id از لاگین پاس داده می‌شود
        self.student_id = student_id
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(670, 450)
        Dialog.setMinimumSize(QtCore.QSize(670, 450))
        Dialog.setMaximumSize(QtCore.QSize(670, 450))
        self.form = Dialog
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 630, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 211, 21))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(250, 20, 55, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(310, 20, 191, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 610, 331))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.groupBox)
        # ===============================
        # Data
        self.professors_cache = []
        self.load_professors()

        # Signals
        self.comboBox.currentIndexChanged.connect(self.load_documents)
        self.lineEdit.textChanged.connect(self.filter_professors)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Student panel"))
        self.groupBox.setTitle(_translate("Dialog", "search box"))
        self.label.setText(_translate("Dialog", "search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "type"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "professor"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "action"))

    def load_professors(self):
        self.comboBox.clear()
        self.professors_cache = get_professors()

        for pid, name in self.professors_cache:
            # name = متن، pid = دیتا مخفی
            self.comboBox.addItem(name, pid)

    def filter_professors(self, text):
        self.comboBox.clear()
        for pid, name in self.professors_cache:
            if text.lower() in name.lower():
                self.comboBox.addItem(name, pid)

    def load_documents(self):
        professor_id = self.comboBox.currentData()
        if not professor_id:
            return

        documents = get_documents_by_professor(professor_id)

        self.tableWidget.setRowCount(0)

        for row_index, (title, file_type, file_name, file_path) in enumerate(documents):
            self.tableWidget.insertRow(row_index)

            self.tableWidget.setItem(row_index, 0, QtWidgets.QTableWidgetItem(title))
            self.tableWidget.setItem(row_index, 1, QtWidgets.QTableWidgetItem(file_type))
            self.tableWidget.setItem(row_index, 2, QtWidgets.QTableWidgetItem(
                self.comboBox.currentText()
            ))

            # ---------- Download button ----------
            btn = QPushButton("Download")
            btn.setIcon(QIcon("assets/icons/download.png"))
            btn.clicked.connect(
                lambda _, p=file_path, n=file_name: self.download_file(p, n)
            )
            self.tableWidget.setCellWidget(row_index, 3, btn)
    def download_file(self, file_path, file_name):
        save_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.form,
            "Save file",
            file_name
        )

        if not save_path:
            return

        shutil.copy(file_path, save_path)
        MessageBox.success(self.form, "File downloaded successfully.")
        






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QDialog()
    ui = studentFrom(student_id=11)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
