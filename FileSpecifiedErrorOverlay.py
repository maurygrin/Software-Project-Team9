# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileSpecifiedErrorOverlay.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fileSpecifiedErrorWindow(object):
    def setupUi(self, fileSpecifiedErrorWindow):
        fileSpecifiedErrorWindow.setObjectName("fileSpecifiedErrorWindow")
        fileSpecifiedErrorWindow.resize(400, 99)
        self.buttonBox = QtWidgets.QDialogButtonBox(fileSpecifiedErrorWindow)
        self.buttonBox.setGeometry(QtCore.QRect(30, 60, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.messageLabel = QtWidgets.QLabel(fileSpecifiedErrorWindow)
        self.messageLabel.setGeometry(QtCore.QRect(10, 10, 371, 31))
        self.messageLabel.setObjectName("messageLabel")
        self.messageLabel_2 = QtWidgets.QLabel(fileSpecifiedErrorWindow)
        self.messageLabel_2.setGeometry(QtCore.QRect(10, 30, 371, 31))
        self.messageLabel_2.setObjectName("messageLabel_2")

        self.retranslateUi(fileSpecifiedErrorWindow)
        self.buttonBox.accepted.connect(fileSpecifiedErrorWindow.accept)
        self.buttonBox.rejected.connect(fileSpecifiedErrorWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(fileSpecifiedErrorWindow)

    def retranslateUi(self, fileSpecifiedErrorWindow):
        _translate = QtCore.QCoreApplication.translate
        fileSpecifiedErrorWindow.setWindowTitle(_translate("fileSpecifiedErrorWindow", "Error Message: File Specified"))
        self.messageLabel.setText(_translate("fileSpecifiedErrorWindow", "A project is associated with one binary file and cannot be "))
        self.messageLabel_2.setText(_translate("fileSpecifiedErrorWindow", "saved without a binary file. Please provide a binary file."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fileSpecifiedErrorWindow = QtWidgets.QDialog()
    ui = Ui_fileSpecifiedErrorWindow()
    ui.setupUi(fileSpecifiedErrorWindow)
    fileSpecifiedErrorWindow.show()
    sys.exit(app.exec_())
