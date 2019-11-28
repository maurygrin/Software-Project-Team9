import os, sys, r2pipe, json, base64
import pymongo
from pymongo import MongoClient
from Script import Script
from Plugin import Plugin
from Project import Project
import xml.etree.cElementTree as ET
from PointOfInterest import POI
from BinaryFile import BinaryFile
from Metadata import Metadata
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

list=[]
class Ui_MainWindow(object):
    def __init__(self):
        self.windowNew = QtWidgets.QDialog()
        self.windowDeleteConfirmation = QtWidgets.QDialog()
        self.windowPlug = QtWidgets.QDialog()
        self.windowPOI = QtWidgets.QDialog()
        self.windowBinaryError = QtWidgets.QDialog()
        self.windowFileError = QtWidgets.QDialog()
        self.windowAnalysisResult = QtWidgets.QDialog()
        self.windowOutputField = QtWidgets.QDialog()
        self.windowComment = QtWidgets.QDialog()
        self.windowPluginError = QtWidgets.QDialog()
        self.text = None
        self.contents = None
        self.le = None
        self.path = ""
        self.arch = ""
        self.os = ""
        self.bintype = ""
        self.machine = ""
        self.classVar = ""
        self.bits = ""
        self.language = ""
        self.canary = ""
        self.endian = ""
        self.crypto = ""
        self.nx = ""
        self.pic = ""
        self.relocs = ""
        self.stripped = ""
        self.extension = ""
        self.projectTabName = "Project"
        self.analysisTabName = "Analysis"
        self.s = ""
        self.vaddr = ""
        self.value = ""
        self.section = ""

        cluster = MongoClient("mongodb://localhost:27017")
        db = cluster.test
        self.collection = db["beat"]

    def projectWindow(self):
        self.setupUiCreateProject(self.windowNew)
        self.windowNew.show()

    def pluginWindow(self):
        self.setupUiCreatePlugin(self.windowPlug)
        self.windowPlug.show()

    def deleteConfirmation(self):
        self.setupUiDeleteProjectConfirmation(self.windowDeleteConfirmation)
        self.windowDeleteConfirmation.show()

    def binaryErrorWindow(self):
        self.setupUiBinaryError(self.windowBinaryError)
        self.windowBinaryError.show()

    def removeBreakpoint(self, item):
       # item.checkState() == 2
        print("changed")
        #item.


    def createProject(self, name, binary, description):
        if not name or not binary or not description:
            print("Failed")
        else:
            self.project = Project(name, binary, description)

            self.projectNameField.setText(self.project.name)
            self.binaryFilePathField.setText(self.project.binary)
            self.projectDescriptionField.setText(self.project.description)

            self.r2 = r2pipe.open(self.path)

            self.binaryInfo = self.r2.cmdj('ij')

            self.metadata = Metadata(self.binaryInfo.get("bin").get("arch"), self.binaryInfo.get("bin").get("os"),
                                     self.binaryInfo.get("bin").get("bintype"),
                                     self.binaryInfo.get("bin").get("machine"), self.binaryInfo.get("bin").get("class"),
                                     self.binaryInfo.get("bin").get("bits"),
                                     self.binaryInfo.get("bin").get("lang"), self.binaryInfo.get("bin").get("canary"),
                                     self.binaryInfo.get("bin").get("endian"),
                                     self.binaryInfo.get("bin").get("crypto"), self.binaryInfo.get("bin").get("nx"),
                                     self.binaryInfo.get("bin").get("pic"),
                                     self.binaryInfo.get("bin").get("relocs"),
                                     self.binaryInfo.get("bin").get("striped"), self.binaryInfo.get("core").get("type"))

            self.binary = BinaryFile(binary, self.metadata)

            self.arch = self.binary.metadata.arch
            self.os = self.binary.metadata.os
            self.bintype = self.binary.metadata.binaryType
            self.machine = self.binary.metadata.machine
            self.classVar = self.binary.metadata.classVariable
            self.bits = self.binary.metadata.bits
            self.language = self.binary.metadata.language
            self.canary = self.binary.metadata.canary
            self.endian = self.binary.metadata.endian
            self.crypto = self.binary.metadata.crypto
            self.nx = self.binary.metadata.nx
            self.pic = self.binary.metadata.pic
            self.relocs = self.binary.metadata.relocs
            self.stripped = self.binary.metadata.stripped
            self.extension = self.binary.metadata.type

            self.binaryFilePathEdit.setText(self.path)
            self.fileProperties.append("arch\t\t\t" + self.binary.metadata.arch + "\n")
            self.fileProperties.append("os\t\t\t" + self.binary.metadata.os + "\n")
            self.fileProperties.append("bintype\t\t\t" + self.binary.metadata.binaryType + "\n")
            self.fileProperties.append("machine\t\t\t" + self.binary.metadata.machine + "\n")
            self.fileProperties.append("class\t\t\t" + self.binary.metadata.classVariable + "\n")
            self.fileProperties.append("bits\t\t\t" + str(self.binary.metadata.bits) + "\n")
            self.fileProperties.append("language\t\t\t" + self.binary.metadata.language + "\n")
            self.fileProperties.append("canary\t\t\t" + str(self.binary.metadata.canary) + "\n")
            self.fileProperties.append("endian\t\t\t" + self.binary.metadata.endian + "\n")
            self.fileProperties.append("crypto\t\t\t" + str(self.binary.metadata.crypto) + "\n")
            self.fileProperties.append("nx\t\t\t" + str(self.binary.metadata.nx) + "\n")
            self.fileProperties.append("pic\t\t\t" + str(self.binary.metadata.pic) + "\n")
            self.fileProperties.append("relocs\t\t\t" + str(self.binary.metadata.relocs) + "\n")
            self.fileProperties.append("stripped\t\t\t" + str(self.binary.metadata.stripped) + "\n")
            self.fileProperties.append("extension\t\t\t" + self.binary.metadata.type + "\n")

            self.binaryFilePathField.setText(self.path)

            self.saveProject()

    def runStaticAnalysis(self):
        if (self.pluginDropDownAnalysis.currentText() == "Select"):
            self.setupPluginError(self.windowPluginError)
            self.windowPluginError.show()
        else:
            self.runDynamicButton.setEnabled(True)

            self.static = 1

            self.terminalField.append("Static Analysis Performed!")
            self.terminalField.append("")

            self.s = self.r2.cmdj("izj")

            poiSelected = self.poiTypeDropDownAnalysis.currentText()

            if (poiSelected == "Strings"):
                self.terminalField.append("Command: iz")
                self.display = "strings"
                self.detailedPoiAnalysisField.setText("")
                self.poiAnalysisList.clear()
                self.detailedPoiAnalysisField.append("\t" + "\n")
                self.detailedPoiAnalysisField.append("\t" + "Virtual Memory Address: ")
                self.detailedPoiAnalysisField.append("\t" + "\n")
                self.detailedPoiAnalysisField.append("\t" + "Value: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Section: ")
                font = self.detailedPoiAnalysisField.font()
                font.setPointSize(20)
                self.detailedPoiAnalysisField.setFont(font)
                self.detailedPoiAnalysisField.repaint()
                #                self.s = self.analysis.display(self.r2, self.display)
                for item in self.s:
                    item = QtWidgets.QListWidgetItem(base64.b64decode(item["string"]).decode())
                    item.setCheckState(QtCore.Qt.Checked)
                    self.poiAnalysisList.addItem(item)

    def displayPOI(self):
        if (self.static == 1):

            poiSelected = self.poiTypeDropDownAnalysis.currentText()

            if (poiSelected == "Strings"):
                self.display = "strings"
                self.terminalField.append("Command: iz")
                self.detailedPoiAnalysisField.setText("")
                self.poiAnalysisList.clear()
                self.detailedPoiAnalysisField.append("\t" + "\n")
                self.detailedPoiAnalysisField.append("\t" + "Virtual Memory Address: ")
                self.detailedPoiAnalysisField.append("\t" + "\n")
                self.detailedPoiAnalysisField.append("\t" + "Value: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Section: ")
                font = self.detailedPoiAnalysisField.font()
                font.setPointSize(20)
                self.detailedPoiAnalysisField.setFont(font)
                self.detailedPoiAnalysisField.repaint()
                for item in self.s:
                    self.poiAnalysisList.addItem(base64.b64decode(item["string"]).decode())

    def parseXML(file_name):
        # Parse XML with ElementTree
        tree = ET.ElementTree(file=file_name)
        # print(tree.getroot())
        root = tree.getroot()
        # print("tag=%s, attrib=%s" % (root.tag, root.attrib))
        users = root.getchildren()
        for user in users:
            user_children = user.getchildren()
            for user_child in user_children:
                print("%s=%s" % (user_child.tag, user_child.text))
                list.append(user_child.text)
        print(list)

    def createPlugin(self, name, description, structure, data_set):
        if not name or not description or not structure or not data_set:
            print("Failed")
        else:
            self.plugin = Plugin(name, description, structure, data_set)
            self.pluginNameField.setText(self.plugin.name)
            self.pluginDescriptionField.setText(self.plugin.description)
            self.pluginStructureField.setText(self.plugin.structure)
            self.pluginPredefinedField.setText(self.plugin.data_set)
            self.pluginDropDownAnalysis.addItem(self.plugin.name)

            self.poiTypeDropDownAnalysis.clear()
            self.poiTypeDropDownAnalysis.repaint()
            self.poiTypeDropDownAnalysis.addItem("Select")
            self.poiTypeDropDownAnalysis.addItem(list[5])
            self.poiTypeDropDownAnalysis.addItem(list[6])

            self.pluginDropDownAnalysis.clear()
            self.pluginDropDownAnalysis.repaint()
            self.pluginDropDownAnalysis.addItem("Select")
            self.pluginDropDownAnalysis.addItem(list[0])

            self.poiPluginDropDown.clear()
            self.poiPluginDropDown.repaint()
            self.poiPluginDropDown.addItem("Select")
            self.poiPluginDropDown.addItem(list[0])

            self.poiFilterDropDown.clear()
            self.poiFilterDropDown.repaint()
            self.poiFilterDropDown.addItem("Select")
            self.poiFilterDropDown.addItem(list[5])
            self.poiFilterDropDown.addItem(list[6])

            self.savePlugin()

    def saveProject(self):
        project = {"Project Name": self.project.name,
                   "Project Description": self.project.description,
                   "Binary File Path": self.path,
                   "arch": self.arch,
                   "os": self.os,
                   "bintype": self.bintype,
                   "machine": self.machine,
                   "class": self.classVar,
                   "bits": self.bits,
                   "language": self.language,
                   "canary": self.canary,
                   "endian": self.endian,
                   "crypto": self.crypto,
                   "nx": self.nx,
                   "pic": self.pic,
                   "relocs": self.relocs,
                   "stripped": self.stripped,
                   "extension": self.extension}

        self.collection.insert([project])

        it = QtWidgets.QListWidgetItem(self.project.name)

        self.projectList.addItem(it)

        it.setSelected(True)

        self.projectDescriptionField.setEnabled(True)

        self.projectDeleteButton.setEnabled(True)

        self.projectTabName = "Project - " + self.project.name
        self.analysisTabName = "Analysis - " + self.project.name

        self.retranslateUi(MainWindow)

    def savePlugin(self):
        pluginDB = {"Plugin Name": self.plugin.name,
                    "Plugin Description": self.plugin.description,
                    "Structure File Path": self.plugin.structure,
                    "Pre-Defined Dataset File Path": self.plugin.data_set,
                    "POI Strings": list[5],
                    "POI Functions": list[6]}

        self.collection.insert([pluginDB])

        it = QtWidgets.QListWidgetItem(self.plugin.name)

        self.pluginManagementList.addItem(it)

        it.setSelected(True)

        self.retranslateUi(MainWindow)

    def deleteProject(self):
        self.projectDeleteButton.setEnabled(False)
        p = self.collection.find_one({"Project Name": self.projectList.currentItem().text()})
        self.collection.delete_one(p)
        self.projectList.takeItem(self.projectList.currentRow())
        self.projectNameField.clear()
        self.projectDescriptionField.clear()
        self.binaryFilePathField.clear()
        self.fileProperties.clear()
        self.projectNameField.repaint()
        self.projectDescriptionField.repaint()
        self.binaryFilePathField.repaint()
        self.fileProperties.repaint()
        self.r2 = ""
        self.projectList.clearSelection()
        self.projectTabName = "Project"
        self.analysisTabName = "Analysis"
        self.retranslateUi(MainWindow)

    def deletePlugin(self):
        p = self.collection.find_one({"Plugin Name": self.pluginManagementList.currentItem().text()})
        self.collection.delete_one(p)
        self.pluginManagementList.takeItem(self.pluginManagementList.currentRow())
        self.pluginNameField.clear()
        self.pluginDescriptionField.clear()
        self.pluginStructureField.clear()
        self.pluginPredefinedField.clear()
        self.pluginNameField.repaint()
        self.pluginDescriptionField.repaint()
        self.pluginStructureField.repaint()
        self.pluginPredefinedField.repaint()

    def getBinaryFilePath(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.binaryFilePathField, "Browse Binary File", "",
                                                            "Binary Files (*.exe *.out *.class *.docx)",
                                                            options=options)
        if fileName:
            self.path = str(fileName)

            self.r2 = r2pipe.open(self.path)

            self.binaryInfo = self.r2.cmdj('ij')

            try:
                if (self.binaryInfo.get("bin").get("arch") != "x86") or (
                        self.binaryInfo.get("core").get("type") != "Executable file" and self.binaryInfo.get(
                    "core").get("type") != "EXEC (Executable file)"):
                    self.binaryErrorWindow()
                    self.r2 = ""
                    self.fileProperties.setText("")
                    self.path = ""
                    self.binaryFilePathEdit.setText("")
                    self.r2 = ""
                    self.binaryInfo = ""

                else:
                    self.binaryFilePathEdit.setText(fileName)

            except Exception as e:
                self.binaryErrorWindow()
                self.r2 = ""
                self.fileProperties.setText("")
                self.path = ""
                self.binaryFilePathEdit.setText("")
                self.r2 = ""
                self.binaryInfo = ""

    def BrowseStruct(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.structureFieldWindow, "Browse XML Schema", "",
                                                            "XML Schemas Files (*.xsd)", options=options)
        if fileName:
            self.structureFieldWindow.setText(fileName)

    def BrowseDataSet(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.datasetFieldWindow, "Browse XML File", "",
                                                            "XML Files (*.xml)", options=options)
        if fileName:
            self.datasetFieldWindow.setText(fileName)
            Ui_MainWindow.parseXML(fileName)
            self.pluginNameEdit.setText(list[0])
            self.pluginDescriptionEdit.setText(list[1])

    def projectClicked(self):
        p = self.collection.find_one({"Project Name": self.projectList.currentItem().text()})

        self.projectNameField.setText(p.get("Project Name"))

        self.projectDescriptionField.setText(p.get("Project Description"))

        self.binaryFilePathField.setText(p.get("Binary File Path"))

        self.fileProperties.append("arch\t\t\t" + p.get("arch") + "\n")
        self.fileProperties.append("os\t\t\t" + p.get("os") + "\n")
        self.fileProperties.append("bintype\t\t\t" + p.get("bintype") + "\n")
        self.fileProperties.append("machine\t\t\t" + p.get("machine") + "\n")
        self.fileProperties.append("class\t\t\t" + p.get("class") + "\n")
        self.fileProperties.append("bits\t\t\t" + str(p.get("bits")) + "\n")
        self.fileProperties.append("language\t\t\t" + p.get("language") + "\n")
        self.fileProperties.append("canary\t\t\t" + str(p.get("canary")) + "\n")
        self.fileProperties.append("endian\t\t\t" + p.get("endian") + "\n")
        self.fileProperties.append("crypto\t\t\t" + str(p.get("crypto")) + "\n")
        self.fileProperties.append("nx\t\t\t" + str(p.get("nx")) + "\n")
        self.fileProperties.append("pic\t\t\t" + str(p.get("pic")) + "\n")
        self.fileProperties.append("relocs\t\t\t" + str(p.get("relocs")) + "\n")
        self.fileProperties.append("stripped\t\t\t" + str(p.get("stripped")) + "\n")
        self.fileProperties.append("extension\t\t\t" + p.get("extension") + "\n")

        self.r2 = r2pipe.open(p.get("Binary File Path"))

        self.detailedPoiAnalysisField.clear()

        self.projectDescriptionField.setEnabled(True)

        self.projectDeleteButton.setEnabled(True)

        self.projectTabName = "Project - " + self.projectList.currentItem().text()
        self.analysisTabName = "Analysis - " + self.projectList.currentItem().text()
        self.retranslateUi(MainWindow)

    def analysisClicked(self):
        selected = self.poiAnalysisList.currentItem().text()
        if self.display is "strings":
            for item in self.s:
                current = base64.b64decode(item["string"]).decode()
                if current == selected:
                    self.vaddr = hex(item["vaddr"])
                    self.vaddr = str(self.vaddr)
                    self.value = current
                    self.section = item["section"]
                    break
            self.detailedPoiAnalysisField.setText("")
            self.detailedPoiAnalysisField.append("\t" + "\n")
            self.detailedPoiAnalysisField.append("\t" + "Virtual Memory Address: " + self.vaddr)
            self.detailedPoiAnalysisField.append("\t" + "\n")
            self.detailedPoiAnalysisField.append("\t" + "Value: " + self.value)
            self.detailedPoiAnalysisField.append("\n")
            self.detailedPoiAnalysisField.append("\t" + "Section: " + self.section)
            font = self.detailedPoiAnalysisField.font()
            font.setPointSize(20)
            self.detailedPoiAnalysisField.setFont(font)
            self.detailedPoiAnalysisField.repaint()

    def runClicked(self):
        print("Analysis Run List clicked")

    def pluginClicked(self):
        plugin = self.collection.find_one({"Plugin Name": self.pluginManagementList.currentItem().text()})

        pluginName = plugin.get("Plugin Name")

        pluginDescription = plugin.get("Plugin Description")

        pluginStructure = plugin.get("Structure File Path")

        pluginDataset = plugin.get("Pre-Defined Dataset File Path")

        pluginString = plugin.get("POI Strings")

        pluginFunction = plugin.get("POI Functions")


        self.pluginNameField.setText(pluginName)
        self.pluginDescriptionField.setText(pluginDescription)
        self.pluginStructureField.setText(pluginStructure)
        self.pluginPredefinedField.setText(pluginDataset)

        self.poiTypeDropDownAnalysis.clear()
        self.poiTypeDropDownAnalysis.repaint()
        self.poiTypeDropDownAnalysis.addItem("Select")
        self.poiTypeDropDownAnalysis.addItem(pluginString)
        self.poiTypeDropDownAnalysis.addItem(pluginFunction)

        self.pluginDropDownAnalysis.clear()
        self.pluginDropDownAnalysis.repaint()
        self.pluginDropDownAnalysis.addItem("Select")
        self.pluginDropDownAnalysis.addItem(pluginName)

        self.poiPluginDropDown.clear()
        self.poiPluginDropDown.repaint()
        self.poiPluginDropDown.addItem("Select")
        self.poiPluginDropDown.addItem(pluginName)

        self.poiFilterDropDown.clear()
        self.poiFilterDropDown.repaint()
        self.poiFilterDropDown.addItem("Select")
        self.poiFilterDropDown.addItem(pluginString)
        self.poiFilterDropDown.addItem(pluginFunction)

        self.deletePluginButton.setEnabled(True)

    def poiClicked(self):
        print("POI List clicked")

    def documentationClicked(self):
        print("Documentation List clicked")

    def filter_projects(self):  ##filtering list of project
        for item in self.projectList.findItems("*", QtCore.Qt.MatchWildcard):
            item.setHidden(True)
        for item in self.projectList.findItems(self.projectSearch.text(), QtCore.Qt.MatchStartsWith):
            item.setHidden(False)

    def filter_plugins(self):
        for item in self.pluginManagementList.findItems("*", QtCore.Qt.MatchWildcard):
            item.setHidden(True)
        for item in self.pluginManagementList.findItems(self.pluginSearch.text(), QtCore.Qt.MatchStartsWith):
            item.setHidden(False)

    def filter_POI(self):
        for item in self.poiList.findItems("*", QtCore.Qt.MatchWildcard):
            item.setHidden(True)
        for item in self.poiList.findItems(self.poiSearch.text(), QtCore.Qt.MatchStartsWith):
            item.setHidden(False)

    def filter_doc(self):
        for item in self.documentList.findItems("*", QtCore.Qt.MatchWildcard):
            item.setHidden(True)
        for item in self.documentList.findItems(self.documentSearch.text(), QtCore.Qt.MatchStartsWith):
            item.setHidden(False)


    def setupUi(self, MainWindow):

        self.static = 0

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1318, 755)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.UI = QtWidgets.QTabWidget(self.centralwidget)
        self.UI.setGeometry(QtCore.QRect(0, 0, 1321, 721))
        self.UI.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.UI.setElideMode(QtCore.Qt.ElideLeft)
        self.UI.setDocumentMode(True)
        self.UI.setTabsClosable(False)
        self.UI.setMovable(True)
        self.UI.setTabBarAutoHide(False)
        self.UI.setObjectName("UI")
        self.projectTab = QtWidgets.QWidget()
        self.projectTab.setObjectName("projectTab")
        self.projectViewGroup = QtWidgets.QGroupBox(self.projectTab)
        self.projectViewGroup.setGeometry(QtCore.QRect(20, 10, 261, 681))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.projectViewGroup.setFont(font)
        self.projectViewGroup.setObjectName("projectViewGroup")
        self.projectNewButton = QtWidgets.QPushButton(self.projectViewGroup)
        self.projectNewButton.setGeometry(QtCore.QRect(10, 640, 113, 32))
        self.projectNewButton.setObjectName("projectNewButton")
        self.projectList = QtWidgets.QListWidget(self.projectViewGroup)
        self.projectList.setGeometry(QtCore.QRect(10, 80, 231, 551))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.projectList.setFont(font)
        self.projectList.setObjectName("projectList")
        self.projectSearch = QtWidgets.QLineEdit(self.projectViewGroup)
        self.projectSearch.setGeometry(QtCore.QRect(10, 30, 231, 31))
        self.projectSearch.setObjectName("projectSearch")
        self.projectSearch.textChanged[str].connect(self.filter_projects)
        self.glass = QtWidgets.QLabel(self.projectViewGroup)
        self.glass.setGeometry(QtCore.QRect(190, 30, 51, 31))
        self.glass.setText("")
        self.glass.setPixmap(QtGui.QPixmap("../../cliparts-for-powerpoint-transparent-magnifying-glass-md.png"))
        self.glass.setScaledContents(True)
        self.glass.setObjectName("glass")
        self.projectSearchButton = QtWidgets.QPushButton(self.projectViewGroup)
        self.projectSearchButton.setGeometry(QtCore.QRect(180, 30, 61, 31))
        self.projectSearchButton.setObjectName("projectSearchButton")
        self.projectDeleteButton = QtWidgets.QPushButton(self.projectViewGroup)
        self.projectDeleteButton.setGeometry(QtCore.QRect(130, 640, 113, 32))
        self.projectDeleteButton.setObjectName("projectDeleteButton")
        self.detailedProjectView = QtWidgets.QGroupBox(self.projectTab)
        self.detailedProjectView.setGeometry(QtCore.QRect(310, 10, 991, 681))
        self.detailedProjectView.setTitle("")
        self.detailedProjectView.setObjectName("detailedProjectView")
        self.saveProjectButton = QtWidgets.QPushButton(self.detailedProjectView)
        self.saveProjectButton.setGeometry(QtCore.QRect(820, 640, 113, 32))
        self.saveProjectButton.setObjectName("saveProjectButton")
        self.projectNameLabel = QtWidgets.QLabel(self.detailedProjectView)
        self.projectNameLabel.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.projectNameLabel.setObjectName("projectNameLabel")
        self.projectDescriptionLabel = QtWidgets.QLabel(self.detailedProjectView)
        self.projectDescriptionLabel.setGeometry(QtCore.QRect(10, 60, 141, 16))
        self.projectDescriptionLabel.setObjectName("projectDescriptionLabel")
        self.binaryFilePathLabel = QtWidgets.QLabel(self.detailedProjectView)
        self.binaryFilePathLabel.setGeometry(QtCore.QRect(10, 180, 131, 16))
        self.binaryFilePathLabel.setObjectName("binaryFilePathLabel")
        self.binaryFilePropertiesLabel = QtWidgets.QLabel(self.detailedProjectView)
        self.binaryFilePropertiesLabel.setGeometry(QtCore.QRect(10, 230, 151, 16))
        self.binaryFilePropertiesLabel.setObjectName("binaryFilePropertiesLabel")
        self.projectNameField = QtWidgets.QLineEdit(self.detailedProjectView)
        self.projectNameField.setGeometry(QtCore.QRect(150, 30, 781, 21))
        self.projectNameField.setObjectName("projectNameField")
        self.projectDescriptionField = QtWidgets.QLineEdit(self.detailedProjectView)
        self.projectDescriptionField.setGeometry(QtCore.QRect(150, 60, 781, 111))
        self.projectDescriptionField.setObjectName("projectDescriptionField")
        self.binaryFilePathField = QtWidgets.QLineEdit(self.detailedProjectView)
        self.binaryFilePathField.setGeometry(QtCore.QRect(150, 180, 781, 21))
        self.binaryFilePathField.setObjectName("binaryFilePathField")
        self.binaryFilePropertiesField = QtWidgets.QScrollArea(self.detailedProjectView)
        self.binaryFilePropertiesField.setGeometry(QtCore.QRect(150, 230, 781, 401))
        self.binaryFilePropertiesField.setWidgetResizable(True)
        self.binaryFilePropertiesField.setObjectName("binaryFilePropertiesField")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.BEAT = QtWidgets.QColumnView(self.scrollAreaWidgetContents)
        self.BEAT.setGeometry(QtCore.QRect(0, 0, 671, 351))
        self.BEAT.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.BEAT.setTabKeyNavigation(True)
        self.BEAT.setDragEnabled(False)
        self.BEAT.setAlternatingRowColors(True)
        self.BEAT.setObjectName("BEAT")
        self.fileProperties = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.fileProperties.setGeometry(QtCore.QRect(0, 0, 781, 401))
        self.fileProperties.setObjectName("fileProperties")
        self.filePropertiesLine = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.filePropertiesLine.setGeometry(QtCore.QRect(220, 0, 16, 581))
        self.filePropertiesLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.filePropertiesLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.filePropertiesLine.setObjectName("filePropertiesLine")
        self.binaryFilePropertiesField.setWidget(self.scrollAreaWidgetContents)
        self.detailedProjectViewLabel = QtWidgets.QLabel(self.detailedProjectView)
        self.detailedProjectViewLabel.setGeometry(QtCore.QRect(10, 0, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.detailedProjectViewLabel.setFont(font)
        self.detailedProjectViewLabel.setObjectName("detailedProjectViewLabel")
        self.UI.addTab(self.projectTab, "")
        self.analysisTab = QtWidgets.QWidget()
        self.analysisTab.setObjectName("analysisTab")
        self.analysisSection = QtWidgets.QGroupBox(self.analysisTab)
        self.analysisSection.setGeometry(QtCore.QRect(310, 20, 991, 671))
        self.analysisSection.setTitle("")
        self.analysisSection.setObjectName("analysisSection")
        self.detailedAnalysisViewLabel = QtWidgets.QLabel(self.analysisSection)
        self.detailedAnalysisViewLabel.setGeometry(QtCore.QRect(40, 80, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.detailedAnalysisViewLabel.setFont(font)
        self.detailedAnalysisViewLabel.setObjectName("detailedAnalysisViewLabel")
        self.terminalLabel = QtWidgets.QLabel(self.analysisSection)
        self.terminalLabel.setGeometry(QtCore.QRect(40, 480, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.terminalLabel.setFont(font)
        self.terminalLabel.setObjectName("terminalLabel")
        self.outputFieldViewButton = QtWidgets.QPushButton(self.analysisSection)
        self.outputFieldViewButton.setGeometry(QtCore.QRect(780, 420, 151, 30))
        self.outputFieldViewButton.setObjectName("outputFieldViewButton")
        self.terminalField = QtWidgets.QTextEdit(self.analysisSection)
        self.terminalField.setGeometry(QtCore.QRect(30, 510, 921, 121))
        self.terminalField.setObjectName("terminalField")
        self.frame = QtWidgets.QFrame(self.analysisSection)
        self.frame.setGeometry(QtCore.QRect(30, 110, 921, 351))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.runList = QtWidgets.QListWidget(self.frame)
        self.runList.setGeometry(QtCore.QRect(20, 20, 161, 281))
        self.runList.setObjectName("runList")
        self.detailedPoiAnalysisField = QtWidgets.QTextBrowser(self.frame)
        self.detailedPoiAnalysisField.setGeometry(QtCore.QRect(200, 20, 701, 281))
        self.detailedPoiAnalysisField.setObjectName("detailedPoiAnalysisField")
        self.deleteAnalysisResultButton = QtWidgets.QPushButton(self.frame)
        self.deleteAnalysisResultButton.setGeometry(QtCore.QRect(20, 310, 171, 30))
        self.deleteAnalysisResultButton.setObjectName("deleteAnalysisResultButton")
        self.pluginLabel = QtWidgets.QLabel(self.analysisTab)
        self.pluginLabel.setGeometry(QtCore.QRect(360, 30, 61, 31))
        self.pluginLabel.setObjectName("pluginLabel")
        self.staticAnalysisLabel = QtWidgets.QLabel(self.analysisTab)
        self.staticAnalysisLabel.setGeometry(QtCore.QRect(880, 40, 101, 21))
        self.staticAnalysisLabel.setObjectName("staticAnalysisLabel")
        self.poiTypeLabel = QtWidgets.QLabel(self.analysisTab)
        self.poiTypeLabel.setGeometry(QtCore.QRect(360, 70, 61, 21))
        self.poiTypeLabel.setObjectName("poiTypeLabel")
        self.dynamicAnalysisLabel = QtWidgets.QLabel(self.analysisTab)
        self.dynamicAnalysisLabel.setGeometry(QtCore.QRect(880, 80, 121, 21))
        self.dynamicAnalysisLabel.setObjectName("dynamicAnalysisLabel")
        self.pluginDropDownAnalysis = QtWidgets.QComboBox(self.analysisTab)
        self.pluginDropDownAnalysis.setGeometry(QtCore.QRect(430, 30, 131, 32))
        self.pluginDropDownAnalysis.setObjectName("pluginDropDownAnalysis")
        self.pluginDropDownAnalysis.addItem("")
        self.runStaticButton = QtWidgets.QPushButton(self.analysisTab)
        self.runStaticButton.setGeometry(QtCore.QRect(1010, 40, 111, 32))
        self.runStaticButton.setObjectName("runStaticButton")
        self.poiTypeDropDownAnalysis = QtWidgets.QComboBox(self.analysisTab)
        self.poiTypeDropDownAnalysis.setGeometry(QtCore.QRect(430, 70, 131, 32))
        self.poiTypeDropDownAnalysis.setEditable(False)
        self.poiTypeDropDownAnalysis.setObjectName("poiTypeDropDownAnalysis")
        self.poiTypeDropDownAnalysis.addItem("")
        self.runDynamicButton = QtWidgets.QPushButton(self.analysisTab)
        self.runDynamicButton.setGeometry(QtCore.QRect(1010, 70, 113, 32))
        self.runDynamicButton.setObjectName("runDynamicButton")
        self.stopDynamicButton = QtWidgets.QPushButton(self.analysisTab)
        self.stopDynamicButton.setGeometry(QtCore.QRect(1130, 70, 113, 32))
        self.stopDynamicButton.setObjectName("stopDynamicButton")
        self.analysisView = QtWidgets.QGroupBox(self.analysisTab)
        self.analysisView.setGeometry(QtCore.QRect(20, 10, 261, 681))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.analysisView.setFont(font)
        self.analysisView.setObjectName("analysisView")
        self.poiAnalysisList = QtWidgets.QListWidget(self.analysisView)
        self.poiAnalysisList.setGeometry(QtCore.QRect(10, 30, 231, 601))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.poiAnalysisList.setFont(font)
        self.poiAnalysisList.setObjectName("poiAnalysisList")
        self.commentViewButton = QtWidgets.QPushButton(self.analysisView)
        self.commentViewButton.setGeometry(QtCore.QRect(100, 640, 141, 30))
        self.commentViewButton.setObjectName("commentViewButton")
        self.UI.addTab(self.analysisTab, "")
        self.pluginManagementTab = QtWidgets.QWidget()
        self.pluginManagementTab.setObjectName("pluginManagementTab")
        self.pluginView = QtWidgets.QGroupBox(self.pluginManagementTab)
        self.pluginView.setGeometry(QtCore.QRect(20, 10, 261, 681))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pluginView.setFont(font)
        self.pluginView.setObjectName("pluginView")
        self.newPluginButton = QtWidgets.QPushButton(self.pluginView)
        self.newPluginButton.setGeometry(QtCore.QRect(10, 640, 113, 32))
        self.newPluginButton.setObjectName("newPluginButton")
        self.pluginSearch = QtWidgets.QLineEdit(self.pluginView)
        self.pluginSearch.setGeometry(QtCore.QRect(10, 30, 231, 31))
        self.pluginSearch.setObjectName("pluginSearch")
        self.pluginSearch.textChanged[str].connect(self.filter_plugins)
        self.pluginManagementList = QtWidgets.QListWidget(self.pluginView)
        self.pluginManagementList.setGeometry(QtCore.QRect(10, 80, 231, 551))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pluginManagementList.setFont(font)
        self.pluginManagementList.setObjectName("pluginManagementList")
        self.glass_2 = QtWidgets.QLabel(self.pluginView)
        self.glass_2.setGeometry(QtCore.QRect(190, 30, 51, 31))
        self.glass_2.setText("")
        self.glass_2.setPixmap(QtGui.QPixmap("../../cliparts-for-powerpoint-transparent-magnifying-glass-md.png"))
        self.glass_2.setScaledContents(True)
        self.glass_2.setObjectName("glass_2")
        self.searchPluginButton = QtWidgets.QPushButton(self.pluginView)
        self.searchPluginButton.setGeometry(QtCore.QRect(180, 30, 61, 31))
        self.searchPluginButton.setObjectName("searchPluginButton")
        self.deletePluginButton = QtWidgets.QPushButton(self.pluginView)
        self.deletePluginButton.setGeometry(QtCore.QRect(130, 640, 113, 32))
        self.deletePluginButton.setObjectName("deletePluginButton")
        self.detailedPluginView = QtWidgets.QGroupBox(self.pluginManagementTab)
        self.detailedPluginView.setGeometry(QtCore.QRect(310, 10, 991, 681))
        self.detailedPluginView.setTitle("")
        self.detailedPluginView.setObjectName("detailedPluginView")
        self.pluginStructureLabel = QtWidgets.QLabel(self.detailedPluginView)
        self.pluginStructureLabel.setGeometry(QtCore.QRect(10, 30, 131, 21))
        self.pluginStructureLabel.setObjectName("pluginStructureLabel")
        self.pluginPredefinedLabel = QtWidgets.QLabel(self.detailedPluginView)
        self.pluginPredefinedLabel.setGeometry(QtCore.QRect(10, 60, 191, 16))
        self.pluginPredefinedLabel.setObjectName("pluginPredefinedLabel")
        self.pluginNameLabel = QtWidgets.QLabel(self.detailedPluginView)
        self.pluginNameLabel.setGeometry(QtCore.QRect(10, 90, 101, 16))
        self.pluginNameLabel.setObjectName("pluginNameLabel")
        self.pluginDescriptionLabel = QtWidgets.QLabel(self.detailedPluginView)
        self.pluginDescriptionLabel.setGeometry(QtCore.QRect(10, 120, 141, 16))
        self.pluginDescriptionLabel.setObjectName("pluginDescriptionLabel")
        self.defaultOutputFieldLabel = QtWidgets.QLabel(self.detailedPluginView)
        self.defaultOutputFieldLabel.setGeometry(QtCore.QRect(10, 220, 161, 16))
        self.defaultOutputFieldLabel.setObjectName("defaultOutputFieldLabel")
        self.poiLabel = QtWidgets.QLabel(self.detailedPluginView)
        self.poiLabel.setGeometry(QtCore.QRect(10, 250, 111, 16))
        self.poiLabel.setObjectName("poiLabel")
        self.outputFieldDropDown = QtWidgets.QComboBox(self.detailedPluginView)
        self.outputFieldDropDown.setGeometry(QtCore.QRect(200, 210, 121, 32))
        self.outputFieldDropDown.setObjectName("outputFieldDropDown")
        self.outputFieldDropDown.addItem("")
        self.savePluginButton = QtWidgets.QPushButton(self.detailedPluginView)
        self.savePluginButton.setGeometry(QtCore.QRect(820, 640, 113, 32))
        self.savePluginButton.setObjectName("savePluginButton")
        self.detailedPluginViewLabel = QtWidgets.QLabel(self.detailedPluginView)
        self.detailedPluginViewLabel.setGeometry(QtCore.QRect(10, 0, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.detailedPluginViewLabel.setFont(font)
        self.detailedPluginViewLabel.setObjectName("detailedPluginViewLabel")
        self.XMLEditorButton = QtWidgets.QPushButton(self.detailedPluginView)
        self.XMLEditorButton.setGeometry(QtCore.QRect(20, 280, 113, 32))
        self.XMLEditorButton.setObjectName("XMLEditorButton")
        self.pluginStructureField = QtWidgets.QLineEdit(self.detailedPluginView)
        self.pluginStructureField.setGeometry(QtCore.QRect(200, 30, 731, 21))
        self.pluginStructureField.setObjectName("pluginStructureField")
        self.pluginPredefinedField = QtWidgets.QLineEdit(self.detailedPluginView)
        self.pluginPredefinedField.setGeometry(QtCore.QRect(200, 60, 731, 21))
        self.pluginPredefinedField.setObjectName("pluginPredefinedField")
        self.pluginNameField = QtWidgets.QLineEdit(self.detailedPluginView)
        self.pluginNameField.setGeometry(QtCore.QRect(200, 90, 731, 21))
        self.pluginNameField.setObjectName("pluginNameField")
        self.pluginDescriptionField = QtWidgets.QTextEdit(self.detailedPluginView)
        self.pluginDescriptionField.setGeometry(QtCore.QRect(200, 120, 731, 74))
        self.pluginDescriptionField.setObjectName("pluginDescriptionField")
        self.poiPluginField = QtWidgets.QTextEdit(self.detailedPluginView)
        self.poiPluginField.setGeometry(QtCore.QRect(200, 250, 731, 381))
        self.poiPluginField.setObjectName("poiPluginField")
        self.UI.addTab(self.pluginManagementTab, "")
        self.poiTab = QtWidgets.QWidget()
        self.poiTab.setObjectName("poiTab")
        self.poiView = QtWidgets.QGroupBox(self.poiTab)
        self.poiView.setGeometry(QtCore.QRect(20, 10, 261, 681))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.poiView.setFont(font)
        self.poiView.setObjectName("poiView")
        self.newPOIButton = QtWidgets.QPushButton(self.poiView)
        self.newPOIButton.setGeometry(QtCore.QRect(10, 640, 113, 32))
        self.newPOIButton.setObjectName("newPOIButton")
        self.poiSearch = QtWidgets.QLineEdit(self.poiView)
        self.poiSearch.setGeometry(QtCore.QRect(10, 30, 231, 31))
        self.poiSearch.setObjectName("poiSearch")
        self.poiSearch.textChanged[str].connect(self.filter_POI)
        self.poiList = QtWidgets.QListWidget(self.poiView)
        self.poiList.setGeometry(QtCore.QRect(10, 80, 231, 551))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.poiList.setFont(font)
        self.poiList.setObjectName("poiList")
        self.glass_3 = QtWidgets.QLabel(self.poiView)
        self.glass_3.setGeometry(QtCore.QRect(190, 30, 51, 31))
        self.glass_3.setText("")
        self.glass_3.setPixmap(QtGui.QPixmap("../../cliparts-for-powerpoint-transparent-magnifying-glass-md.png"))
        self.glass_3.setScaledContents(True)
        self.glass_3.setObjectName("glass_3")
        self.poiSearchButton = QtWidgets.QPushButton(self.poiView)
        self.poiSearchButton.setGeometry(QtCore.QRect(180, 30, 61, 31))
        self.poiSearchButton.setObjectName("poiSearchButton")
        self.poiDeleteButton = QtWidgets.QPushButton(self.poiView)
        self.poiDeleteButton.setGeometry(QtCore.QRect(130, 640, 113, 32))
        self.poiDeleteButton.setObjectName("poiDeleteButton")
        self.poiDetailedView = QtWidgets.QGroupBox(self.poiTab)
        self.poiDetailedView.setGeometry(QtCore.QRect(310, 10, 991, 681))
        self.poiDetailedView.setTitle("")
        self.poiDetailedView.setObjectName("poiDetailedView")
        self.pluginPoiLabel = QtWidgets.QLabel(self.poiDetailedView)
        self.pluginPoiLabel.setGeometry(QtCore.QRect(40, 20, 51, 16))
        self.pluginPoiLabel.setObjectName("pluginPoiLabel")
        self.poiFilterLabel = QtWidgets.QLabel(self.poiDetailedView)
        self.poiFilterLabel.setGeometry(QtCore.QRect(40, 70, 71, 16))
        self.poiFilterLabel.setObjectName("poiFilterLabel")
        self.poiSaveButton = QtWidgets.QPushButton(self.poiDetailedView)
        self.poiSaveButton.setGeometry(QtCore.QRect(820, 620, 113, 32))
        self.poiSaveButton.setObjectName("poiSaveButton")
        self.poiPluginDropDown = QtWidgets.QComboBox(self.poiDetailedView)
        self.poiPluginDropDown.setGeometry(QtCore.QRect(110, 10, 131, 32))
        self.poiPluginDropDown.setObjectName("poiPluginDropDown")
        self.poiPluginDropDown.addItem("")
        self.poiFilterDropDown = QtWidgets.QComboBox(self.poiDetailedView)
        self.poiFilterDropDown.setGeometry(QtCore.QRect(110, 60, 131, 32))
        self.poiFilterDropDown.setEditable(False)
        self.poiFilterDropDown.setObjectName("poiFilterDropDown")
        self.poiFilterDropDown.addItem("")
        self.detailedPoiViewLabel = QtWidgets.QLabel(self.poiDetailedView)
        self.detailedPoiViewLabel.setGeometry(QtCore.QRect(40, 120, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.detailedPoiViewLabel.setFont(font)
        self.detailedPoiViewLabel.setObjectName("detailedPoiViewLabel")
        self.poiViewField = QtWidgets.QTextBrowser(self.poiDetailedView)
        self.poiViewField.setGeometry(QtCore.QRect(30, 140, 891, 461))
        self.poiViewField.setObjectName("poiViewField")
        self.UI.addTab(self.poiTab, "")
        self.Documentation = QtWidgets.QWidget()
        self.Documentation.setObjectName("Documentation")
        self.detailedDocumentView = QtWidgets.QGroupBox(self.Documentation)
        self.detailedDocumentView.setGeometry(QtCore.QRect(310, 10, 991, 681))
        self.detailedDocumentView.setTitle("")
        self.detailedDocumentView.setObjectName("detailedDocumentView")
        self.documentViewField = QtWidgets.QTextEdit(self.detailedDocumentView)
        self.documentViewField.setGeometry(QtCore.QRect(20, 30, 911, 631))
        self.documentViewField.setObjectName("documentViewField")
        self.detailedDocumentationViewLabel = QtWidgets.QLabel(self.detailedDocumentView)
        self.detailedDocumentationViewLabel.setGeometry(QtCore.QRect(10, 0, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.detailedDocumentationViewLabel.setFont(font)
        self.detailedDocumentationViewLabel.setObjectName("detailedDocumentationViewLabel")
        self.documentView = QtWidgets.QGroupBox(self.Documentation)
        self.documentView.setGeometry(QtCore.QRect(20, 10, 261, 681))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.documentView.setFont(font)
        self.documentView.setObjectName("documentView")
        self.documentSearch = QtWidgets.QLineEdit(self.documentView)
        self.documentSearch.setGeometry(QtCore.QRect(10, 30, 231, 31))
        self.documentSearch.setObjectName("documentSearch")
        self.documentSearch.textChanged[str].connect(self.filter_doc)
        self.documentList = QtWidgets.QListWidget(self.documentView)
        self.documentList.setGeometry(QtCore.QRect(10, 80, 231, 581))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.documentList.setFont(font)
        self.documentList.setObjectName("documentList")
        self.searchDocumentButton = QtWidgets.QPushButton(self.documentView)
        self.searchDocumentButton.setGeometry(QtCore.QRect(180, 30, 61, 31))
        self.searchDocumentButton.setObjectName("searchDocumentButton")
        self.UI.addTab(self.Documentation, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.newPluginButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.newPOIButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.outputFieldViewButton.setFocusPolicy(QtCore.Qt.NoFocus)

        self.retranslateUi(MainWindow)
        self.UI.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.fileProperties.append("Name\t\t\tValue\n")

        self.projectNameField.setEnabled(False)
        self.projectDescriptionField.setEnabled(False)
        self.binaryFilePathField.setEnabled(False)
        self.projectDeleteButton.setEnabled(False)

        self.pluginStructureField.setEnabled(False)
        self.pluginPredefinedField.setEnabled(False)
        self.pluginNameField.setEnabled(False)
        self.deletePluginButton.setEnabled(False)

        self.projectNewButton.clicked.connect(self.projectWindow)

        self.newPluginButton.clicked.connect(self.pluginWindow)

        self.saveProjectButton.setEnabled(False)

        self.runStaticButton.clicked.connect(self.runStaticAnalysis)

        self.projectList.clicked.connect(self.projectClicked)

        self.poiAnalysisList.itemSelectionChanged.connect(self.analysisClicked)

        self.poiAnalysisList.itemChanged.connect(self.removeBreakpoint)

        self.runList.clicked.connect(self.runClicked)

        self.pluginManagementList.clicked.connect(self.pluginClicked)

        self.poiList.clicked.connect(self.poiClicked)

        self.documentList.clicked.connect(self.documentationClicked)

        self.deletePluginButton.clicked.connect(self.deletePlugin)

        self.poiTypeDropDownAnalysis.activated.connect(self.displayPOI)

        for document in self.collection.find():
            self.projectList.addItem(document.get("Project Name"))

        for document in self.collection.find():
            self.pluginManagementList.addItem(document.get("Plugin Name"))

        self.projectDeleteButton.clicked.connect(self.deleteConfirmation)
        # self.deletePluginButton.clicked.connect(self.deleteConfirmation)

        self.terminalField.setReadOnly(True)

    def setupUiDeleteProjectConfirmation(self, DeleteProjectConfirmation):
        DeleteProjectConfirmation.setObjectName("deleteProjectConfirmation")
        DeleteProjectConfirmation.resize(400, 99)
        self.buttonBox = QtWidgets.QDialogButtonBox(DeleteProjectConfirmation)
        self.buttonBox.setGeometry(QtCore.QRect(30, 50, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText("Yes")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setText("No")
        self.buttonBox.setObjectName("buttonBox")
        self.messageLabel = QtWidgets.QLabel(DeleteProjectConfirmation)
        self.messageLabel.setGeometry(QtCore.QRect(10, 10, 371, 31))
        self.messageLabel.setObjectName("messageLabel")
        self.messageLabel_2 = QtWidgets.QLabel(DeleteProjectConfirmation)
        self.messageLabel_2.setGeometry(QtCore.QRect(10, 30, 371, 31))
        self.messageLabel_2.setObjectName("messageLabel_2")

        self.retranslateUiDeleteProjectConfirmation(DeleteProjectConfirmation)
        self.buttonBox.accepted.connect(DeleteProjectConfirmation.accept)
        self.buttonBox.rejected.connect(DeleteProjectConfirmation.reject)
        QtCore.QMetaObject.connectSlotsByName(DeleteProjectConfirmation)

        self.buttonBox.accepted.connect(
            lambda: self.deleteProject()
        )

    def setupUiCreateProject(self, NewProject):
        NewProject.setObjectName("NewProject")
        NewProject.resize(539, 333)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewProject)
        self.buttonBox.setGeometry(QtCore.QRect(110, 290, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).setText("Create")
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
        self.binaryFilePathBrowse.setGeometry(QtCore.QRect(454, 80, 81, 31))
        self.binaryFilePathBrowse.setObjectName("binaryFilePathBrowse")

        self.retranslateUiCreateProject(NewProject)
        self.buttonBox.accepted.connect(NewProject.accept)
        self.buttonBox.rejected.connect(NewProject.reject)
        QtCore.QMetaObject.connectSlotsByName(NewProject)

        self.binaryFilePathEdit.setEnabled(False)

        self.binaryFilePathBrowse.clicked.connect(self.getBinaryFilePath)

        self.buttonBox.accepted.connect(
            lambda: self.createProject(self.projectNameEdit.toPlainText(), self.binaryFilePathEdit.toPlainText(),
                                       self.projectDescriptionEdit.toPlainText())
        )

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

        self.brosweDSWindow.clicked.connect(self.BrowseDataSet)
        self.browseStructWindow.clicked.connect(self.BrowseStruct)

        self.buttonBox.accepted.connect(
            lambda: self.createPlugin(self.pluginNameEdit.toPlainText(), self.pluginDescriptionEdit.toPlainText(),
                                      self.structureFieldWindow.toPlainText(), self.datasetFieldWindow.toPlainText()))

    def setupUiBinaryError(self, binaryFileErrorWindow):
        binaryFileErrorWindow.setObjectName("binaryFileErrorWindow")
        binaryFileErrorWindow.resize(400, 99)
        self.buttonBox = QtWidgets.QDialogButtonBox(binaryFileErrorWindow)
        self.buttonBox.setGeometry(QtCore.QRect(30, 50, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.messageLabel = QtWidgets.QLabel(binaryFileErrorWindow)
        self.messageLabel.setGeometry(QtCore.QRect(10, 10, 371, 31))
        self.messageLabel.setObjectName("messageLabel")

        self.retranslateUiBinaryError(binaryFileErrorWindow)
        self.buttonBox.accepted.connect(binaryFileErrorWindow.accept)
        self.buttonBox.rejected.connect(binaryFileErrorWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(binaryFileErrorWindow)

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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BEAT: Binary Extraction and Analysis Tool"))
        self.projectViewGroup.setTitle(_translate("MainWindow", "Project View"))
        self.projectNewButton.setText(_translate("MainWindow", "New"))
      #  self.projectSearch.setHtml(_translate("MainWindow",
                                        #      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          #    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          #    "p, li { white-space: pre-wrap; }\n"
                                            #  "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                            #  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:13pt;\"><br /></p></body></html>"))
        self.projectSearchButton.setText(_translate("MainWindow", "🔍 "))
        self.projectDeleteButton.setText(_translate("MainWindow", "- Delete"))
        self.saveProjectButton.setText(_translate("MainWindow", "+ Save"))
        self.projectNameLabel.setText(_translate("MainWindow", "Project Name"))
        self.projectDescriptionLabel.setText(_translate("MainWindow", "Project Description"))
        self.binaryFilePathLabel.setText(_translate("MainWindow", "Binary File Path"))
        self.binaryFilePropertiesLabel.setText(_translate("MainWindow", "Binary File Properties"))
        self.detailedProjectViewLabel.setText(_translate("MainWindow", "Detailed Project View"))
        self.UI.setTabText(self.UI.indexOf(self.projectTab), _translate("MainWindow", self.projectTabName))
        self.detailedAnalysisViewLabel.setText(_translate("MainWindow", "Detailed Analysis View"))
        self.terminalLabel.setText(_translate("MainWindow", "Terminal"))
        self.outputFieldViewButton.setText(_translate("MainWindow", "Output Field View"))
        self.deleteAnalysisResultButton.setText(_translate("MainWindow", "Delete Analysis Result"))
        self.pluginLabel.setText(_translate("MainWindow", "Plugin"))
        self.staticAnalysisLabel.setText(_translate("MainWindow", "Static Analysis"))
        self.poiTypeLabel.setText(_translate("MainWindow", "POI Type"))
        self.dynamicAnalysisLabel.setText(_translate("MainWindow", "Dynamic Analysis"))
        self.pluginDropDownAnalysis.setItemText(0, _translate("MainWindow", "Select"))
        self.runStaticButton.setText(_translate("MainWindow", "Run"))
        self.poiTypeDropDownAnalysis.setItemText(0, _translate("MainWindow", "Select"))
        self.runDynamicButton.setText(_translate("MainWindow", "Run"))
        self.stopDynamicButton.setText(_translate("MainWindow", "Stop"))
        self.analysisView.setTitle(_translate("MainWindow", "Analysis View"))
        self.commentViewButton.setText(_translate("MainWindow", "Comment View"))
        self.UI.setTabText(self.UI.indexOf(self.analysisTab), _translate("MainWindow", self.analysisTabName))
        self.pluginView.setTitle(_translate("MainWindow", "Plugin View"))
        self.newPluginButton.setText(_translate("MainWindow", "New"))
        #self.pluginSearch.setHtml(_translate("MainWindow",
                                       #      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        #     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         #    "p, li { white-space: pre-wrap; }\n"
                                          #   "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                           #  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.searchPluginButton.setText(_translate("MainWindow", "🔍 "))
        self.deletePluginButton.setText(_translate("MainWindow", "- Delete"))
        self.pluginStructureLabel.setText(_translate("MainWindow", "Plugin Structure"))
        self.pluginPredefinedLabel.setText(_translate("MainWindow", "Plugin Predefined Data Set"))
        self.pluginNameLabel.setText(_translate("MainWindow", "Plugin Name"))
        self.pluginDescriptionLabel.setText(_translate("MainWindow", "Plugin Description"))
        self.defaultOutputFieldLabel.setText(_translate("MainWindow", "Default Output Field"))
        self.poiLabel.setText(_translate("MainWindow", "Points of Interest"))
        self.outputFieldDropDown.setItemText(0, _translate("MainWindow", "Output Field"))
        self.savePluginButton.setText(_translate("MainWindow", "+ Save"))
        self.detailedPluginViewLabel.setText(_translate("MainWindow", "Detailed Plugin View"))
        self.XMLEditorButton.setText(_translate("MainWindow", "XML Editor"))
        self.UI.setTabText(self.UI.indexOf(self.pluginManagementTab), _translate("MainWindow", "Plugin Management"))
        self.poiView.setTitle(_translate("MainWindow", "Point of Interest View"))
        self.newPOIButton.setText(_translate("MainWindow", "New"))
       # self.poiSearch.setHtml(_translate("MainWindow",
                                #          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                 #         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                  #        "p, li { white-space: pre-wrap; }\n"
                                     #     "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                     #     "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.poiSearchButton.setText(_translate("MainWindow", "🔍 "))
        self.poiDeleteButton.setText(_translate("MainWindow", "- Delete"))
        self.pluginPoiLabel.setText(_translate("MainWindow", "Plugin"))
        self.poiFilterLabel.setText(_translate("MainWindow", "POI Filter"))
        self.poiSaveButton.setText(_translate("MainWindow", "+ Save"))
        self.poiPluginDropDown.setItemText(0, _translate("MainWindow", "Select"))
        self.poiFilterDropDown.setItemText(0, _translate("MainWindow", "Select"))
        self.detailedPoiViewLabel.setText(_translate("MainWindow", "Detailed Points of Interest View"))
        self.UI.setTabText(self.UI.indexOf(self.poiTab), _translate("MainWindow", "Points of Interest"))
       # self.documentViewField.setHtml(_translate("MainWindow",
                                              #    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               #   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               #   "p, li { white-space: pre-wrap; }\n"
                                                #  "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                #  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.detailedDocumentationViewLabel.setText(_translate("MainWindow", "Detailed Documentation View"))
        self.documentView.setTitle(_translate("MainWindow", "Documentation View"))
      #  self.documentSearch.setHtml(_translate("MainWindow",
                                           #    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             #  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             #  "p, li { white-space: pre-wrap; }\n"
                                             #  "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                              # "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.searchDocumentButton.setText(_translate("MainWindow", "🔍 "))
        self.UI.setTabText(self.UI.indexOf(self.Documentation), _translate("MainWindow", "Documentation"))

    def retranslateUiCreateProject(self, NewProject):
        _translate = QtCore.QCoreApplication.translate
        NewProject.setWindowTitle(_translate("NewProject", "New Project"))
        self.projectNameLabel.setText(_translate("NewProject", "Project Name"))
        self.projectDescriptionLabel.setText(_translate("NewProject", "Project Description"))
        self.binaryFilePathLabel.setText(_translate("NewProject", "Binary File Path"))
        self.binaryFilePathBrowse.setText(_translate("NewProject", "Browse"))

    def retranslateUiCreatePlugin(self, newPlugin):
        _translate = QtCore.QCoreApplication.translate
        newPlugin.setWindowTitle(_translate("newPlugin", "Create New Plugin"))
        self.projectNameLabel.setText(_translate("newPlugin", "Plugin Name"))
        self.pluginDescriptionLabel.setText(_translate("newPlugin", "Plugin Description"))
        self.pluginStructlabel.setText(_translate("newPlugin", "Plugin Structure"))
        self.pluginDatasetLabel.setText(_translate("newPlugin", "Plugin Dataset"))
        self.browseStructWindow.setText(_translate("newPlugin", "Browse"))
        self.brosweDSWindow.setText(_translate("newPlugin", "Browse"))

    def retranslateUiDeleteProjectConfirmation(self, DeleteProjectConfirmation):
        _translate = QtCore.QCoreApplication.translate
        DeleteProjectConfirmation.setWindowTitle(_translate("deleteProjectConfirmation", "Delete Project Confirmation"))
        self.messageLabel.setText(
            _translate("deleteProjectConfirmation", "You are about to delete permanently a project. Are you sure"))
        self.messageLabel_2.setText(_translate("deleteProjectConfirmation", "you want to delete it?"))

    def retranslateUiBinaryError(self, binaryFileErrorWindow):
        _translate = QtCore.QCoreApplication.translate
        binaryFileErrorWindow.setWindowTitle(
            _translate("binaryFileErrorWindow", "Error Message: x86 Architecture Binary File"))
        self.messageLabel.setText(
            _translate("binaryFileErrorWindow", "     The system only supports x86 architecture files."))

    def retranslatePluginError(self, pluginSelected):
        _translate = QtCore.QCoreApplication.translate
        pluginSelected.setWindowTitle(_translate("pluginSelected", "Error Message: Plugin Selected"))
        self.messageLabel.setText(
            _translate("pluginSelected", "You need to select a plugin before running an analysis."))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
