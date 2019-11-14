# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewPOI(object):
    def setupUi(self, NewPOI):
        NewPOI.setObjectName("NewPOI")
        NewPOI.resize(454, 184)
        self.poiTypeLabel = QtWidgets.QLabel(NewPOI)
        self.poiTypeLabel.setGeometry(QtCore.QRect(10, 60, 141, 16))
        self.poiTypeLabel.setObjectName("poiTypeLabel")
        self.poiOutLabel = QtWidgets.QLabel(NewPOI)
        self.poiOutLabel.setGeometry(QtCore.QRect(10, 110, 81, 16))
        self.poiOutLabel.setObjectName("poiOutLabel")
        self.poiOutEdit = QtWidgets.QTextEdit(NewPOI)
        self.poiOutEdit.setGeometry(QtCore.QRect(10, 130, 431, 21))
        self.poiOutEdit.setObjectName("poiOutEdit")
        self.buttonBox = QtWidgets.QDialogButtonBox(NewPOI)
        self.buttonBox.setGeometry(QtCore.QRect(90, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.poiTypeEdit = QtWidgets.QTextEdit(NewPOI)
        self.poiTypeEdit.setGeometry(QtCore.QRect(10, 80, 431, 21))
        self.poiTypeEdit.setObjectName("poiTypeEdit")
        self.poiNameEdit = QtWidgets.QTextEdit(NewPOI)
        self.poiNameEdit.setGeometry(QtCore.QRect(10, 30, 431, 21))
        self.poiNameEdit.setObjectName("poiNameEdit")
        self.poiNameLabel = QtWidgets.QLabel(NewPOI)
        self.poiNameLabel.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.poiNameLabel.setObjectName("poiNameLabel")

        self.retranslateUi(NewPOI)
        QtCore.QMetaObject.connectSlotsByName(NewPOI)

    def retranslateUi(self, NewPOI):
        _translate = QtCore.QCoreApplication.translate
        NewPOI.setWindowTitle(_translate("NewPOI", "New POI"))
        self.poiTypeLabel.setText(_translate("NewPOI", "Poin Of Interest Description"))
        self.poiOutLabel.setText(_translate("NewPOI", "Python Output"))
        self.poiNameLabel.setText(_translate("NewPOI", "Point Of Interest Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewPOI = QtWidgets.QDialog()
    ui = Ui_NewPOI()
    ui.setupUi(NewPOI)
    NewPOI.show()
    sys.exit(app.exec_())
