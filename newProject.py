# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newProject.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from Project import Project

class Ui_newProject(object):

    def createProject(self, name, description):
        if not name and not description:
            print("Failed")
        else:
            self.project = Project(name, description)

    def setupUi(self, Dialog):

        self.project = ""

        Dialog.setObjectName("New Project")
        Dialog.resize(492, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 240, 341, 32))
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
        self.projectDescriptionLabel.setGeometry(QtCore.QRect(20, 60, 131, 16))
        self.projectDescriptionLabel.setObjectName("projectDescriptionLabel")
        self.projectDescriptionEdit = QtWidgets.QTextEdit(Dialog)
        self.projectDescriptionEdit.setGeometry(QtCore.QRect(20, 80, 431, 141))
        self.projectDescriptionEdit.setObjectName("projectDescriptionEdit")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.buttonBox.accepted.connect(
            lambda: self.createProject(self.projectNameEdit.toPlainText(), self.projectDescriptionEdit.toPlainText()))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("New Project", "New Project"))
        self.projectNameLabel.setText(_translate("Dialog", "Project Name"))
        self.projectDescriptionLabel.setText(_translate("Dialog", "Project Description"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_newProject()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
