# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OutputFieldView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OutputFieldView(object):
    def setupUi(self, OutputFieldView):
        OutputFieldView.setObjectName("OutputFieldView")
        OutputFieldView.resize(616, 402)
        self.generateOutputButton = QtWidgets.QPushButton(OutputFieldView)
        self.generateOutputButton.setGeometry(QtCore.QRect(420, 360, 113, 32))
        self.generateOutputButton.setObjectName("generateOutputButton")
        self.browseOutputButton = QtWidgets.QPushButton(OutputFieldView)
        self.browseOutputButton.setGeometry(QtCore.QRect(190, 360, 113, 32))
        self.browseOutputButton.setObjectName("browseOutputButton")
        self.descriptionOutputLabel = QtWidgets.QLabel(OutputFieldView)
        self.descriptionOutputLabel.setGeometry(QtCore.QRect(30, 70, 81, 16))
        self.descriptionOutputLabel.setObjectName("descriptionOutputLabel")
        self.descriptionOutputField = QtWidgets.QTextEdit(OutputFieldView)
        self.descriptionOutputField.setGeometry(QtCore.QRect(110, 70, 481, 221))
        self.descriptionOutputField.setObjectName("descriptionOutputField")
        self.nameOutputLabel = QtWidgets.QLabel(OutputFieldView)
        self.nameOutputLabel.setGeometry(QtCore.QRect(30, 30, 59, 16))
        self.nameOutputLabel.setObjectName("nameOutputLabel")
        self.nameOutputField = QtWidgets.QLineEdit(OutputFieldView)
        self.nameOutputField.setGeometry(QtCore.QRect(110, 30, 481, 21))
        self.nameOutputField.setObjectName("nameOutputField")
        self.locationOutputField = QtWidgets.QLineEdit(OutputFieldView)
        self.locationOutputField.setGeometry(QtCore.QRect(110, 320, 481, 21))
        self.locationOutputField.setObjectName("locationOutputField")
        self.locationOutputLabel = QtWidgets.QLabel(OutputFieldView)
        self.locationOutputLabel.setGeometry(QtCore.QRect(30, 320, 59, 16))
        self.locationOutputLabel.setObjectName("locationOutputLabel")

        self.retranslateUi(OutputFieldView)
        QtCore.QMetaObject.connectSlotsByName(OutputFieldView)

    def retranslateUi(self, OutputFieldView):
        _translate = QtCore.QCoreApplication.translate
        OutputFieldView.setWindowTitle(_translate("OutputFieldView", "Output Field View"))
        self.generateOutputButton.setText(_translate("OutputFieldView", "Generate"))
        self.browseOutputButton.setText(_translate("OutputFieldView", "Browse"))
        self.descriptionOutputLabel.setText(_translate("OutputFieldView", "Description"))
        self.nameOutputLabel.setText(_translate("OutputFieldView", "Name"))
        self.locationOutputLabel.setText(_translate("OutputFieldView", "Location"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OutputFieldView = QtWidgets.QDialog()
    ui = Ui_OutputFieldView()
    ui.setupUi(OutputFieldView)
    OutputFieldView.show()
    sys.exit(app.exec_())
