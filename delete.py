# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_deleteWindow(object):
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 130, 75, 24))
        self.pushButton.setObjectName("pushButton")
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
        self.label.setText(_translate("deleteWindow", "Project Name"))
        self.label_2.setText(_translate("deleteWindow", "Project Name"))
        self.label_3.setText(_translate("deleteWindow", "Project Location"))
        self.label_4.setText(_translate("deleteWindow", "Project Description"))
        self.pushButton.setText(_translate("deleteWindow", "Browse.."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deleteWindow = QtWidgets.QMainWindow()
    ui = Ui_deleteWindow()
    ui.setupUi(deleteWindow)
    deleteWindow.show()
    sys.exit(app.exec_())
