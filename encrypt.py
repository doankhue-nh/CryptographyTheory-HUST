# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\project_ltmm\encrypt.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Encryption(object):
    def setupUi(self, Encryption):
        Encryption.setObjectName("Encryption")
        Encryption.resize(1551, 931)
        font = QtGui.QFont()
        font.setPointSize(11)
        Encryption.setFont(font)
        self.back_button = QtWidgets.QPushButton(Encryption)
        self.back_button.setGeometry(QtCore.QRect(700, 890, 171, 31))
        self.back_button.setStyleSheet("font: bold;\n"
"font-size: 13pt;\n"
"color: rgb(0, 0, 127)")
        self.back_button.setObjectName("back_button")
        self.browse_button = QtWidgets.QPushButton(Encryption)
        self.browse_button.setGeometry(QtCore.QRect(500, 30, 211, 51))
        self.browse_button.setStyleSheet("font: bold;\n"
"font-size: 20pt;\n"
"color: rgb(0, 0, 127)")
        self.browse_button.setObjectName("browse_button")
        self.aes_button = QtWidgets.QPushButton(Encryption)
        self.aes_button.setGeometry(QtCore.QRect(90, 290, 231, 41))
        self.aes_button.setStyleSheet("font: bold;\n"
"font-size: 20pt;\n"
"color: rgb(0, 0, 127)")
        self.aes_button.setObjectName("aes_button")
        self.des_button = QtWidgets.QPushButton(Encryption)
        self.des_button.setGeometry(QtCore.QRect(670, 290, 231, 41))
        self.des_button.setStyleSheet("font: bold;\n"
"font-size: 20pt;\n"
"color: rgb(0, 0, 127)")
        self.des_button.setObjectName("des_button")
        self.rc4_button = QtWidgets.QPushButton(Encryption)
        self.rc4_button.setGeometry(QtCore.QRect(1200, 300, 231, 41))
        self.rc4_button.setStyleSheet("font: bold;\n"
"font-size: 20pt;\n"
"color: rgb(0, 0, 127)")
        self.rc4_button.setObjectName("rc4_button")
        self.choose_label = QtWidgets.QLabel(Encryption)
        self.choose_label.setGeometry(QtCore.QRect(40, 30, 431, 51))
        self.choose_label.setStyleSheet("font: bold;\n"
"font-size: 25pt\n"
"")
        self.choose_label.setObjectName("choose_label")
        self.key_label = QtWidgets.QLabel(Encryption)
        self.key_label.setGeometry(QtCore.QRect(80, 110, 341, 51))
        self.key_label.setStyleSheet("font: bold;\n"
"font-size: 25pt\n"
"")
        self.key_label.setObjectName("key_label")
        self.key_edit = QtWidgets.QTextEdit(Encryption)
        self.key_edit.setGeometry(QtCore.QRect(420, 110, 581, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.key_edit.setFont(font)
        self.key_edit.setObjectName("key_edit")
        self.img_label = QtWidgets.QLabel(Encryption)
        self.img_label.setGeometry(QtCore.QRect(280, 410, 241, 41))
        self.img_label.setStyleSheet("font-size: 20pt;\n"
"font: bold\n"
"")
        self.img_label.setObjectName("img_label")
        self.img_label_2 = QtWidgets.QLabel(Encryption)
        self.img_label_2.setGeometry(QtCore.QRect(1060, 410, 271, 51))
        self.img_label_2.setStyleSheet("font-size: 20pt;\n"
"font: bold\n"
"")
        self.img_label_2.setObjectName("img_label_2")
        self.img = QtWidgets.QLabel(Encryption)
        self.img.setGeometry(QtCore.QRect(130, 470, 511, 411))
        self.img.setText("")
        self.img.setScaledContents(True)
        self.img.setObjectName("img")
        self.enimg = QtWidgets.QLabel(Encryption)
        self.enimg.setGeometry(QtCore.QRect(920, 470, 551, 411))
        self.enimg.setText("")
        self.enimg.setScaledContents(True)
        self.enimg.setObjectName("enimg")
        self.label = QtWidgets.QLabel(Encryption)
        self.label.setGeometry(QtCore.QRect(280, 190, 301, 81))
        self.label.setStyleSheet("font:bold;\n"
"font-size: 25pt;\n"
"color: rgb(85, 0, 127)")
        self.label.setObjectName("label")
        self.time_label = QtWidgets.QLabel(Encryption)
        self.time_label.setGeometry(QtCore.QRect(620, 210, 751, 41))
        self.time_label.setStyleSheet("font:bold;\n"
"font-size: 20pt")
        self.time_label.setText("")
        self.time_label.setObjectName("time_label")
        self.cbc_button = QtWidgets.QPushButton(Encryption)
        self.cbc_button.setGeometry(QtCore.QRect(30, 350, 141, 51))
        self.cbc_button.setStyleSheet("font: bold;\n"
"font-size: 13pt;\n"
"color: rgb(0, 0, 127)")
        self.cbc_button.setObjectName("cbc_button")
        self.ecb_button = QtWidgets.QPushButton(Encryption)
        self.ecb_button.setGeometry(QtCore.QRect(220, 350, 141, 51))
        self.ecb_button.setStyleSheet("font: bold;\n"
"font-size: 13pt;\n"
"color: rgb(0, 0, 127)")
        self.ecb_button.setObjectName("ecb_button")
        self.team_label = QtWidgets.QLabel(Encryption)
        self.team_label.setGeometry(QtCore.QRect(1070, 10, 471, 151))
        self.team_label.setStyleSheet("color: rgb(170, 85, 255);\n"
"font: bold")
        self.team_label.setObjectName("team_label")

        self.retranslateUi(Encryption)
        QtCore.QMetaObject.connectSlotsByName(Encryption)

    def retranslateUi(self, Encryption):
        _translate = QtCore.QCoreApplication.translate
        Encryption.setWindowTitle(_translate("Encryption", "Dialog"))
        self.back_button.setText(_translate("Encryption", "Back"))
        self.browse_button.setText(_translate("Encryption", "Browse"))
        self.aes_button.setText(_translate("Encryption", "AES"))
        self.des_button.setText(_translate("Encryption", "DES"))
        self.rc4_button.setText(_translate("Encryption", "RC4"))
        self.choose_label.setText(_translate("Encryption", "Choose your picture"))
        self.key_label.setText(_translate("Encryption", "Enter your key"))
        self.key_edit.setHtml(_translate("Encryption", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:19pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7.8pt;\"><br /></p></body></html>"))
        self.key_edit.setPlaceholderText(_translate("Encryption", "Type here!"))
        self.img_label.setText(_translate("Encryption", "Your picture"))
        self.img_label_2.setText(_translate("Encryption", "Encrypt Picture"))
        self.label.setText(_translate("Encryption", "Running time:"))
        self.cbc_button.setText(_translate("Encryption", "CBC Mode"))
        self.ecb_button.setText(_translate("Encryption", "ECB Mode"))
        self.team_label.setText(_translate("Encryption", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Cryptography Theory </span></p><p align=\"center\"><span style=\" font-size:26pt;\">Made by Team07</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Encryption = QtWidgets.QDialog()
    ui = Ui_Encryption()
    ui.setupUi(Encryption)
    Encryption.show()
    sys.exit(app.exec_())
