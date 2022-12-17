import sys
import time
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QFileDialog
)
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
from menu import Ui_CryptographyTheory
from encrypt import Ui_Encryption
from aes_encrypt import process_aes_cbc, process_aes_ecb
from des_encrypt import process_des
from rc4_encrypt import process_rc4

filename = []


class menu(QMainWindow, Ui_CryptographyTheory):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.en_button.clicked.connect(self.encryptFunction)

    def encryptFunction(self):
        img_encrypt = encrypt()
        widget.addWidget(img_encrypt)
        widget.setCurrentIndex(widget.currentIndex()+1)


class encrypt(QMainWindow, Ui_Encryption):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.second_label.setHidden(True)
        self.ecb_button.setHidden(True)
        self.cbc_button.setHidden(True)
        self.back_button.clicked.connect(self.backFunction)
        self.browse_button.clicked.connect(self.browseFunction)
        self.aes_button.clicked.connect(self.aesFunction)
        self.des_button.clicked.connect(self.desFunction)
        self.rc4_button.clicked.connect(self.rc4Function)
        self.ecb_button.clicked.connect(self.ecbFunction)
        self.cbc_button.clicked.connect(self.cbcFunction)

    def backFunction(self):
        back = menu()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def browseFunction(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Open file', '', 'Images (*.png)')
        self.img.setPixmap(QPixmap(fname[0]))
        linkFile = fname[0].split('/')
        filename.append(linkFile[-1])

    def aesFunction(self):
        self.ecb_button.setHidden(False)
        self.cbc_button.setHidden(False)

    def cbcFunction(self):
        key = self.key_edit.toPlainText()
        original_name = filename[-1]
        filename_out = original_name.split('.')[0] + "-aes-cbc"
        start_time = time.time()
        process_aes_cbc(original_name, filename_out, key)
        self.enimg.setPixmap(QPixmap(filename_out + ".png"))
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.time_label.setText(str(elapsed_time))
        self.second_label.setHidden(False)

    def ecbFunction(self):
        key = self.key_edit.toPlainText()
        original_name = filename[-1]
        filename_out = original_name.split('.')[0] + "-aes-ecb"
        start_time = time.time()
        process_aes_ecb(original_name, filename_out, key)
        self.enimg.setPixmap(QPixmap(filename_out + ".png"))
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.time_label.setText(str(elapsed_time))
        self.second_label.setHidden(False)

    def desFunction(self):
        key = self.key_edit.toPlainText()
        original_name = filename[-1]
        filename_out = original_name.split('.')[0] + "-des"
        start_time = time.time()
        process_des(original_name, filename_out, key)
        self.enimg.setPixmap(QPixmap(filename_out + ".png"))
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.time_label.setText(str(elapsed_time))
        self.second_label.setHidden(False)

    def rc4Function(self):
        key = self.key_edit.toPlainText()
        original_name = filename[-1]
        filename_out = original_name.split('.')[0] + "-rc4"
        start_time = time.time()
        process_rc4(original_name, filename_out, key)
        self.enimg.setPixmap(QPixmap(filename_out + ".png"))
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.time_label.setText(str(elapsed_time))
        self.second_label.setHidden(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = menu()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainWindow)
    widget.setFixedHeight(861)
    widget.setFixedWidth(1347)
    widget.show()
    app.exec_()

# python -m PyQt5.uic.pyuic -x D:\project_ltmm\encrypt.ui -o D:\project_ltmm\encrypt.py
# python -m PyQt5.uic.pyuic -x D:\project_ltmm\menu.ui -o D:\project_ltmm\menu.py
