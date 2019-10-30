# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BinaryFileErrorOverlay.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_binaryFileErrorWindow(object):

    def setupUi(self, binaryFileErrorWindow):
        binaryFileErrorWindow.setObjectName("binaryFileErrorWindow")
        binaryFileErrorWindow.resize(400, 99)
        self.buttonBox = QtWidgets.QDialogButtonBox(binaryFileErrorWindow)
        self.buttonBox.setGeometry(QtCore.QRect(30, 50, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.messageLabel = QtWidgets.QLabel(binaryFileErrorWindow)
        self.messageLabel.setGeometry(QtCore.QRect(10, 10, 371, 31))
        self.messageLabel.setObjectName("messageLabel")

        self.retranslateUi(binaryFileErrorWindow)
        self.buttonBox.accepted.connect(binaryFileErrorWindow.accept)
        self.buttonBox.rejected.connect(binaryFileErrorWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(binaryFileErrorWindow)

    def retranslateUi(self, binaryFileErrorWindow):
        _translate = QtCore.QCoreApplication.translate
        binaryFileErrorWindow.setWindowTitle(_translate("binaryFileErrorWindow", "Error Message: x86 Architecture Binary File"))
        self.messageLabel.setText(_translate("binaryFileErrorWindow", "The system only supports files that are of x86 architecture."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    binaryFileErrorWindow = QtWidgets.QDialog()
    ui = Ui_binaryFileErrorWindow()
    ui.setupUi(binaryFileErrorWindow)
    binaryFileErrorWindow.show()
    sys.exit(app.exec_())
