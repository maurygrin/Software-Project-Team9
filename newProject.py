# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newProject.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_newProject(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(528, 306)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 270, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.projectNameLabel = QtWidgets.QLabel(Dialog)
        self.projectNameLabel.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.projectNameLabel.setObjectName("projectNameLabel")
        self.projectNameEdit = QtWidgets.QTextEdit(Dialog)
        self.projectNameEdit.setGeometry(QtCore.QRect(20, 30, 431, 21))
        self.projectNameEdit.setObjectName("projectNameEdit")
        self.projectDescriptionLabel = QtWidgets.QLabel(Dialog)
        self.projectDescriptionLabel.setGeometry(QtCore.QRect(20, 100, 131, 16))
        self.projectDescriptionLabel.setObjectName("projectDescriptionLabel")
        self.projectDescriptionEdit = QtWidgets.QTextEdit(Dialog)
        self.projectDescriptionEdit.setGeometry(QtCore.QRect(20, 120, 431, 141))
        self.projectDescriptionEdit.setObjectName("projectDescriptionEdit")
        self.binaryFilePathEdit = QtWidgets.QTextEdit(Dialog)
        self.binaryFilePathEdit.setGeometry(QtCore.QRect(20, 70, 431, 21))
        self.binaryFilePathEdit.setObjectName("binaryFilePathEdit")
        self.binaryFilePathLabel = QtWidgets.QLabel(Dialog)
        self.binaryFilePathLabel.setGeometry(QtCore.QRect(20, 50, 81, 16))
        self.binaryFilePathLabel.setObjectName("binaryFilePathLabel")
        self.binaryFilePathBrowse = QtWidgets.QPushButton(Dialog)
        self.binaryFilePathBrowse.setGeometry(QtCore.QRect(450, 70, 75, 23))
        self.binaryFilePathBrowse.setObjectName("binaryFilePathBrowse")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.projectNameLabel.setText(_translate("Dialog", "Project Name"))
        self.projectDescriptionLabel.setText(_translate("Dialog", "Project Description"))
        self.binaryFilePathLabel.setText(_translate("Dialog", "Binary File Path"))
        self.binaryFilePathBrowse.setText(_translate("Dialog", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
