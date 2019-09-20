# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'savePM.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_confirmationWindow(object):
    def setupUi(self, confirmationWindow):
        confirmationWindow.setObjectName("confirmationWindow")
        confirmationWindow.resize(399, 192)
        self.centralwidget = QtWidgets.QWidget(confirmationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(80, 110, 113, 32))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(220, 110, 113, 32))
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(100, 50, 321, 16))
        self.label_14.setObjectName("label_14")
        confirmationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(confirmationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 399, 21))
        self.menubar.setObjectName("menubar")
        confirmationWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(confirmationWindow)
        self.statusbar.setObjectName("statusbar")
        confirmationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(confirmationWindow)
        QtCore.QMetaObject.connectSlotsByName(confirmationWindow)

    def retranslateUi(self, confirmationWindow):
        _translate = QtCore.QCoreApplication.translate
        confirmationWindow.setWindowTitle(_translate("confirmationWindow", "MainWindow"))
        self.pushButton_12.setText(_translate("confirmationWindow", "Cancel"))
        self.pushButton_13.setText(_translate("confirmationWindow", "Save"))
        self.label_14.setText(_translate("confirmationWindow", "Are you soure that you want to save?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    confirmationWindow = QtWidgets.QMainWindow()
    ui = Ui_confirmationWindow()
    ui.setupUi(confirmationWindow)
    confirmationWindow.show()
    sys.exit(app.exec_())
