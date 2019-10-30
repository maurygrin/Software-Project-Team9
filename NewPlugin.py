# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newPlugin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newPlugin(object):
    def setupUi(self, newPlugin):
        newPlugin.setObjectName("newPlugin")
        newPlugin.resize(492, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(newPlugin)
        self.buttonBox.setGeometry(QtCore.QRect(110, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.projectNameLabel = QtWidgets.QLabel(newPlugin)
        self.projectNameLabel.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.projectNameLabel.setObjectName("projectNameLabel")
        self.pluginNameEdit = QtWidgets.QTextEdit(newPlugin)
        self.pluginNameEdit.setGeometry(QtCore.QRect(20, 30, 431, 21))
        self.pluginNameEdit.setObjectName("pluginNameEdit")
        self.pluginDescriptionLabel = QtWidgets.QLabel(newPlugin)
        self.pluginDescriptionLabel.setGeometry(QtCore.QRect(20, 60, 131, 16))
        self.pluginDescriptionLabel.setObjectName("pluginDescriptionLabel")
        self.pluginDescriptionEdit = QtWidgets.QTextEdit(newPlugin)
        self.pluginDescriptionEdit.setGeometry(QtCore.QRect(20, 80, 431, 141))
        self.pluginDescriptionEdit.setObjectName("pluginDescriptionEdit")

        self.retranslateUi(newPlugin)
        self.buttonBox.accepted.connect(newPlugin.accept)
        self.buttonBox.rejected.connect(newPlugin.reject)
        QtCore.QMetaObject.connectSlotsByName(newPlugin)

    def retranslateUi(self, newPlugin):
        _translate = QtCore.QCoreApplication.translate
        newPlugin.setWindowTitle(_translate("newPlugin", "New Plugin"))
        self.projectNameLabel.setText(_translate("newPlugin", "Plugin Name"))
        self.pluginDescriptionLabel.setText(_translate("newPlugin", "Plugin Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newPlugin = QtWidgets.QDialog()
    ui = Ui_newPlugin()
    ui.setupUi(newPlugin)
    newPlugin.show()
    sys.exit(app.exec_())
