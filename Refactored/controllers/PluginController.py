from PluginSub.Plugin import Plugin

from PyQt5 import QtCore, QtWidgets
import xml.etree.cElementTree as ET


class PluginController(object):

    def __init__(self, plugin_tab, poi_tab, analysis_tab, db, poiController, documentController, document_tab):
        self.plugin_tab = plugin_tab
        self.documentController= documentController
        self.poiController = poiController
        self.document_tab = document_tab
        self.db = db
        self.plugin_tab.newPluginButton.clicked.connect(self.pluginWindow)
        self.plugin_tab.pluginStructureField.setEnabled(False)
        self.plugin_tab.pluginPredefinedField.setEnabled(False)
        self.plugin_tab.pluginNameField.setEnabled(False)
        self.plugin_tab.deletePluginButton.setEnabled(False)
        self.plugin_tab.pluginManagementList.clicked.connect(self.pluginClicked)
        self.plugin_tab.deletePluginButton.clicked.connect(self.deletePlugin)

        self.plugin_tab.pluginSearch.textChanged[str].connect(self.filter_plugins)

        self.poi_tab = poi_tab

        self.analysis_tab = analysis_tab

        self.db.findPlugins(self.plugin_tab)

        self.list = []
        self.listStrings = []
        self.listFunctions = []
        self.plugin_tab.savePluginButton.setEnabled(False)


    def pluginSelectionWindow(self):
        self.plugin_tab.setupUiPluginSelection(self.plugin_tab.windowPluginSelection)
        self.plugin_tab.windowPluginSelection.show()

    def pluginDatasetWindow(self):
        self.plugin_tab.setupUiDatasetError(self.plugin_tab.windowDatasetError)
        self.plugin_tab.windowDatasetError.show()

    def pluginWindow(self):
        self.plugin_tab.setupUiCreatePlugin(self.plugin_tab.windowPlug)
        self.plugin_tab.windowPlug.show()
        self.plugin_tab.brosweDSWindow.clicked.connect(self.BrowseDataSet)
        self.plugin_tab.browseStructWindow.clicked.connect(self.BrowseStruct)

        self.plugin_tab.buttonBox.accepted.connect(
            lambda: self.createPlugin(self.plugin_tab.pluginNameEdit.toPlainText(), self.plugin_tab.pluginDescriptionEdit.toPlainText(),
                                      self.plugin_tab.structureFieldWindow.toPlainText(),
                                      self.plugin_tab.datasetFieldWindow.toPlainText()))

    def createPlugin(self, name, description, structure, data_set):
        if not name or not description or not structure or not data_set:
            self.pluginSelectionWindow()
        else:
            self.plugin_tab.poiPluginField.clear()
            self.plugin_tab.poiPluginField.repaint()
            self.plugin = Plugin(name, description, structure, data_set)
            self.plugin_tab.pluginNameField.setText(self.plugin.name)
            self.plugin_tab.pluginDescriptionField.setText(self.plugin.description)
            self.plugin_tab.pluginStructureField.setText(self.plugin.structure)
            self.plugin_tab.pluginPredefinedField.setText(self.plugin.data_set)
            self.analysis_tab.pluginDropDownAnalysis.addItem(self.plugin.name)

            self.analysis_tab.poiTypeDropDownAnalysis.clear()
            self.analysis_tab.poiTypeDropDownAnalysis.repaint()
            self.analysis_tab.poiTypeDropDownAnalysis.addItem("Select")
            self.analysis_tab.poiTypeDropDownAnalysis.addItem(self.list[4])
            self.analysis_tab.poiTypeDropDownAnalysis.addItem(self.list[5])

            self.plugin_tab.outputFieldDropDown.clear()
            self.plugin_tab.outputFieldDropDown.addItem(self.list[2])
            print(self.list[2])
            self.plugin_tab.outputFieldDropDown.repaint()

            self.analysis_tab.pluginDropDownAnalysis.clear()
            self.analysis_tab.pluginDropDownAnalysis.repaint()
            self.analysis_tab.pluginDropDownAnalysis.addItem(self.list[0])

            self.poi_tab.poiPluginDropDown.clear()
            self.poi_tab.poiPluginDropDown.repaint()
            self.poi_tab.poiPluginDropDown.addItem(self.list[0])

            self.poi_tab.poiFilterDropDown.clear()
            self.poi_tab.poiFilterDropDown.repaint()
            self.poi_tab.poiFilterDropDown.addItem("Select")
            self.poi_tab.poiFilterDropDown.addItem(self.list[4])
            self.poi_tab.poiFilterDropDown.addItem(self.list[5])

            self.plugin_tab.poiPluginField.setText(self.listFunctions[0])

            self.savePlugin()

    def BrowseStruct(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.plugin_tab.structureFieldWindow, "Browse XML Schema", "",
                                                            "XML Schemas Files (*.xsd)", options=options)
        if fileName:
            self.plugin_tab.structureFieldWindow.setText(fileName)

    def BrowseDataSet(self):
        try:
            options = QtWidgets.QFileDialog.Options()
            options |= QtWidgets.QFileDialog.DontUseNativeDialog
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.plugin_tab.datasetFieldWindow, "Browse XML File", "",
                                                                "XML Files (*.xml)", options=options)
            if fileName:
                self.listStrings.clear()
                self.list.clear()
                self.listFunctions.clear()
                self.plugin_tab.datasetFieldWindow.setText(fileName)
                self.parseXML(fileName)
                self.plugin_tab.pluginNameEdit.setText(self.list[0])
                self.plugin_tab.pluginDescriptionEdit.setText(self.list[1])
        except Exception as e:
            self.pluginDatasetWindow()
            self.plugin_tab.datasetFieldWindow.clear()


    def savePlugin(self):
        pluginDB = {"Plugin Name": self.plugin.name,
                    "Plugin Description": self.plugin.description,
                    "Structure File Path": self.plugin.structure,
                    "Pre-Defined Dataset File Path": self.plugin.data_set,
                    "Plugin Output": self.list[2],
                    "POI Strings": self.list[4],
                    "POI Functions": self.list[5],
                    "Strings": [],  # Nested Document
                    "Functions": []  # Nested Document
                    }

        i = 0
        while i < len(self.listStrings):
            docStrings = {
                "Name": self.listStrings[i],
                "Type": self.listStrings[i + 1],
                "Output": self.listStrings[i + 2]
            }
            if (self.poi_tab.poiPluginDropDown.currentText() == self.list[0]):
                self.plugin_tab.poiPluginField.append(str(docStrings))
            pluginDB["Strings"].append(docStrings)  # Insert Nested Document
            self.plugin_tab.poiPluginField.append(self.listStrings[i])
            i += 3

        i = 0
        while i < len(self.listFunctions):
            docFunctions = {
                "Name": self.listFunctions[i],
                "Type": self.listFunctions[i + 1],
                "Output": self.listFunctions[i + 2]
            }
            if (self.poi_tab.poiPluginDropDown.currentText() == self.plugin.name):
                self.plugin_tab.poiPluginField.append(str(docFunctions))
            i += 3
            pluginDB["Functions"].append(docFunctions)  # Insert Nested Document
        self.db.insertPlugin(pluginDB)

        it = QtWidgets.QListWidgetItem(self.plugin.name)
        self.plugin_tab.pluginManagementList.addItem(it)
        self.plugin_tab.pluginManagementList.setCurrentItem(it)
        it.setSelected(True)
        currentDocument = self.document_tab.documentList.currentItem()
        self.documentController.hidePluginStructure(False)

        if currentDocument is not None:
            if currentDocument.text() == "Plugin Structure":
                self.document_tab.loadPluginStructureDocumentation()
        #self.retranslateUi(MainWindow)

    def deletePlugin(self):
        p = self.db.findPlugin("Plugin Name", self.plugin_tab.pluginManagementList.currentItem().text())
        self.db.deletePlugin(p)
        self.plugin_tab.pluginManagementList.takeItem(self.plugin_tab.pluginManagementList.currentRow())
        self.plugin_tab.pluginNameField.clear()
        self.plugin_tab.pluginDescriptionField.clear()
        self.plugin_tab.pluginStructureField.clear()
        self.plugin_tab.pluginPredefinedField.clear()
        self.plugin_tab.pluginNameField.repaint()
        self.plugin_tab.pluginDescriptionField.repaint()
        self.plugin_tab.pluginStructureField.repaint()
        self.plugin_tab.pluginPredefinedField.repaint()
        self.plugin_tab.poiPluginField.clear()
        self.plugin_tab.poiPluginField.repaint()
        self.poi_tab.poiList.clear()
        self.poi_tab.poiList.repaint()

        self.plugin_tab.outputFieldDropDown.clear()
        self.plugin_tab.outputFieldDropDown.repaint()
        self.plugin_tab.outputFieldDropDown.addItem("Output Field")

        self.poi_tab.poiFilterDropDown.clear()
        self.poi_tab.poiFilterDropDown.repaint()
        self.poi_tab.poiFilterDropDown.addItem("Select")

        self.analysis_tab.poiTypeDropDownAnalysis.clear()
        self.analysis_tab.poiTypeDropDownAnalysis.repaint()
        self.analysis_tab.poiTypeDropDownAnalysis.addItem("Select")

        self.analysis_tab.pluginDropDownAnalysis.clear()
        self.analysis_tab.pluginDropDownAnalysis.repaint()
        self.analysis_tab.pluginDropDownAnalysis.addItem("Select")

        self.poi_tab.poiPluginDropDown.clear()
        self.poi_tab.poiPluginDropDown.repaint()
        self.poi_tab.poiPluginDropDown.addItem("Select")

    def pluginClicked(self):
        self.listStrings.clear()
        self.listFunctions.clear()
        self.plugin_tab.deletePluginButton.setEnabled(True)
        self.plugin_tab.outputFieldDropDown.clear()
        self.plugin_tab.outputFieldDropDown.repaint()
        self.poi_tab.poiViewField.clear()
        self.poi_tab.poiViewField.repaint()
        plugin = self.db.findPlugin("Plugin Name", self.plugin_tab.pluginManagementList.currentItem().text())
        self.plugin_tab.poiPluginField.clear()
        self.plugin_tab.poiPluginField.repaint()
        self.poi_tab.poiList.clear()
        self.poi_tab.poiList.repaint()
        pluginName = plugin.get("Plugin Name")
        pluginDescription = plugin.get("Plugin Description")
        pluginStructure = plugin.get("Structure File Path")
        pluginDataset = plugin.get("Pre-Defined Dataset File Path")
        pluginOutput = plugin.get("Plugin Output")
        self.documentController.hidePluginStructure(False)

        pluginString = plugin.get("POI Strings")
        pluginFunction = plugin.get("POI Functions")

        for item in plugin.get("Strings"):  # Get Nested Document values
            self.listStrings.append(item.get("Name"))
            self.listStrings.append(item.get("Type"))
            self.listStrings.append(item.get("Output"))

        for item in plugin.get("Functions"):  # Get Nested Document values
            self.listFunctions.append(item.get("Name"))
            self.listFunctions.append(item.get("Type"))
            self.listFunctions.append(item.get("Output"))
        print("Clicked: Plugin")

        self.plugin_tab.poiPluginField.append(str(self.listStrings))  # Test
        self.plugin_tab.poiPluginField.append(str(self.listFunctions))  # Test

        self.plugin_tab.pluginNameField.setText(pluginName)
        self.plugin_tab.pluginDescriptionField.setText(pluginDescription)
        self.plugin_tab.pluginStructureField.setText(pluginStructure)
        self.plugin_tab.pluginPredefinedField.setText(pluginDataset)
        self.plugin_tab.outputFieldDropDown.addItem(pluginOutput)

        self.analysis_tab.poiTypeDropDownAnalysis.clear()
        self.analysis_tab.poiTypeDropDownAnalysis.addItem("Select")
        self.analysis_tab.poiTypeDropDownAnalysis.addItem(pluginString)
        self.analysis_tab.poiTypeDropDownAnalysis.addItem(pluginFunction)
        self.poi_tab.poiFilterDropDown.repaint()

        self.analysis_tab.pluginDropDownAnalysis.clear()
        self.analysis_tab.pluginDropDownAnalysis.repaint()
        self.analysis_tab.pluginDropDownAnalysis.addItem(pluginName)

        self.plugin_tab.outputFieldDropDown.clear()
        self.plugin_tab.outputFieldDropDown.repaint()
        self.plugin_tab.outputFieldDropDown.addItem(pluginOutput)

        self.poi_tab.poiPluginDropDown.clear()
        self.poi_tab.poiPluginDropDown.repaint()
        self.poi_tab.poiPluginDropDown.addItem(pluginName)

        self.poi_tab.poiFilterDropDown.clear()
        self.poi_tab.poiFilterDropDown.addItem("Select")
        self.poi_tab.poiFilterDropDown.addItem(pluginString)
        self.poi_tab.poiFilterDropDown.addItem(pluginFunction)
        self.poi_tab.poiFilterDropDown.repaint()

        self.plugin_tab.deletePluginButton.setEnabled(True)

        self.poiController.set_list(self.list)
        self.poiController.set_listStrings(self.listStrings)
        self.poiController.set_listFunctions(self.listFunctions)

    def parseXML(self, file_name):
        self.listFunctions.clear()
        self.listStrings.clear()
        self.list.clear()
        # Parse XML with ElementTree
        tree = ET.ElementTree(file=file_name)
        # print(tree.getroot())
        root = tree.getroot()
        # print("tag=%s, attrib=%s" % (root.tag, root.attrib))
        users = root.getchildren()
        for user in users:
            user_children = user.getchildren()
            for user_child in user_children:
                # print("%s=%s" % (user_child.tag, user_child.text))
                if user_child.tag == "network":
                    self.list.append(user_child.text)
                if user_child.tag == "nameFunctions" or user_child.tag == "typeFunctions" or user_child.tag == "outputFunctions":
                    self.listFunctions.append(user_child.text)
                if user_child.tag == "nameStrings" or user_child.tag == "typeStrings" or user_child.tag == "outputString":
                    self.listStrings.append(user_child.text)
        # print(list)
        print("Parse: ")
        print(self.listStrings)
        print(self.listFunctions)

        self.poiController.set_list(self.list)
        self.poiController.set_listStrings(self.listStrings)
        self.poiController.set_listFunctions(self.listFunctions)

    def filter_plugins(self):
        for item in self.plugin_tab.pluginManagementList.findItems("*", QtCore.Qt.MatchWildcard):
            item.setHidden(True)
        for item in self.plugin_tab.pluginManagementList.findItems(self.plugin_tab.pluginSearch.text(), QtCore.Qt.MatchStartsWith):
            item.setHidden(False)

