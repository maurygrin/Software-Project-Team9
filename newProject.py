# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newProject.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewProject(object):
    def setupUi(self, NewProject):
        NewProject.setObjectName("NewProject")
        NewProject.resize(539, 333)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewProject)
        self.buttonBox.setGeometry(QtCore.QRect(110, 290, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.projectNameLabel = QtWidgets.QLabel(NewProject)
        self.projectNameLabel.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.projectNameLabel.setObjectName("projectNameLabel")
        self.projectNameEdit = QtWidgets.QTextEdit(NewProject)
        self.projectNameEdit.setGeometry(QtCore.QRect(20, 30, 431, 21))
        self.projectNameEdit.setObjectName("projectNameEdit")
        self.projectDescriptionLabel = QtWidgets.QLabel(NewProject)
        self.projectDescriptionLabel.setGeometry(QtCore.QRect(20, 110, 131, 16))
        self.projectDescriptionLabel.setObjectName("projectDescriptionLabel")
        self.projectDescriptionEdit = QtWidgets.QTextEdit(NewProject)
        self.projectDescriptionEdit.setGeometry(QtCore.QRect(20, 140, 431, 141))
        self.projectDescriptionEdit.setObjectName("projectDescriptionEdit")
        self.binaryFilePathEdit = QtWidgets.QTextEdit(NewProject)
        self.binaryFilePathEdit.setGeometry(QtCore.QRect(20, 80, 431, 21))
        self.binaryFilePathEdit.setObjectName("binaryFilePathEdit")
        self.binaryFilePathLabel = QtWidgets.QLabel(NewProject)
        self.binaryFilePathLabel.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.binaryFilePathLabel.setObjectName("binaryFilePathLabel")
        self.binaryFilePathBrowse = QtWidgets.QPushButton(NewProject)
        self.binaryFilePathBrowse.setGeometry(QtCore.QRect(460, 80, 75, 31))
        self.binaryFilePathBrowse.setObjectName("binaryFilePathBrowse")

        self.retranslateUi(NewProject)
        self.buttonBox.accepted.connect(NewProject.accept)
        self.buttonBox.rejected.connect(NewProject.reject)
        QtCore.QMetaObject.connectSlotsByName(NewProject)

    def retranslateUi(self, NewProject):
        _translate = QtCore.QCoreApplication.translate
        NewProject.setWindowTitle(_translate("NewProject", "New Project"))
        self.projectNameLabel.setText(_translate("NewProject", "Project Name"))
        self.projectDescriptionLabel.setText(_translate("NewProject", "Project Description"))
        self.binaryFilePathLabel.setText(_translate("NewProject", "Binary File Path"))
        self.binaryFilePathBrowse.setText(_translate("NewProject", "Browse"))
