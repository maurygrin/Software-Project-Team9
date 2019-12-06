import os, sys, r2pipe

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from Project import Project
from BinaryFile import BinaryFile
from Metadata import Metadata

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from pathlib import Path, PureWindowsPath

class DocumentationTab(object):

    #def __init__(self):

    def setupDocumentationTab(self, tab):
        self.tab = tab

        self.DocumentationViewContainer = QtWidgets.QGroupBox(self.tab)
        self.DocumentationViewContainer.setGeometry(QtCore.QRect(0, 0, 231, 621))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.DocumentationViewContainer.setFont(font)
        self.DocumentationViewContainer.setObjectName("DocumentationViewContainer")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.DocumentationViewContainer)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.DocumentationViewMainLayout = QtWidgets.QVBoxLayout()
        self.DocumentationViewMainLayout.setObjectName("DocumentationViewMainLayout")
        self.DocumentSearchLabel = QtWidgets.QLabel(self.DocumentationViewContainer)
        self.DocumentSearchLabel.setObjectName("DocumentSearchLabel")
        self.DocumentationViewMainLayout.addWidget(self.DocumentSearchLabel)
        self.documentSearch = QtWidgets.QLineEdit(self.DocumentationViewContainer)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.documentSearch.setFont(font)
        self.documentSearch.setObjectName("documentSearch")
        self.DocumentationViewMainLayout.addWidget(self.documentSearch)
        self.DocumentsLabel = QtWidgets.QLabel(self.DocumentationViewContainer)
        self.DocumentsLabel.setObjectName("DocumentsLabel")
        self.DocumentationViewMainLayout.addWidget(self.DocumentsLabel)
        self.documentList = QtWidgets.QListWidget(self.DocumentationViewContainer)
        self.documentList.setObjectName("documentList")
        self.DocumentationViewMainLayout.addWidget(self.documentList)
        self.gridLayout_5.addLayout(self.DocumentationViewMainLayout, 0, 0, 1, 1)
        self.DetailedDocumentationViewContainer = QtWidgets.QGroupBox(self.tab)
        self.DetailedDocumentationViewContainer.setGeometry(QtCore.QRect(240, 0, 981, 621))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.DetailedDocumentationViewContainer.setFont(font)
        self.DetailedDocumentationViewContainer.setObjectName("DetailedDocumentationViewContainer")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.DetailedDocumentationViewContainer)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.documentViewField = QtWidgets.QTextEdit(self.DetailedDocumentationViewContainer)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.documentViewField.setFont(font)
        self.documentViewField.setObjectName("documentViewField")
        self.gridLayout_4.addWidget(self.documentViewField, 0, 0, 1, 1)
        self.DocumentationButtonsLayout = QtWidgets.QHBoxLayout()
        self.DocumentationButtonsLayout.setObjectName("DocumentationButtonsLayout")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.DocumentationButtonsLayout.addItem(spacerItem20)
        self.saveDocumentButton = QtWidgets.QPushButton(self.DetailedDocumentationViewContainer)
        self.saveDocumentButton.setObjectName("saveDocumentButton")
        self.DocumentationButtonsLayout.addWidget(self.saveDocumentButton)
        self.restoreDocumentButton = QtWidgets.QPushButton(self.DetailedDocumentationViewContainer)
        self.restoreDocumentButton.setObjectName("restoreDocumentButton")
        self.DocumentationButtonsLayout.addWidget(self.restoreDocumentButton)
        self.gridLayout_4.addLayout(self.DocumentationButtonsLayout, 1, 0, 1, 1)

        return self.tab


    def retranslateDocumentationTab(self):

        _translate = QtCore.QCoreApplication.translate
        self.DocumentationViewContainer.setTitle(_translate("MainWindow", "Documentation View"))
        self.DocumentSearchLabel.setText(_translate("MainWindow", "Documentation Search"))
        self.DocumentsLabel.setText(_translate("MainWindow", "Documents"))
        self.DetailedDocumentationViewContainer.setTitle(_translate("MainWindow", "Detailed Documentation View"))
        self.saveDocumentButton.setText(_translate("MainWindow", "Save Document"))
        self.restoreDocumentButton.setText(_translate("MainWindow", "Restore Document"))
