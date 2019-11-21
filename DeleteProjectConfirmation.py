# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteProjectConfirmation.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_deleteProjectConfirmation(object):
    def setupUi(self, deleteProjectConfirmation):
        deleteProjectConfirmation.setObjectName("deleteProjectConfirmation")
        deleteProjectConfirmation.resize(400, 99)
        self.buttonBox = QtWidgets.QDialogButtonBox(deleteProjectConfirmation)
        self.buttonBox.setGeometry(QtCore.QRect(30, 50, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.messageLabel = QtWidgets.QLabel(deleteProjectConfirmation)
        self.messageLabel.setGeometry(QtCore.QRect(10, 10, 371, 31))
        self.messageLabel.setObjectName("messageLabel")
        self.messageLabel_2 = QtWidgets.QLabel(deleteProjectConfirmation)
        self.messageLabel_2.setGeometry(QtCore.QRect(10, 30, 371, 31))
        self.messageLabel_2.setObjectName("messageLabel_2")

        self.retranslateUi(deleteProjectConfirmation)
        self.buttonBox.accepted.connect(deleteProjectConfirmation.accept)
        self.buttonBox.rejected.connect(deleteProjectConfirmation.reject)
        QtCore.QMetaObject.connectSlotsByName(deleteProjectConfirmation)

    def retranslateUi(self, deleteProjectConfirmation):
        _translate = QtCore.QCoreApplication.translate
        deleteProjectConfirmation.setWindowTitle(_translate("deleteProjectConfirmation", "Delete Project Confirmation"))
        self.messageLabel.setText(_translate("deleteProjectConfirmation", "You are about to delete permanently a project. Are you sure"))
        self.messageLabel_2.setText(_translate("deleteProjectConfirmation", "you want to delete it?"))
