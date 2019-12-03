import os, sys, r2pipe

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from Project import Project
from BinaryFile import BinaryFile
from Metadata import Metadata

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from pathlib import Path, PureWindowsPath

class PluginTab(object):

    #def __init__(self):

    def setupPluginTab(self, tab):
        self.tab = tab
        self.PluginViewContainer = QtWidgets.QGroupBox(self.tab)
        self.PluginViewContainer.setGeometry(QtCore.QRect(0, 0, 231, 621))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.PluginViewContainer.setFont(font)
        self.PluginViewContainer.setObjectName("PluginViewContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.PluginViewContainer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pluginsearchlabel = QtWidgets.QLabel(self.PluginViewContainer)
        self.pluginsearchlabel.setObjectName("pluginsearchlabel")
        self.verticalLayout.addWidget(self.pluginsearchlabel)
        self.pluginSearch = QtWidgets.QLineEdit(self.PluginViewContainer)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pluginSearch.setFont(font)
        self.pluginSearch.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pluginSearch.setObjectName("pluginSearch")
        self.verticalLayout.addWidget(self.pluginSearch)
        self.pluginslabel = QtWidgets.QLabel(self.PluginViewContainer)
        self.pluginslabel.setObjectName("pluginslabel")
        self.verticalLayout.addWidget(self.pluginslabel)
        self.pluginManagementList = QtWidgets.QListWidget(self.PluginViewContainer)
        self.pluginManagementList.setObjectName("pluginManagementList")
        self.verticalLayout.addWidget(self.pluginManagementList)
        self.pluginviewbuttonslayout = QtWidgets.QHBoxLayout()
        self.pluginviewbuttonslayout.setObjectName("pluginviewbuttonslayout")
        self.newPluginButton = QtWidgets.QPushButton(self.PluginViewContainer)
        self.newPluginButton.setObjectName("newPluginButton")
        self.pluginviewbuttonslayout.addWidget(self.newPluginButton)
        self.deletePluginButton = QtWidgets.QPushButton(self.PluginViewContainer)
        self.deletePluginButton.setObjectName("deletePluginButton")
        self.pluginviewbuttonslayout.addWidget(self.deletePluginButton)
        self.verticalLayout.addLayout(self.pluginviewbuttonslayout)
        self.DetailedPluginViewContainer = QtWidgets.QGroupBox(self.tab)
        self.DetailedPluginViewContainer.setGeometry(QtCore.QRect(240, 0, 981, 621))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.DetailedPluginViewContainer.setFont(font)
        self.DetailedPluginViewContainer.setObjectName("DetailedPluginViewContainer")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.DetailedPluginViewContainer)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pluginstructurelayout = QtWidgets.QHBoxLayout()
        self.pluginstructurelayout.setObjectName("pluginstructurelayout")
        self.pluginstructurelabel = QtWidgets.QLabel(self.DetailedPluginViewContainer)
        self.pluginstructurelabel.setObjectName("pluginstructurelabel")
        self.pluginstructurelayout.addWidget(self.pluginstructurelabel)
        spacerItem11 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.pluginstructurelayout.addItem(spacerItem11)
        self.pluginStructureField = QtWidgets.QLineEdit(self.DetailedPluginViewContainer)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pluginStructureField.setFont(font)
        self.pluginStructureField.setObjectName("pluginStructureField")
        self.pluginstructurelayout.addWidget(self.pluginStructureField)
        self.verticalLayout_5.addLayout(self.pluginstructurelayout)
        self.pluginpredefineddatasetlayout = QtWidgets.QHBoxLayout()
        self.pluginpredefineddatasetlayout.setObjectName("pluginpredefineddatasetlayout")
        self.pluginpredefineddatasetlabel = QtWidgets.QLabel(self.DetailedPluginViewContainer)
        self.pluginpredefineddatasetlabel.setObjectName("pluginpredefineddatasetlabel")
        self.pluginpredefineddatasetlayout.addWidget(self.pluginpredefineddatasetlabel)
        self.pluginPredefinedField = QtWidgets.QLineEdit(self.DetailedPluginViewContainer)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pluginPredefinedField.setFont(font)
        self.pluginPredefinedField.setObjectName("pluginPredefinedField")
        self.pluginpredefineddatasetlayout.addWidget(self.pluginPredefinedField)
        self.verticalLayout_5.addLayout(self.pluginpredefineddatasetlayout)
        self.pluginnamelayout = QtWidgets.QHBoxLayout()
        self.pluginnamelayout.setObjectName("pluginnamelayout")
        self.pluginnamelabel = QtWidgets.QLabel(self.DetailedPluginViewContainer)
        self.pluginnamelabel.setObjectName("pluginnamelabel")
        self.pluginnamelayout.addWidget(self.pluginnamelabel)
        spacerItem12 = QtWidgets.QSpacerItem(81, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.pluginnamelayout.addItem(spacerItem12)
        self.pluginNameField = QtWidgets.QLineEdit(self.DetailedPluginViewContainer)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pluginNameField.setFont(font)
        self.pluginNameField.setObjectName("pluginNameField")
        self.pluginnamelayout.addWidget(self.pluginNameField)
        self.verticalLayout_5.addLayout(self.pluginnamelayout)
        self.plugindescriptionlayout = QtWidgets.QHBoxLayout()
        self.plugindescriptionlayout.setObjectName("plugindescriptionlayout")
        self.plugindescriptionlabel = QtWidgets.QLabel(self.DetailedPluginViewContainer)
        self.plugindescriptionlabel.setObjectName("plugindescriptionlabel")
        self.plugindescriptionlayout.addWidget(self.plugindescriptionlabel)
        spacerItem13 = QtWidgets.QSpacerItem(47, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.plugindescriptionlayout.addItem(spacerItem13)
        self.pluginDescriptionField = QtWidgets.QTextEdit(self.DetailedPluginViewContainer)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pluginDescriptionField.setFont(font)
        self.pluginDescriptionField.setObjectName("pluginDescriptionField")
        self.plugindescriptionlayout.addWidget(self.pluginDescriptionField)
        self.verticalLayout_5.addLayout(self.plugindescriptionlayout)
        self.DefaultOutputFieldLayout = QtWidgets.QHBoxLayout()
        self.DefaultOutputFieldLayout.setObjectName("DefaultOutputFieldLayout")
        self.defaultoutputfieldlabel = QtWidgets.QLabel(self.DetailedPluginViewContainer)
        self.defaultoutputfieldlabel.setObjectName("defaultoutputfieldlabel")
        self.DefaultOutputFieldLayout.addWidget(self.defaultoutputfieldlabel)
        self.outputFieldDropDown = QtWidgets.QComboBox(self.DetailedPluginViewContainer)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.outputFieldDropDown.setFont(font)
        self.outputFieldDropDown.setObjectName("outputFieldDropDown")
        self.outputFieldDropDown.addItem("")
        self.DefaultOutputFieldLayout.addWidget(self.outputFieldDropDown)
        spacerItem14 = QtWidgets.QSpacerItem(620, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.DefaultOutputFieldLayout.addItem(spacerItem14)
        self.verticalLayout_5.addLayout(self.DefaultOutputFieldLayout)
        self.PointsOfInterestPluginLayout = QtWidgets.QHBoxLayout()
        self.PointsOfInterestPluginLayout.setObjectName("PointsOfInterestPluginLayout")
        self.poipluginlabel = QtWidgets.QLabel(self.DetailedPluginViewContainer)
        self.poipluginlabel.setObjectName("poipluginlabel")
        self.PointsOfInterestPluginLayout.addWidget(self.poipluginlabel)
        spacerItem15 = QtWidgets.QSpacerItem(56, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.PointsOfInterestPluginLayout.addItem(spacerItem15)
        self.poiPluginField = QtWidgets.QTextEdit(self.DetailedPluginViewContainer)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.poiPluginField.setFont(font)
        self.poiPluginField.setObjectName("poiPluginField")
        self.PointsOfInterestPluginLayout.addWidget(self.poiPluginField)
        self.verticalLayout_5.addLayout(self.PointsOfInterestPluginLayout)
        self.pluginbuttonslayout = QtWidgets.QHBoxLayout()
        self.pluginbuttonslayout.setObjectName("pluginbuttonslayout")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.pluginbuttonslayout.addItem(spacerItem16)
        self.XMLEditorButton = QtWidgets.QPushButton(self.DetailedPluginViewContainer)
        self.XMLEditorButton.setObjectName("XMLEditorButton")
        self.pluginbuttonslayout.addWidget(self.XMLEditorButton)
        self.savePluginButton = QtWidgets.QPushButton(self.DetailedPluginViewContainer)
        self.savePluginButton.setObjectName("savePluginButton")
        self.pluginbuttonslayout.addWidget(self.savePluginButton)
        self.verticalLayout_5.addLayout(self.pluginbuttonslayout)
        return self.tab


    def retranslatePluginTab(self):

        _translate = QtCore.QCoreApplication.translate
        self.PluginViewContainer.setTitle(_translate("MainWindow", "Plugin View"))
        self.pluginsearchlabel.setText(_translate("MainWindow", "Plugin Search"))
        self.pluginslabel.setText(_translate("MainWindow", "Plugins"))
        self.newPluginButton.setText(_translate("MainWindow", "New"))
        self.deletePluginButton.setText(_translate("MainWindow", "Delete"))
        self.DetailedPluginViewContainer.setTitle(_translate("MainWindow", "Detailed Plugin View"))
        self.pluginstructurelabel.setText(_translate("MainWindow", "Plugin Structure"))
        self.pluginpredefineddatasetlabel.setText(_translate("MainWindow", "Plugin Predefined Dataset"))
        self.pluginnamelabel.setText(_translate("MainWindow", "Plugin Name"))
        self.plugindescriptionlabel.setText(_translate("MainWindow", "Plugin Description"))
        self.defaultoutputfieldlabel.setText(_translate("MainWindow", "Default Output Field"))
        self.outputFieldDropDown.setItemText(0, _translate("MainWindow", "Default Output Field"))
        self.poipluginlabel.setText(_translate("MainWindow", "Points of Interest"))
        self.XMLEditorButton.setText(_translate("MainWindow", "XML Editor"))
        self.savePluginButton.setText(_translate("MainWindow", "Save"))