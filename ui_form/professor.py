import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt
import shutil
from core.messages import MessageBox
from core.repositories.file_repo import create_document
from PyQt5.QtGui import QIcon


class ProfessorForm(object):
    def __init__(self, professor_id):
        # professor_id از لاگین پاس داده می‌شود
        self.professor_id = professor_id

    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        Form.resize(571, 260)
        #------------windows size fixed----------------

        # (تنظیم اندازه فرم به صورت ثابت)
        # --- Layout اصلی ---
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 551, 241))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        # --- GroupBox Upload ---
        self.groupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.itemtypelable_upload = QtWidgets.QLabel(self.groupBox)
        self.itemtypelable_upload.setGeometry(QtCore.QRect(20, 40, 55, 16))

        # ComboBox: نوع فایل
        self.DacumentArticle_upload = QtWidgets.QComboBox(self.groupBox)
        self.DacumentArticle_upload.setGeometry(QtCore.QRect(80, 33, 461, 31))
        self.DacumentArticle_upload.addItem("document")
        self.DacumentArticle_upload.addItem("article")

        # دکمه انتخاب فایل
        self.selectpushButton_upload = QtWidgets.QPushButton(self.groupBox)
        self.selectpushButton_upload.setGeometry(QtCore.QRect(10, 80, 121, 41))

        # Label نمایش نام فایل انتخاب شده
        self.browselabel_uplod = QtWidgets.QLabel(self.groupBox)
        self.browselabel_uplod.setGeometry(QtCore.QRect(150, 92, 350, 16))
        self.browselabel_uplod.setWordWrap(True)
        self.browselabel_uplod.setMinimumWidth(350)

        # LineEdit برای نام دلخواه فایل
        self.uploadnamelabel_upload = QtWidgets.QLabel(self.groupBox)
        self.uploadnamelabel_upload.setGeometry(QtCore.QRect(23, 148, 91, 16))
        self.uploadnamelineEdit_upload = QtWidgets.QLineEdit(self.groupBox)
        self.uploadnamelineEdit_upload.setGeometry(QtCore.QRect(120, 140, 421, 31))

        # دکمه آپلود
        self.uploadpushButton_upload = QtWidgets.QPushButton(self.groupBox)
        self.uploadpushButton_upload.setGeometry(QtCore.QRect(10, 190, 531, 41))

        self.horizontalLayout.addWidget(self.groupBox)

        # --- متغیر داخلی ---
        self.selected_file_path = None

        # --- اتصال سیگنال‌ها ---
        self.selectpushButton_upload.clicked.connect(self.select_file)
        self.uploadpushButton_upload.clicked.connect(self.upload_file)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "professor panel"))
        self.groupBox.setTitle(_translate("Form", "upload item"))
        self.itemtypelable_upload.setText(_translate("Form", "item type"))
        self.selectpushButton_upload.setText(_translate("Form", "select"))
        self.browselabel_uplod.setText(_translate("Form", "browse"))
        self.uploadnamelabel_upload.setText(_translate("Form", "upload name"))
        self.uploadpushButton_upload.setText(_translate("Form", "upload"))

    # ----------------- متد انتخاب فایل -----------------
    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.Form, "Select file", "", "All Files (*.*)"
        )
        if not file_path:
            return
        self.selected_file_path = file_path
        self.browselabel_uplod.setText(Path(file_path).name)

    # ----------------- متد آپلود فایل -----------------

    def upload_file(self):
        if not self.selected_file_path:
            MessageBox.error(self.Form, "No file selected")
            return

        title = self.uploadnamelineEdit_upload.text().strip()
        if not title:
            MessageBox.error(self.Form, "Upload name is required")
            return

        file_type = self.DacumentArticle_upload.currentText()
        source_path = Path(self.selected_file_path)

        # (موس رو به حالت لودینگ تغییر می‌دهیم)
        QtWidgets.QApplication.setOverrideCursor(Qt.WaitCursor)
        self.uploadpushButton_upload.setDisabled(True)
        import uuid
        unique_suffix = uuid.uuid4().hex  # تولید یک شناسه یکتا
        destination_file_name = f"{unique_suffix}_{source_path.name}"  # فایل جدید یونیک

        # --- (مسیر ذخیره فایل)---
        storage_dir = Path("storage") / file_type
        storage_dir.mkdir(parents=True, exist_ok=True)
        destination_path = storage_dir / destination_file_name

        # (کپی فایل به storage)
        shutil.copy(self.selected_file_path, destination_path)

        # (ثبت در دیتابیس)
        create_document(
            title=title,
            file_type=file_type,
            professor_id=self.professor_id,  # (پاس داده شده از لاگین)
            file_name=source_path.name,
            file_path=str(destination_path),
        )

        # --- (بازگرداندن موس) ---
        QtWidgets.QApplication.restoreOverrideCursor()
        self.uploadpushButton_upload.setDisabled(False)

        # --- (پیام موفقیت) ---
        MessageBox.success(self.Form, "File uploaded successfully")
        self.uploadnamelineEdit_upload.setText("")
        self.browselabel_uplod.setText("browse")  # (بازگرداندن Label)


# ------------------- اجرای مستقل فرم -------------------
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = ProfessorForm(professor_id=10)  # نمونه professor_id
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
