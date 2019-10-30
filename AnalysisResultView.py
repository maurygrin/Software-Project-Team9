# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnalysisResultView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_analysisResultView(object):
    def setupUi(self, analysisResultView):
        analysisResultView.setObjectName("analysisResultView")
        analysisResultView.resize(616, 402)
        self.analysisList = QtWidgets.QListView(analysisResultView)
        self.analysisList.setGeometry(QtCore.QRect(20, 70, 181, 271))
        self.analysisList.setObjectName("analysisList")
        self.deleteAnalysisButton = QtWidgets.QPushButton(analysisResultView)
        self.deleteAnalysisButton.setGeometry(QtCore.QRect(480, 360, 113, 32))
        self.deleteAnalysisButton.setObjectName("deleteAnalysisButton")
        self.saveAnalysisButton = QtWidgets.QPushButton(analysisResultView)
        self.saveAnalysisButton.setGeometry(QtCore.QRect(330, 360, 113, 32))
        self.saveAnalysisButton.setObjectName("saveAnalysisButton")
        self.newAnalysisButton = QtWidgets.QPushButton(analysisResultView)
        self.newAnalysisButton.setGeometry(QtCore.QRect(90, 360, 113, 32))
        self.newAnalysisButton.setObjectName("newAnalysisButton")
        self.analysisViewGroup = QtWidgets.QGroupBox(analysisResultView)
        self.analysisViewGroup.setGeometry(QtCore.QRect(220, 10, 371, 331))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.analysisViewGroup.setFont(font)
        self.analysisViewGroup.setObjectName("analysisViewGroup")
        self.nameAnalysisField = QtWidgets.QLineEdit(self.analysisViewGroup)
        self.nameAnalysisField.setGeometry(QtCore.QRect(100, 40, 251, 21))
        self.nameAnalysisField.setObjectName("nameAnalysisField")
        self.nameAnalysisLabel = QtWidgets.QLabel(self.analysisViewGroup)
        self.nameAnalysisLabel.setGeometry(QtCore.QRect(20, 40, 59, 16))
        self.nameAnalysisLabel.setObjectName("nameAnalysisLabel")
        self.descriptionAnalysisField = QtWidgets.QTextEdit(self.analysisViewGroup)
        self.descriptionAnalysisField.setGeometry(QtCore.QRect(100, 80, 251, 221))
        self.descriptionAnalysisField.setObjectName("descriptionAnalysisField")
        self.descriptionAnalysisLabel = QtWidgets.QLabel(self.analysisViewGroup)
        self.descriptionAnalysisLabel.setGeometry(QtCore.QRect(20, 80, 81, 16))
        self.descriptionAnalysisLabel.setObjectName("descriptionAnalysisLabel")
        self.analysisSearch = QtWidgets.QTextEdit(analysisResultView)
        self.analysisSearch.setGeometry(QtCore.QRect(20, 30, 181, 31))
        self.analysisSearch.setObjectName("analysisSearch")
        self.glass = QtWidgets.QLabel(analysisResultView)
        self.glass.setGeometry(QtCore.QRect(150, 30, 51, 31))
        self.glass.setText("")
        self.glass.setPixmap(QtGui.QPixmap("../../cliparts-for-powerpoint-transparent-magnifying-glass-md.png"))
        self.glass.setScaledContents(True)
        self.glass.setObjectName("glass")
        self.analysisSearchButton = QtWidgets.QPushButton(analysisResultView)
        self.analysisSearchButton.setGeometry(QtCore.QRect(140, 30, 61, 31))
        self.analysisSearchButton.setObjectName("analysisSearchButton")

        self.retranslateUi(analysisResultView)
        QtCore.QMetaObject.connectSlotsByName(analysisResultView)

    def retranslateUi(self, analysisResultView):
        _translate = QtCore.QCoreApplication.translate
        analysisResultView.setWindowTitle(_translate("analysisResultView", "Analysis Result View"))
        self.deleteAnalysisButton.setText(_translate("analysisResultView", "- Delete"))
        self.saveAnalysisButton.setText(_translate("analysisResultView", "+ Save"))
        self.newAnalysisButton.setText(_translate("analysisResultView", "New"))
        self.analysisViewGroup.setTitle(_translate("analysisResultView", "Analysis Result Area"))
        self.nameAnalysisLabel.setText(_translate("analysisResultView", "Name"))
        self.descriptionAnalysisLabel.setText(_translate("analysisResultView", "Description"))
        self.analysisSearch.setHtml(_translate("analysisResultView", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-style:italic; color:#7e7e7e;\">Analysis Search</span></p></body></html>"))
        self.analysisSearchButton.setText(_translate("analysisResultView", "🔍 "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    analysisResultView = QtWidgets.QDialog()
    ui = Ui_analysisResultView()
    ui.setupUi(analysisResultView)
    analysisResultView.show()
    sys.exit(app.exec_())
