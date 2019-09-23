# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_deleteWindow(object):

    def __init__(self):
        self.text = None

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self.centralwidget, 'Save File', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            path = self.textEdit_3.toPlainText()
            title = self.textEdit_4.toPlainText()
            user = self.textEdit_2.toPlainText()
            description = self.textEdit.toPlainText()
            f.write(description)
            f.write("\n")
            f.write(path)
            f.write("\n")
            f.write(user)
            f.write("\n")
            f.write(title)
            f.write("\n")

    def getFilePath(self):
        filename = QFileDialog.getOpenFileName(self.centralwidget, 'Open File', os.getenv('HOME'))
        self.textEdit_3.setText(str(filename))
        print(filename)

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self.centralwidget, 'Open File', os.getenv('HOME'))
        with open(filename[0], 'r') as f:
            file_text = f.read()
            self.text.setText(file_text)

    def clear_text(self):
        self.text.clear()

    def cancel(self):
        sys.exit()

    def setupUi(self, deleteWindow):
        deleteWindow.setObjectName("deleteWindow")
        deleteWindow.resize(774, 525)
        self.centralwidget = QtWidgets.QWidget(deleteWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(180, 40, 431, 21))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(180, 80, 431, 21))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(180, 130, 431, 21))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(180, 180, 431, 141))
        self.textEdit_4.setObjectName("textEdit_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 60, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 110, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 160, 111, 16))
        self.label_4.setObjectName("label_4")
        self.fileBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.fileBrowse.setGeometry(QtCore.QRect(630, 130, 75, 24))
        self.fileBrowse.setObjectName("fileBrowse")

        self.fileBrowse.clicked.connect(self.getFilePath)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 450, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 450, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.save_text)

        deleteWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(deleteWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 21))
        self.menubar.setObjectName("menubar")
        deleteWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(deleteWindow)
        self.statusbar.setObjectName("statusbar")
        deleteWindow.setStatusBar(self.statusbar)

        self.retranslateUi(deleteWindow)
        QtCore.QMetaObject.connectSlotsByName(deleteWindow)

    def retranslateUi(self, deleteWindow):
        _translate = QtCore.QCoreApplication.translate
        deleteWindow.setWindowTitle(_translate("deleteWindow", "MainWindow"))
        self.textEdit_2.setHtml(_translate("deleteWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("deleteWindow", "Project Name"))
        self.label_2.setText(_translate("deleteWindow", "User Name "))
        self.label_3.setText(_translate("deleteWindow", "Project Path"))
        self.label_4.setText(_translate("deleteWindow", "Project Description"))
        self.fileBrowse.setText(_translate("deleteWindow", "Browse.."))
        self.pushButton_2.setText(_translate("deleteWindow", "Cancel"))
        self.pushButton_3.setText(_translate("deleteWindow", "Save"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    deleteWindow = QtWidgets.QMainWindow()
    ui = Ui_deleteWindow()
    ui.setupUi(deleteWindow)
    deleteWindow.show()
    sys.exit(app.exec_())
