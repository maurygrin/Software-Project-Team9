# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pluginError.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pluginSelected(object):
    def setupUi(self, pluginSelected):
        pluginSelected.setObjectName("pluginSelected")
        pluginSelected.resize(400, 99)
        self.buttonBox = QtWidgets.QDialogButtonBox(pluginSelected)
        self.buttonBox.setGeometry(QtCore.QRect(30, 60, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.messageLabel = QtWidgets.QLabel(pluginSelected)
        self.messageLabel.setGeometry(QtCore.QRect(30, 20, 371, 31))
        self.messageLabel.setObjectName("messageLabel")

        self.retranslateUi(pluginSelected)
        self.buttonBox.accepted.connect(pluginSelected.accept)
        self.buttonBox.rejected.connect(pluginSelected.reject)
        QtCore.QMetaObject.connectSlotsByName(pluginSelected)

    def retranslateUi(self, pluginSelected):
        _translate = QtCore.QCoreApplication.translate
        pluginSelected.setWindowTitle(_translate("pluginSelected", "Error Message: Plugin Selected"))
        self.messageLabel.setText(_translate("pluginSelected", "You need to select a plugin before running an analysis."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pluginSelected = QtWidgets.QDialog()
    ui = Ui_pluginSelected()
    ui.setupUi(pluginSelected)
    pluginSelected.show()
    sys.exit(app.exec_())
