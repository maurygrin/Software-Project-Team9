# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pluginDataset.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_datasetErrorWindow(object):
    def setupUi(self, datasetErrorWindow):
        datasetErrorWindow.setObjectName("datasetErrorWindow")
        datasetErrorWindow.resize(400, 99)
        self.buttonBox = QtWidgets.QDialogButtonBox(datasetErrorWindow)
        self.buttonBox.setGeometry(QtCore.QRect(30, 50, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.messageLabel = QtWidgets.QLabel(datasetErrorWindow)
        self.messageLabel.setGeometry(QtCore.QRect(10, 10, 371, 31))
        self.messageLabel.setObjectName("messageLabel")

        self.retranslateUi(datasetErrorWindow)
        self.buttonBox.accepted.connect(datasetErrorWindow.accept)
        self.buttonBox.rejected.connect(datasetErrorWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(datasetErrorWindow)

    def retranslateUi(self, datasetErrorWindow):
        _translate = QtCore.QCoreApplication.translate
        datasetErrorWindow.setWindowTitle(_translate("datasetErrorWindow", "Error Message: Predefined Data Set"))
        self.messageLabel.setText(_translate("datasetErrorWindow", "The plugin predefined data set is not valid."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    datasetErrorWindow = QtWidgets.QDialog()
    ui = Ui_datasetErrorWindow()
    ui.setupUi(datasetErrorWindow)
    datasetErrorWindow.show()
    sys.exit(app.exec_())
