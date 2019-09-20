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
        deleteWindow.resize(399, 190)
        self.centralwidget = QtWidgets.QWidget(deleteWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(90, 40, 321, 16))
        self.label_14.setObjectName("label_14")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(70, 100, 113, 32))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(220, 100, 113, 32))
        self.pushButton_13.setObjectName("pushButton_13")
        deleteWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(deleteWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 399, 21))
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
        self.label_14.setText(_translate("deleteWindow", "Are you soure that you want to delete?"))
        self.pushButton_12.setText(_translate("deleteWindow", "Cancel"))
        self.pushButton_13.setText(_translate("deleteWindow", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deleteWindow = QtWidgets.QMainWindow()
    ui = Ui_deleteWindow()
    ui.setupUi(deleteWindow)
    deleteWindow.show()
    sys.exit(app.exec_())
