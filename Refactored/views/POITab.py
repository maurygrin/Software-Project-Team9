import os, sys, r2pipe

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from Project import Project
from BinaryFile import BinaryFile
from Metadata import Metadata

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from pathlib import Path, PureWindowsPath

class POITab(object):

    def __init__(self):
        self.windowPOI = QtWidgets.QDialog()

    def setupPOITab(self, tab):
        self.tab = tab

        self.PointsOfInterestViewContainer = QtWidgets.QGroupBox(self.tab)
        self.PointsOfInterestViewContainer.setGeometry(QtCore.QRect(0, 0, 231, 621))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.PointsOfInterestViewContainer.setFont(font)
        self.PointsOfInterestViewContainer.setObjectName("PointsOfInterestViewContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.PointsOfInterestViewContainer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PointsOfInterestViewLayout = QtWidgets.QVBoxLayout()
        self.PointsOfInterestViewLayout.setObjectName("PointsOfInterestViewLayout")
        self.poisearchlabel = QtWidgets.QLabel(self.PointsOfInterestViewContainer)
        self.poisearchlabel.setObjectName("poisearchlabel")
        self.PointsOfInterestViewLayout.addWidget(self.poisearchlabel)
        self.poiSearch = QtWidgets.QLineEdit(self.PointsOfInterestViewContainer)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.poiSearch.setFont(font)
        self.poiSearch.setObjectName("poiSearch")
        self.PointsOfInterestViewLayout.addWidget(self.poiSearch)
        self.poipoilabel = QtWidgets.QLabel(self.PointsOfInterestViewContainer)
        self.poipoilabel.setObjectName("poipoilabel")
        self.PointsOfInterestViewLayout.addWidget(self.poipoilabel)
        self.poiList = QtWidgets.QListWidget(self.PointsOfInterestViewContainer)
        self.poiList.setObjectName("poiList")
        self.PointsOfInterestViewLayout.addWidget(self.poiList)
        self.verticalLayout_2.addLayout(self.PointsOfInterestViewLayout)
        self.PointsOfInterestButtonsLayout = QtWidgets.QHBoxLayout()
        self.PointsOfInterestButtonsLayout.setObjectName("PointsOfInterestButtonsLayout")
        self.newPOIButton = QtWidgets.QPushButton(self.PointsOfInterestViewContainer)
        self.newPOIButton.setObjectName("newPOIButton")
        self.PointsOfInterestButtonsLayout.addWidget(self.newPOIButton)
        self.poiDeleteButton = QtWidgets.QPushButton(self.PointsOfInterestViewContainer)
        self.poiDeleteButton.setObjectName("poiDeleteButton")
        self.PointsOfInterestButtonsLayout.addWidget(self.poiDeleteButton)
        self.verticalLayout_2.addLayout(self.PointsOfInterestButtonsLayout)
        self.DetailedPointsOfInterestViewContainer = QtWidgets.QGroupBox(self.tab)
        self.DetailedPointsOfInterestViewContainer.setGeometry(QtCore.QRect(240, 20, 981, 601))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.DetailedPointsOfInterestViewContainer.setFont(font)
        self.DetailedPointsOfInterestViewContainer.setTitle("")
        self.DetailedPointsOfInterestViewContainer.setObjectName("DetailedPointsOfInterestViewContainer")
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.DetailedPointsOfInterestViewContainer)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(15, 57, 951, 32))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.POIFilterLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.POIFilterLayout.setContentsMargins(0, 0, 0, 0)
        self.POIFilterLayout.setObjectName("POIFilterLayout")
        self.poifilterlabel = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        self.poifilterlabel.setObjectName("poifilterlabel")
        self.POIFilterLayout.addWidget(self.poifilterlabel)
        self.poiFilterDropDown = QtWidgets.QComboBox(self.horizontalLayoutWidget_9)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.poiFilterDropDown.setFont(font)
        self.poiFilterDropDown.setObjectName("poiFilterDropDown")
        self.poiFilterDropDown.addItem("")
        self.POIFilterLayout.addWidget(self.poiFilterDropDown)
        spacerItem17 = QtWidgets.QSpacerItem(799, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.POIFilterLayout.addItem(spacerItem17)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.DetailedPointsOfInterestViewContainer)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(15, 99, 951, 441))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.detailedpoilayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.detailedpoilayout.setContentsMargins(0, 0, 0, 0)
        self.detailedpoilayout.setObjectName("detailedpoilayout")
        self.detailedpoiviewlabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.detailedpoiviewlabel.setFont(font)
        self.detailedpoiviewlabel.setObjectName("detailedpoiviewlabel")
        self.detailedpoilayout.addWidget(self.detailedpoiviewlabel)
        self.poiViewField = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.poiViewField.setFont(font)
        self.poiViewField.setObjectName("poiViewField")
        self.detailedpoilayout.addWidget(self.poiViewField)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.DetailedPointsOfInterestViewContainer)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(15, 553, 951, 32))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.POIButtonsLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.POIButtonsLayout.setContentsMargins(0, 0, 0, 0)
        self.POIButtonsLayout.setObjectName("POIButtonsLayout")
        spacerItem18 = QtWidgets.QSpacerItem(4040, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.POIButtonsLayout.addItem(spacerItem18)
        self.poiSaveButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_10)
        self.poiSaveButton.setObjectName("poiSaveButton")
        self.POIButtonsLayout.addWidget(self.poiSaveButton)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.DetailedPointsOfInterestViewContainer)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(15, 15, 951, 32))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.POIPluginLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.POIPluginLayout.setContentsMargins(0, 0, 0, 0)
        self.POIPluginLayout.setObjectName("POIPluginLayout")
        self.POIPluginLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        self.POIPluginLabel.setObjectName("POIPluginLabel")
        self.POIPluginLayout.addWidget(self.POIPluginLabel)
        self.poiPluginDropDown = QtWidgets.QComboBox(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.poiPluginDropDown.setFont(font)
        self.poiPluginDropDown.setObjectName("poiPluginDropDown")
        self.poiPluginDropDown.addItem("")
        self.POIPluginLayout.addWidget(self.poiPluginDropDown)
        spacerItem19 = QtWidgets.QSpacerItem(800, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.POIPluginLayout.addItem(spacerItem19)

        return self.tab

    def retranslatePOITab(self):

        _translate = QtCore.QCoreApplication.translate
        self.PointsOfInterestViewContainer.setTitle(_translate("MainWindow", "Points of Interest View"))
        self.poisearchlabel.setText(_translate("MainWindow", "Points of Interest Search"))
        self.poipoilabel.setText(_translate("MainWindow", "Points of Interest"))
        self.newPOIButton.setText(_translate("MainWindow", "New"))
        self.poiDeleteButton.setText(_translate("MainWindow", "Delete"))
        self.poifilterlabel.setText(_translate("MainWindow", "POI Filter"))
        self.poiFilterDropDown.setItemText(0, _translate("MainWindow", "Select"))
        self.detailedpoiviewlabel.setText(_translate("MainWindow", "Detailed Points of Interest View"))
        self.poiViewField.setHtml(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p></body></html>"))
        self.poiSaveButton.setText(_translate("MainWindow", "     Save     "))
        self.POIPluginLabel.setText(_translate("MainWindow", "Plugin"))
        self.poiPluginDropDown.setItemText(0, _translate("MainWindow", "Select"))

    def setupUiPOI(self, NewPOI):
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
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
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

        self.retranslateUiPOI(NewPOI)
        QtCore.QMetaObject.connectSlotsByName(NewPOI)

    def retranslateUiPOI(self, NewPOI):
        _translate = QtCore.QCoreApplication.translate
        NewPOI.setWindowTitle(_translate("NewPOI", "New POI"))
        self.poiTypeLabel.setText(_translate("NewPOI", "Poin Of Interest Description"))
        self.poiOutLabel.setText(_translate("NewPOI", "Python Output"))
        self.poiNameLabel.setText(_translate("NewPOI", "Point Of Interest Name"))