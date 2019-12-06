from PyQt5 import QtCore, QtGui, QtWidgets

class PluginTab(object):

    def __init__(self):
        self.windowPlug = QtWidgets.QDialog()
        self.windowPluginError = QtWidgets.QDialog()
        self.windowPluginSelection = QtWidgets.QDialog()
        self.windowDatasetError = QtWidgets.QDialog()

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

    def setupUiCreatePlugin(self, newPlugin):
        newPlugin.setObjectName("newPlugin")
        newPlugin.resize(541, 369)
        self.buttonBox = QtWidgets.QDialogButtonBox(newPlugin)
        self.buttonBox.setGeometry(QtCore.QRect(370, 330, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.projectNameLabel = QtWidgets.QLabel(newPlugin)
        self.projectNameLabel.setGeometry(QtCore.QRect(20, 100, 81, 16))
        self.projectNameLabel.setObjectName("projectNameLabel")
        self.pluginNameEdit = QtWidgets.QTextEdit(newPlugin)
        self.pluginNameEdit.setGeometry(QtCore.QRect(20, 120, 431, 21))
        self.pluginNameEdit.setObjectName("pluginNameEdit")
        self.pluginDescriptionLabel = QtWidgets.QLabel(newPlugin)
        self.pluginDescriptionLabel.setGeometry(QtCore.QRect(20, 150, 131, 16))
        self.pluginDescriptionLabel.setObjectName("pluginDescriptionLabel")
        self.pluginDescriptionEdit = QtWidgets.QTextEdit(newPlugin)
        self.pluginDescriptionEdit.setGeometry(QtCore.QRect(20, 170, 431, 141))
        self.pluginDescriptionEdit.setObjectName("pluginDescriptionEdit")
        self.pluginStructlabel = QtWidgets.QLabel(newPlugin)
        self.pluginStructlabel.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.pluginStructlabel.setObjectName("pluginStructlabel")
        self.pluginDatasetLabel = QtWidgets.QLabel(newPlugin)
        self.pluginDatasetLabel.setGeometry(QtCore.QRect(20, 60, 81, 16))
        self.pluginDatasetLabel.setObjectName("pluginDatasetLabel")
        self.browseStructWindow = QtWidgets.QPushButton(newPlugin)
        self.browseStructWindow.setGeometry(QtCore.QRect(460, 40, 75, 23))
        self.browseStructWindow.setObjectName("browseStructWindow")
        self.brosweDSWindow = QtWidgets.QPushButton(newPlugin)
        self.brosweDSWindow.setGeometry(QtCore.QRect(460, 80, 75, 23))
        self.brosweDSWindow.setObjectName("brosweDSWindow")
        self.structureFieldWindow = QtWidgets.QTextBrowser(newPlugin)
        self.structureFieldWindow.setGeometry(QtCore.QRect(20, 40, 431, 21))
        self.structureFieldWindow.setObjectName("structureFieldWindow")
        self.datasetFieldWindow = QtWidgets.QTextBrowser(newPlugin)
        self.datasetFieldWindow.setGeometry(QtCore.QRect(20, 80, 431, 21))
        self.datasetFieldWindow.setObjectName("datasetFieldWindow")

        self.retranslateUiCreatePlugin(newPlugin)
        self.buttonBox.accepted.connect(newPlugin.accept)
        self.buttonBox.rejected.connect(newPlugin.reject)
        QtCore.QMetaObject.connectSlotsByName(newPlugin)

    def retranslateUiCreatePlugin(self, newPlugin):
        _translate = QtCore.QCoreApplication.translate
        newPlugin.setWindowTitle(_translate("newPlugin", "Create New Plugin"))
        self.projectNameLabel.setText(_translate("newPlugin", "Plugin Name"))
        self.pluginDescriptionLabel.setText(_translate("newPlugin", "Plugin Description"))
        self.pluginStructlabel.setText(_translate("newPlugin", "Plugin Structure"))
        self.pluginDatasetLabel.setText(_translate("newPlugin", "Plugin Dataset"))
        self.browseStructWindow.setText(_translate("newPlugin", "Browse"))
        self.brosweDSWindow.setText(_translate("newPlugin", "Browse"))

    def setupPluginError(self, pluginSelected):
        pluginSelected.setObjectName("pluginSelected")
        pluginSelected.resize(400, 99)
        self.buttonBox = QtWidgets.QDialogButtonBox(pluginSelected)
        self.buttonBox.setGeometry(QtCore.QRect(30, 60, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.messageLabel = QtWidgets.QLabel(pluginSelected)
        self.messageLabel.setGeometry(QtCore.QRect(30, 20, 371, 31))
        self.messageLabel.setObjectName("messageLabel")

        self.retranslatePluginError(pluginSelected)
        self.buttonBox.accepted.connect(pluginSelected.accept)
        QtCore.QMetaObject.connectSlotsByName(pluginSelected)

    def retranslatePluginError(self, pluginSelected):
        _translate = QtCore.QCoreApplication.translate
        pluginSelected.setWindowTitle(_translate("pluginSelected", "Error Message: Plugin Selected"))
        self.messageLabel.setText(
            _translate("pluginSelected", "You need to select a plugin before running an analysis."))

    def setupUiPluginSelection(self, PluginSelection):
        PluginSelection.setObjectName("PluginSelection")
        PluginSelection.resize(306, 99)
        PluginSelection.setMinimumSize(QtCore.QSize(306, 99))
        PluginSelection.setMaximumSize(QtCore.QSize(306, 99))
        self.PluginSelectionMainLayout = QtWidgets.QGridLayout(PluginSelection)
        self.PluginSelectionMainLayout.setObjectName("PluginSelectionMainLayout")
        self.PluginSelectionLayout = QtWidgets.QVBoxLayout()
        self.PluginSelectionLayout.setObjectName("PluginSelectionLayout")
        self.PluginSelectionLabel = QtWidgets.QLabel(PluginSelection)
        self.PluginSelectionLabel.setObjectName("PluginSelectionLabel")
        self.PluginSelectionLayout.addWidget(self.PluginSelectionLabel)
        self.PluginSelectionButtonbox = QtWidgets.QDialogButtonBox(PluginSelection)
        self.PluginSelectionButtonbox.setOrientation(QtCore.Qt.Horizontal)
        self.PluginSelectionButtonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.PluginSelectionButtonbox.setObjectName("PluginSelectionButtonbox")
        self.PluginSelectionLayout.addWidget(self.PluginSelectionButtonbox)
        self.PluginSelectionMainLayout.addLayout(self.PluginSelectionLayout, 0, 0, 1, 1)

        self.retranslateUiPluginSelection(PluginSelection)
        self.PluginSelectionButtonbox.accepted.connect(PluginSelection.accept)
        self.PluginSelectionButtonbox.rejected.connect(PluginSelection.reject)
        QtCore.QMetaObject.connectSlotsByName(PluginSelection)

    def retranslateUiPluginSelection(self, PluginSelection):
        _translate = QtCore.QCoreApplication.translate
        PluginSelection.setWindowTitle(_translate("PluginSelection", "Error Message: Plugin Selected"))
        self.PluginSelectionLabel.setText(_translate("PluginSelection", "Fill out missing fields to create plugin."))

    def setupUiDatasetError(self, PluginDatasetError):
        PluginDatasetError.setObjectName("PluginDatasetError")
        PluginDatasetError.resize(311, 99)
        PluginDatasetError.setMinimumSize(QtCore.QSize(311, 99))
        PluginDatasetError.setMaximumSize(QtCore.QSize(311, 99))
        self.PluginDatasetErrorMainLayout = QtWidgets.QGridLayout(PluginDatasetError)
        self.PluginDatasetErrorMainLayout.setObjectName("PluginDatasetErrorMainLayout")
        self.PluginDatasetErrorLayout = QtWidgets.QVBoxLayout()
        self.PluginDatasetErrorLayout.setObjectName("PluginDatasetErrorLayout")
        self.PluginDatasetErrorLabel = QtWidgets.QLabel(PluginDatasetError)
        self.PluginDatasetErrorLabel.setObjectName("PluginDatasetErrorLabel")
        self.PluginDatasetErrorLayout.addWidget(self.PluginDatasetErrorLabel)
        self.PluginDatasetErrorButtonbox = QtWidgets.QDialogButtonBox(PluginDatasetError)
        self.PluginDatasetErrorButtonbox.setOrientation(QtCore.Qt.Horizontal)
        self.PluginDatasetErrorButtonbox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.PluginDatasetErrorButtonbox.setObjectName("PluginDatasetErrorButtonbox")
        self.PluginDatasetErrorLayout.addWidget(self.PluginDatasetErrorButtonbox)
        self.PluginDatasetErrorMainLayout.addLayout(self.PluginDatasetErrorLayout, 0, 0, 1, 1)

        self.retranslateUiDatasetError(PluginDatasetError)
        self.PluginDatasetErrorButtonbox.accepted.connect(PluginDatasetError.accept)
        self.PluginDatasetErrorButtonbox.rejected.connect(PluginDatasetError.reject)
        QtCore.QMetaObject.connectSlotsByName(PluginDatasetError)

    def retranslateUiDatasetError(self, PluginDatasetError):
        _translate = QtCore.QCoreApplication.translate
        PluginDatasetError.setWindowTitle(_translate("PluginDatasetError", "Error Message: Predefined Data Set"))
        self.PluginDatasetErrorLabel.setText(_translate("PluginDatasetError", "The plugin predefined data set is not valid."))