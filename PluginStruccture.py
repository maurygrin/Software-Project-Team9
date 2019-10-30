# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pluginStructure.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_structureErrorWindow(object):
    def setupUi(self, structureErrorWindow):
        structureErrorWindow.setObjectName("structureErrorWindow")
        structureErrorWindow.resize(400, 99)
        self.buttonBox = QtWidgets.QDialogButtonBox(structureErrorWindow)
        self.buttonBox.setGeometry(QtCore.QRect(30, 50, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.messageLabel = QtWidgets.QLabel(structureErrorWindow)
        self.messageLabel.setGeometry(QtCore.QRect(10, 10, 371, 31))
        self.messageLabel.setObjectName("messageLabel")

        self.retranslateUi(structureErrorWindow)
        self.buttonBox.accepted.connect(structureErrorWindow.accept)
        self.buttonBox.rejected.connect(structureErrorWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(structureErrorWindow)

    def retranslateUi(self, structureErrorWindow):
        _translate = QtCore.QCoreApplication.translate
        structureErrorWindow.setWindowTitle(_translate("structureErrorWindow", "Error Message: Plugin Structure"))
        self.messageLabel.setText(_translate("structureErrorWindow", "The plugin structure XML file is not valid."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    structureErrorWindow = QtWidgets.QDialog()
    ui = Ui_structureErrorWindow()
    ui.setupUi(structureErrorWindow)
    structureErrorWindow.show()
    sys.exit(app.exec_())
