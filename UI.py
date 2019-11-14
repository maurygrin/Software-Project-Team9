# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import os, sys, r2pipe, json, base64
import pymongo
from pymongo import MongoClient
from Script import Script

from Project import Project
from BinaryFile import BinaryFile
from Metadata import Metadata

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

import XML
from newProject import Ui_newProject
from XML import Notepad

from pathlib import Path, PureWindowsPath


class Ui_MainWindow(object):

    def __init__(self):
        self.windowNew = QtWidgets.QDialog()
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
        self.s = ""
        self.v = ""
        self.f = ""
        self.d = ""
        self.value = ""
        self.section = ""
        self.display = ""
        cluster = MongoClient("mongodb://localhost:27017/")
        db = cluster.test
        self.collection = db["test"]

    def isStaticButtonPressed(self):

        if (self.pluginDropDownAnalysis.currentText() == "Select"):
            self.setupPluginError(self.windowPluginError)
            self.windowPluginError.show()

        else:

            self.runDynamicButton.setEnabled(True)

            self.static = 1

            poiSelected = self.poiTypeDropDownAnalysis.currentText()

            self.analysis = Script()

            if (poiSelected=="Strings"):
                self.display = "strings"
                self.detailedPoiAnalysisField.setText("")
                self.poiAnalysisList.clear()
                self.detailedPoiAnalysisField.append("\t" + "\n")
                self.detailedPoiAnalysisField.append("\t" + "Value: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Section: ")
                font = self.detailedPoiAnalysisField.font()
                font.setPointSize(30)
                self.detailedPoiAnalysisField.setFont(font)
                self.detailedPoiAnalysisField.repaint()
                self.s = self.analysis.display(self.r2, self.display)
                for item in self.s:
                    self.poiAnalysisList.addItem(base64.b64decode(item["string"]).decode())

            elif (poiSelected=="Variables"):
                self.display = "variables"
                self.detailedPoiAnalysisField.setText("")
                self.poiAnalysisList.clear()
                self.v = self.analysis.display(self.r2, self.display)
                print(self.v)
                #for item in self.v:
                    #print(base64.b64decode(item["string"]).decode())
                    #self.poiAnalysisList.addItem(base64.b64decode(item["string"]).decode())
                #self.detailedPoiAnalysisField.setText(v)
                #self.detailedPoiAnalysisField.repaint()

            elif (poiSelected=="Functions"):
                self.display = "functions"
                self.poiAnalysisList.clear()
                self.f = self.analysis.display(self.r2, self.display)
                print(self.f)
                #display = "strings"
                #self.f = self.analysis.display(self.r2, display)
                #for item in self.f:
                  #  self.poiAnalysisList.addItem(base64.b64decode(item["string"]).decode())
                #self.detailedPoiAnalysisField.setText(f)
                #self.detailedPoiAnalysisField.repaint()

            elif (poiSelected=="DLLs"):
                self.display = "dlls"
                self.detailedPoiAnalysisField.setText("")

                self.detailedPoiAnalysisField.append("\t" + "Order of Parameters: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Parameter Type: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Parameter Value: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Return Type: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Return Value: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Relation: ")
                font = self.detailedPoiAnalysisField.font()
                font.setPointSize(15)
                self.detailedPoiAnalysisField.setFont(font)
                self.detailedPoiAnalysisField.repaint()
                self.poiAnalysisList.clear()
                self.d = self.analysis.display(self.r2, self.display)
                for item in self.d:
                    self.poiAnalysisList.addItem(item["name"])

                print(self.d)

            else:
                self.detailedPoiAnalysisField.setText("")
                self.detailedPoiAnalysisField.repaint()


    def displayPOI(self):
        if(self.static == 1):

            poiSelected = self.poiTypeDropDownAnalysis.currentText()

            if (poiSelected=="Strings"):
                self.display = "strings"
                self.detailedPoiAnalysisField.setText("")
                self.poiAnalysisList.clear()
                self.detailedPoiAnalysisField.append("\t" + "\n")
                self.detailedPoiAnalysisField.append("\t" + "Value: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Section: ")
                font = self.detailedPoiAnalysisField.font()
                font.setPointSize(30)
                self.detailedPoiAnalysisField.setFont(font)
                self.detailedPoiAnalysisField.repaint()
                self.s = self.analysis.display(self.r2, self.display)
                for item in self.s:
                    print(item)
                    self.poiAnalysisList.addItem(base64.b64decode(item["string"]).decode())

            elif (poiSelected=="Variables"):
                self.display = "variables"
                self.poiAnalysisList.clear()
                self.detailedPoiAnalysisField.setText("")
                self.detailedPoiAnalysisField.append("\t" + "\n")
                self.detailedPoiAnalysisField.append("\t" + "Order of Parameters: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Parameter Type: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Parameter Value: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Return Type: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Return Value: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Relation: ")
                font = self.detailedPoiAnalysisField.font()
                font.setPointSize(5)
                self.detailedPoiAnalysisField.setFont(font)
                self.detailedPoiAnalysisField.repaint()
                self.poiAnalysisList.clear()
                self.v = self.analysis.display(self.r2, self.display)
                #self.detailedPoiAnalysisField.setText(v)
                #self.detailedPoiAnalysisField.repaint()

            elif (poiSelected=="Functions"):
                self.display = "functions"
                #self.poiAnalysisList.clear()
                self.f = self.analysis.display(self.r2, self.display)
                self.detailedPoiAnalysisField.setText(self.f)
                self.detailedPoiAnalysisField.repaint()

            elif (poiSelected=="DLLs"):
                self.display = "dlls"
                self.detailedPoiAnalysisField.setText("")
                self.detailedPoiAnalysisField.append("\t" + "\n")
                self.detailedPoiAnalysisField.append("\t" + "Order of Parameters: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Parameter Type: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Parameter Value: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Return Type: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Return Value: ")
                self.detailedPoiAnalysisField.append("\n")
                self.detailedPoiAnalysisField.append("\t" + "Relation: ")
                font = self.detailedPoiAnalysisField.font()
                font.setPointSize(20)
                self.detailedPoiAnalysisField.setFont(font)
                self.detailedPoiAnalysisField.repaint()
                self.poiAnalysisList.clear()
                self.d = self.analysis.display(self.r2, self.display)
                for item in self.d:
                    self.poiAnalysisList.addItem(item["name"])
                #self.detailedPoiAnalysisField.setText(d)
                #self.detailedPoiAnalysisField.repaint()

            else:
                self.detailedPoiAnalysisField.setText("")
                self.detailedPoiAnalysisField.repaint()


    def isDynamicButtonPressed(self):
        self.stopButton.setEnabled(True)
        self.runButtonDynamic.setEnabled(False)
        self.r2.cmd('oo')
        x = self.r2.cmd('ood')
        print(x)

    def isStopButtonPressed(self):
        self.runButtonDynamic.setEnabled(True)
        self.stopButton.setEnabled(False)
        self.textEdit_3.repaint()

    def analysisResultWindow(self):
        self.setupAnalysisResultView(self.windowAnalysisResult)
        self.windowAnalysisResult.show()

    def outputFieldWindow(self):
        self.setupOutputFieldView(self.windowOutputField)
        self.windowOutputField.show()

    def commentWindow(self):
        self.setupCommentView(self.windowComment)
        self.windowComment.show()

    def projectWindow(self):
        self.setupUiCreate(self.windowNew)
        self.windowNew.show()

    def saveProject(self):
        if self.binaryFilePathField.text() == "":
            self.fileErrorWindow()
        else:
            #Save Project

            project = {"Project Name" : self.project.name,
                       "Project Description" : self.project.description,
                       "Binary File Path" : self.project.binary.path,
                       "arch" : self.project.binary.metadata.arch,
                       "os" : self.project.binary.metadata.os,
                       "bintype": self.project.binary.metadata.binaryType,
                       "machine" : self.project.binary.metadata.machine,
                       "class" : self.project.binary.metadata.classVariable,
                       "bits": self.project.binary.metadata.bits,
                       "language" : self.project.binary.metadata.language,
                       "canary" : self.project.binary.metadata.canary,
                       "endian": self.project.binary.metadata.endian,
                       "crypto" : self.project.binary.metadata.crypto,
                       "nx" : self.project.binary.metadata.nx,
                       "pic": self.project.binary.metadata.pic,
                       "relocs" : self.project.binary.metadata.relocs,
                       "stripped" : self.project.binary.metadata.stripped,
                       "extension" : self.project.binary.metadata.type}

            self.collection.insert([project])

            self.projectList.addItem(self.project.name)


    def deleteProject(self):
        if self.binaryFilePathField.text() == "":
            self.fileErrorWindow()
        else:
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


    def createProject(self, name, description):
        if not name or not description:
            print("Failed")
        else:
            self.project = Project(name, description, self.binary)
            self.projectNameField.setText(self.project.name)
            self.projectDescriptionField.setText(self.project.description)

    def binaryErrorWindow(self):
        self.setupUiBinaryError(self.windowBinaryError)
        self.windowBinaryError.show()

    def fileErrorWindow(self):
        self.setupUiFileError(self.windowFileError)
        self.windowFileError.show()

    def getBinaryFilePath(self):
        filename = QFileDialog.getOpenFileName(self.centralwidget, 'Open File', os.getenv('HOME'))
        if filename[0]:
            self.path = str(filename)
            # self.analysis = Script()
            self.path = self.path.replace("(", "").replace("'", "").split(",")[0]

            self.r2 = r2pipe.open(self.path)

            self.binaryInfo = self.r2.cmdj('ij')

            self.metadata = Metadata(self.binaryInfo.get("bin").get("arch"), self.binaryInfo.get("bin").get("os"), self.binaryInfo.get("bin").get("bintype"),
                                     self.binaryInfo.get("bin").get("machine"), self.binaryInfo.get("bin").get("class"), self.binaryInfo.get("bin").get("bits"),
                                     self.binaryInfo.get("bin").get("lang"), self.binaryInfo.get("bin").get("canary"), self.binaryInfo.get("bin").get("endian"),
                                     self.binaryInfo.get("bin").get("crypto"), self.binaryInfo.get("bin").get("nx"), self.binaryInfo.get("bin").get("pic"),
                                     self.binaryInfo.get("bin").get("relocs"), self.binaryInfo.get("bin").get("striped"), self.binaryInfo.get("core").get("type"))

            self.binary = BinaryFile(self.path, self.metadata)

            #print(self.binaryInfo)
            #print(self.binaryInfo.get("core").get("type"))
            try:
                if (self.binary.metadata.arch != "x86") or (self.binary.metadata.type != "Executable file" and self.binary.metadata.type != "EXEC (Executable file)"):
                    self.binaryErrorWindow()
                    self.r2 = ""
                    self.fileProperties.setText("")
                    self.binaryFilePathField.setText("")
                else:
                    self.binaryFilePathField.setText(str(self.path))
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

            except Exception as e:
                self.binaryErrorWindow()
                self.r2 = ""
                self.fileProperties.setText("")
                self.binaryFilePathField.setText("")

    def clickedProject(self):

        #item = self.projectList.currentItem()
        #print(item.text())

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



    def openWindow(self):
        r = QMessageBox()
        r.setWindowTitle("Confirmation Window")
        r.setText("Are you sure that you want to save?")
        r.setIcon(QMessageBox.Information)
        r.setStandardButtons(QMessageBox.Cancel | QMessageBox.Save)

    def setupUiMain(self, MainWindow):

        self.path = ""
        self.static = 0
        self.analysis = ""
        self.r2 = ""
        self.binaryInfo = ""
        self.project = ""
        self.binary = ""
        self.metadata = ""

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1318, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.UI = QtWidgets.QTabWidget(self.centralwidget)
        self.UI.setGeometry(QtCore.QRect(0, 0, 1281, 721))
        self.UI.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.UI.setElideMode(QtCore.Qt.ElideLeft)
        self.UI.setDocumentMode(True)
        self.UI.setTabsClosable(False)
        self.UI.setMovable(True)
        self.UI.setTabBarAutoHide(False)
        self.UI.setObjectName("UI")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.projectViewGroup = QtWidgets.QGroupBox(self.tab)
        self.projectViewGroup.setGeometry(QtCore.QRect(20, 10, 261, 681))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.projectViewGroup.setFont(font)
        self.projectViewGroup.setObjectName("projectViewGroup")
        self.projectNewButton = QtWidgets.QPushButton(self.projectViewGroup)
        self.projectNewButton.setGeometry(QtCore.QRect(130, 620, 113, 32))
        self.projectNewButton.setObjectName("projectNewButton")
        self.projectList = QtWidgets.QListWidget(self.projectViewGroup)
        self.projectList.setGeometry(QtCore.QRect(10, 80, 231, 521))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.projectList.setFont(font)
        self.projectList.setObjectName("projectList")
        self.projectSearch = QtWidgets.QTextEdit(self.projectViewGroup)
        self.projectSearch.setGeometry(QtCore.QRect(10, 30, 231, 31))
        self.projectSearch.setObjectName("projectSearch")
        self.glass = QtWidgets.QLabel(self.projectViewGroup)
        self.glass.setGeometry(QtCore.QRect(190, 30, 51, 31))
        self.glass.setText("")
        self.glass.setPixmap(QtGui.QPixmap("../../cliparts-for-powerpoint-transparent-magnifying-glass-md.png"))
        self.glass.setScaledContents(True)
        self.glass.setObjectName("glass")
        self.projectSearchButton = QtWidgets.QPushButton(self.projectViewGroup)
        self.projectSearchButton.setGeometry(QtCore.QRect(180, 30, 61, 31))
        self.projectSearchButton.setObjectName("projectSearchButton")
        self.detailedProjectViewGroup = QtWidgets.QGroupBox(self.tab)
        self.detailedProjectViewGroup.setGeometry(QtCore.QRect(310, 10, 951, 681))
        self.detailedProjectViewGroup.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.detailedProjectViewGroup.setFont(font)
        self.detailedProjectViewGroup.setTitle("")
        self.detailedProjectViewGroup.setFlat(True)
        self.detailedProjectViewGroup.setObjectName("detailedProjectViewGroup")
        self.projectNameLabel = QtWidgets.QLabel(self.detailedProjectViewGroup)
        self.projectNameLabel.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.projectNameLabel.setObjectName("projectNameLabel")
        self.projectDescriptionLabel = QtWidgets.QLabel(self.detailedProjectViewGroup)
        self.projectDescriptionLabel.setGeometry(QtCore.QRect(10, 60, 141, 16))
        self.projectDescriptionLabel.setObjectName("projectDescriptionLabel")
        self.binaryFilePathLabel = QtWidgets.QLabel(self.detailedProjectViewGroup)
        self.binaryFilePathLabel.setGeometry(QtCore.QRect(10, 140, 131, 16))
        self.binaryFilePathLabel.setObjectName("binaryFilePathLabel")
        self.binaryFilePropertiesLabel = QtWidgets.QLabel(self.detailedProjectViewGroup)
        self.binaryFilePropertiesLabel.setGeometry(QtCore.QRect(10, 170, 151, 16))
        self.binaryFilePropertiesLabel.setObjectName("binaryFilePropertiesLabel")
        self.projectNoteLabel1 = QtWidgets.QLabel(self.detailedProjectViewGroup)
        self.projectNoteLabel1.setGeometry(QtCore.QRect(170, 620, 481, 16))
        self.projectNoteLabel1.setObjectName("projectNoteLabel1")
        self.projectBrowseButton = QtWidgets.QPushButton(self.detailedProjectViewGroup)
        self.projectBrowseButton.setGeometry(QtCore.QRect(840, 140, 99, 25))
        self.projectBrowseButton.setObjectName("projectBrowseButton")
        self.projectDeleteButton = QtWidgets.QPushButton(self.detailedProjectViewGroup)
        self.projectDeleteButton.setGeometry(QtCore.QRect(730, 620, 113, 32))
        self.projectDeleteButton.setObjectName("projectDeleteButton")
        self.binaryFilePropertiesField = QtWidgets.QScrollArea(self.detailedProjectViewGroup)
        self.binaryFilePropertiesField.setGeometry(QtCore.QRect(170, 170, 671, 441))
        self.binaryFilePropertiesField.setWidgetResizable(True)
        self.binaryFilePropertiesField.setObjectName("binaryFilePropertiesField")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 669, 439))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.BEAT = QtWidgets.QColumnView(self.scrollAreaWidgetContents)
        self.BEAT.setGeometry(QtCore.QRect(0, 0, 671, 441))
        self.BEAT.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.BEAT.setTabKeyNavigation(True)
        self.BEAT.setDragEnabled(False)
        self.BEAT.setAlternatingRowColors(True)
        self.BEAT.setObjectName("BEAT")
        self.fileProperties = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.fileProperties.setGeometry(QtCore.QRect(0, 0, 671, 441))
        self.fileProperties.setObjectName("fileProperties")
        self.filePropertiesLine = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.filePropertiesLine.setGeometry(QtCore.QRect(220, 0, 16, 471))
        self.filePropertiesLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.filePropertiesLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.filePropertiesLine.setObjectName("filePropertiesLine")
        self.binaryFilePropertiesField.setWidget(self.scrollAreaWidgetContents)
        self.projectSaveButton = QtWidgets.QPushButton(self.detailedProjectViewGroup)
        self.projectSaveButton.setGeometry(QtCore.QRect(620, 620, 113, 32))
        self.projectSaveButton.setObjectName("projectSaveButton")
        self.detailedProjectViewLabel = QtWidgets.QLabel(self.detailedProjectViewGroup)
        self.detailedProjectViewLabel.setGeometry(QtCore.QRect(10, 0, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.detailedProjectViewLabel.setFont(font)
        self.detailedProjectViewLabel.setObjectName("detailedProjectViewLabel")
        self.projectNoteLabel = QtWidgets.QLabel(self.detailedProjectViewGroup)
        self.projectNoteLabel.setGeometry(QtCore.QRect(170, 640, 481, 16))
        self.projectNoteLabel.setObjectName("projectNoteLabel")
        self.projectNameField = QtWidgets.QLineEdit(self.detailedProjectViewGroup)
        self.projectNameField.setGeometry(QtCore.QRect(170, 30, 671, 21))
        self.projectNameField.setObjectName("projectNameField")
        self.projectDescriptionField = QtWidgets.QLineEdit(self.detailedProjectViewGroup)
        self.projectDescriptionField.setGeometry(QtCore.QRect(170, 60, 671, 71))
        self.projectDescriptionField.setObjectName("projectDescriptionField")
        self.binaryFilePathField = QtWidgets.QLineEdit(self.detailedProjectViewGroup)
        self.binaryFilePathField.setGeometry(QtCore.QRect(170, 140, 671, 21))
        self.binaryFilePathField.setObjectName("binaryFilePathField")
        self.UI.addTab(self.tab, "")





        self.analysisTab = QtWidgets.QWidget()
        self.analysisTab.setObjectName("analysisTab")
        self.analysisView = QtWidgets.QGroupBox(self.analysisTab)
        self.analysisView.setGeometry(QtCore.QRect(310, 0, 911, 691))
        self.analysisView.setTitle("")
        self.analysisView.setObjectName("analysisView")
        self.detailedPoiViewLabel = QtWidgets.QLabel(self.analysisView)
        self.detailedPoiViewLabel.setGeometry(QtCore.QRect(40, 130, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.detailedPoiViewLabel.setFont(font)
        self.detailedPoiViewLabel.setObjectName("detailedPoiViewLabel")
        self.analysisResultViewButton = QtWidgets.QPushButton(self.analysisView)
        self.analysisResultViewButton.setGeometry(QtCore.QRect(30, 480, 151, 30))
        self.analysisResultViewButton.setObjectName("analysisResultViewButton")
        self.terminalLabel = QtWidgets.QLabel(self.analysisView)
        self.terminalLabel.setGeometry(QtCore.QRect(40, 520, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.terminalLabel.setFont(font)
        self.terminalLabel.setObjectName("terminalLabel")
        self.detailedPoiAnalysisField = QtWidgets.QTextBrowser(self.analysisView)
        self.detailedPoiAnalysisField.setGeometry(QtCore.QRect(35, 151, 851, 321))
        self.detailedPoiAnalysisField.setObjectName("detailedPoiAnalysisField")
        self.outputFieldViewButton = QtWidgets.QPushButton(self.analysisView)
        self.outputFieldViewButton.setGeometry(QtCore.QRect(380, 480, 151, 30))
        self.outputFieldViewButton.setObjectName("outputFieldViewButton")
        self.commentViewButton = QtWidgets.QPushButton(self.analysisView)
        self.commentViewButton.setGeometry(QtCore.QRect(740, 480, 151, 30))
        self.commentViewButton.setObjectName("commentViewButton")
        self.terminalField = QtWidgets.QTextEdit(self.analysisView)
        self.terminalField.setGeometry(QtCore.QRect(30, 550, 851, 121))
        self.terminalField.setObjectName("terminalField")
        self.pluginLabel = QtWidgets.QLabel(self.analysisTab)
        self.pluginLabel.setGeometry(QtCore.QRect(390, 30, 61, 31))
        self.pluginLabel.setObjectName("pluginLabel")
        self.staticAnalysisLabel = QtWidgets.QLabel(self.analysisTab)
        self.staticAnalysisLabel.setGeometry(QtCore.QRect(750, 40, 101, 21))
        self.staticAnalysisLabel.setObjectName("staticAnalysisLabel")
        self.poiTypeLabel = QtWidgets.QLabel(self.analysisTab)
        self.poiTypeLabel.setGeometry(QtCore.QRect(390, 80, 61, 21))
        self.poiTypeLabel.setObjectName("poiTypeLabel")
        self.dynamicAnalysisLabel = QtWidgets.QLabel(self.analysisTab)
        self.dynamicAnalysisLabel.setGeometry(QtCore.QRect(750, 80, 121, 21))
        self.dynamicAnalysisLabel.setObjectName("dynamicAnalysisLabel")
        self.pluginDropDownAnalysis = QtWidgets.QComboBox(self.analysisTab)
        self.pluginDropDownAnalysis.setGeometry(QtCore.QRect(460, 30, 131, 32))
        self.pluginDropDownAnalysis.setObjectName("pluginDropDownAnalysis")
        self.pluginDropDownAnalysis.addItem("")
        self.pluginDropDownAnalysis.addItem("")
        self.runStaticButton = QtWidgets.QPushButton(self.analysisTab)
        self.runStaticButton.setGeometry(QtCore.QRect(880, 30, 111, 32))
        self.runStaticButton.setObjectName("runStaticButton")
        self.poiTypeDropDownAnalysis = QtWidgets.QComboBox(self.analysisTab)
        self.poiTypeDropDownAnalysis.setGeometry(QtCore.QRect(460, 70, 131, 32))
        self.poiTypeDropDownAnalysis.setEditable(False)
        self.poiTypeDropDownAnalysis.setObjectName("poiTypeDropDownAnalysis")
        self.poiTypeDropDownAnalysis.addItem("")
        self.poiTypeDropDownAnalysis.addItem("")
        self.poiTypeDropDownAnalysis.addItem("")
        self.poiTypeDropDownAnalysis.addItem("")
        self.poiTypeDropDownAnalysis.addItem("")
        self.runDynamicButton = QtWidgets.QPushButton(self.analysisTab)
        self.runDynamicButton.setGeometry(QtCore.QRect(880, 70, 113, 32))
        self.runDynamicButton.setObjectName("runDynamicButton")
        self.stopDynamicButton = QtWidgets.QPushButton(self.analysisTab)
        self.stopDynamicButton.setGeometry(QtCore.QRect(1000, 70, 113, 32))
        self.stopDynamicButton.setObjectName("stopDynamicButton")
        self.poiView = QtWidgets.QGroupBox(self.analysisTab)
        self.poiView.setGeometry(QtCore.QRect(20, 10, 261, 681))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.poiView.setFont(font)
        self.poiView.setObjectName("poiView")
        self.poiAnalysisList = QtWidgets.QListWidget(self.poiView)
        self.poiAnalysisList.setGeometry(QtCore.QRect(10, 40, 231, 621))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.poiAnalysisList.setFont(font)
        self.poiAnalysisList.setObjectName("poiAnalysisList")
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
        self.newPluginButton.setGeometry(QtCore.QRect(130, 620, 113, 32))
        self.newPluginButton.setObjectName("newPluginButton")
        self.pluginSearch = QtWidgets.QTextEdit(self.pluginView)
        self.pluginSearch.setGeometry(QtCore.QRect(10, 30, 231, 31))
        self.pluginSearch.setObjectName("pluginSearch")
        self.pluginManagementList = QtWidgets.QListWidget(self.pluginView)
        self.pluginManagementList.setGeometry(QtCore.QRect(10, 80, 231, 521))
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
        self.detailedPluginView = QtWidgets.QGroupBox(self.pluginManagementTab)
        self.detailedPluginView.setGeometry(QtCore.QRect(310, 10, 951, 681))
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
        self.pluginStructureBrowseButton = QtWidgets.QPushButton(self.detailedPluginView)
        self.pluginStructureBrowseButton.setGeometry(QtCore.QRect(840, 30, 99, 25))
        self.pluginStructureBrowseButton.setObjectName("pluginStructureBrowseButton")
        self.deletePluginButton = QtWidgets.QPushButton(self.detailedPluginView)
        self.deletePluginButton.setGeometry(QtCore.QRect(730, 620, 113, 32))
        self.deletePluginButton.setObjectName("deletePluginButton")
        self.savePluginButton = QtWidgets.QPushButton(self.detailedPluginView)
        self.savePluginButton.setGeometry(QtCore.QRect(620, 620, 113, 32))
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
        self.XMLEditorButton.setGeometry(QtCore.QRect(0, 280, 113, 32))
        self.XMLEditorButton.setObjectName("XMLEditorButton")
        self.pluginStructureField = QtWidgets.QLineEdit(self.detailedPluginView)
        self.pluginStructureField.setGeometry(QtCore.QRect(200, 30, 641, 21))
        self.pluginStructureField.setObjectName("pluginStructureField")
        self.pluginPredefinedField = QtWidgets.QLineEdit(self.detailedPluginView)
        self.pluginPredefinedField.setGeometry(QtCore.QRect(200, 60, 641, 21))
        self.pluginPredefinedField.setObjectName("pluginPredefinedField")
        self.pluginNameField = QtWidgets.QLineEdit(self.detailedPluginView)
        self.pluginNameField.setGeometry(QtCore.QRect(200, 90, 641, 21))
        self.pluginNameField.setObjectName("pluginNameField")
        self.pluginDescriptionField = QtWidgets.QTextEdit(self.detailedPluginView)
        self.pluginDescriptionField.setGeometry(QtCore.QRect(200, 120, 641, 74))
        self.pluginDescriptionField.setObjectName("pluginDescriptionField")
        self.poiPluginField = QtWidgets.QTextEdit(self.detailedPluginView)
        self.poiPluginField.setGeometry(QtCore.QRect(200, 250, 641, 341))
        self.poiPluginField.setObjectName("poiPluginField")
        self.pluginPredifinedButton = QtWidgets.QPushButton(self.pluginManagementTab)
        self.pluginPredifinedButton.setGeometry(QtCore.QRect(1150, 70, 99, 25))
        self.pluginPredifinedButton.setObjectName("pluginPredifinedButton")
        self.UI.addTab(self.pluginManagementTab, "")



        self.poiTab = QtWidgets.QWidget()
        self.poiTab.setObjectName("poiTab")
        self.poiView_2 = QtWidgets.QGroupBox(self.poiTab)
        self.poiView_2.setGeometry(QtCore.QRect(20, 10, 261, 681))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.poiView_2.setFont(font)
        self.poiView_2.setObjectName("poiView_2")
        self.newPOIButton = QtWidgets.QPushButton(self.poiView_2)
        self.newPOIButton.setGeometry(QtCore.QRect(130, 620, 113, 32))
        self.newPOIButton.setObjectName("newPOIButton")
        self.poiSearch = QtWidgets.QTextEdit(self.poiView_2)
        self.poiSearch.setGeometry(QtCore.QRect(10, 30, 231, 31))
        self.poiSearch.setObjectName("poiSearch")
        self.poiList = QtWidgets.QListWidget(self.poiView_2)
        self.poiList.setGeometry(QtCore.QRect(10, 80, 231, 521))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.poiList.setFont(font)
        self.poiList.setObjectName("poiList")
        self.glass_3 = QtWidgets.QLabel(self.poiView_2)
        self.glass_3.setGeometry(QtCore.QRect(190, 30, 51, 31))
        self.glass_3.setText("")
        self.glass_3.setPixmap(QtGui.QPixmap("../../cliparts-for-powerpoint-transparent-magnifying-glass-md.png"))
        self.glass_3.setScaledContents(True)
        self.glass_3.setObjectName("glass_3")
        self.poiSearchButton = QtWidgets.QPushButton(self.poiView_2)
        self.poiSearchButton.setGeometry(QtCore.QRect(180, 30, 61, 31))
        self.poiSearchButton.setObjectName("poiSearchButton")
        self.poiDetailedView = QtWidgets.QGroupBox(self.poiTab)
        self.poiDetailedView.setGeometry(QtCore.QRect(310, 10, 951, 681))
        self.poiDetailedView.setTitle("")
        self.poiDetailedView.setObjectName("poiDetailedView")
        self.pluginPoiLabel = QtWidgets.QLabel(self.poiDetailedView)
        self.pluginPoiLabel.setGeometry(QtCore.QRect(90, 20, 51, 16))
        self.pluginPoiLabel.setObjectName("pluginPoiLabel")
        self.poiFilterLabel = QtWidgets.QLabel(self.poiDetailedView)
        self.poiFilterLabel.setGeometry(QtCore.QRect(90, 50, 71, 16))
        self.poiFilterLabel.setObjectName("poiFilterLabel")
        self.poiSaveButton = QtWidgets.QPushButton(self.poiDetailedView)
        self.poiSaveButton.setGeometry(QtCore.QRect(620, 620, 113, 32))
        self.poiSaveButton.setObjectName("poiSaveButton")
        self.poiPluginDropDown = QtWidgets.QComboBox(self.poiDetailedView)
        self.poiPluginDropDown.setGeometry(QtCore.QRect(160, 10, 131, 32))
        self.poiPluginDropDown.setObjectName("poiPluginDropDown")
        self.poiPluginDropDown.addItem("")
        self.poiPluginDropDown.addItem("")
        self.poiFilterDropDown = QtWidgets.QComboBox(self.poiDetailedView)
        self.poiFilterDropDown.setGeometry(QtCore.QRect(160, 40, 131, 32))
        self.poiFilterDropDown.setEditable(False)
        self.poiFilterDropDown.setObjectName("poiFilterDropDown")
        self.poiFilterDropDown.addItem("")
        self.poiFilterDropDown.addItem("")
        self.poiFilterDropDown.addItem("")
        self.poiFilterDropDown.addItem("")
        self.poiFilterDropDown.addItem("")
        self.detailedPoiViewLabel_2 = QtWidgets.QLabel(self.poiDetailedView)
        self.detailedPoiViewLabel_2.setGeometry(QtCore.QRect(40, 120, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.detailedPoiViewLabel_2.setFont(font)
        self.detailedPoiViewLabel_2.setObjectName("detailedPoiViewLabel_2")
        self.poiViewField = QtWidgets.QTextBrowser(self.poiDetailedView)
        self.poiViewField.setGeometry(QtCore.QRect(30, 140, 891, 461))
        self.poiViewField.setObjectName("poiViewField")
        self.poiDeleteButton = QtWidgets.QPushButton(self.poiTab)
        self.poiDeleteButton.setGeometry(QtCore.QRect(1040, 630, 113, 32))
        self.poiDeleteButton.setObjectName("poiDeleteButton")
        self.UI.addTab(self.poiTab, "")



        self.Documentation = QtWidgets.QWidget()
        self.Documentation.setObjectName("Documentation")
        self.detailedDocumentView = QtWidgets.QGroupBox(self.Documentation)
        self.detailedDocumentView.setGeometry(QtCore.QRect(310, 10, 951, 681))
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
        self.documentSearch = QtWidgets.QTextEdit(self.documentView)
        self.documentSearch.setGeometry(QtCore.QRect(10, 30, 231, 31))
        self.documentSearch.setObjectName("documentSearch")
        self.documentList = QtWidgets.QListWidget(self.documentView)
        self.documentList.setGeometry(QtCore.QRect(10, 80, 231, 581))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.documentList.setFont(font)
        self.documentList.setObjectName("documentList")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        item.setFont(font)
        self.documentList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.documentList.addItem(item)
        self.searchDocumentButton = QtWidgets.QPushButton(self.documentView)
        self.searchDocumentButton.setGeometry(QtCore.QRect(180, 30, 61, 31))
        self.searchDocumentButton.setObjectName("searchDocumentButton")
        self.UI.addTab(self.Documentation, "")



        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUiMain(MainWindow)
        self.UI.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.projectNameField.setEnabled(False)
        self.projectDescriptionField.setEnabled(False)
        self.binaryFilePathField.setEnabled(False)

        self.projectNewButton.clicked.connect(self.projectWindow)

        self.projectBrowseButton.clicked.connect(self.getBinaryFilePath)

        self.fileProperties.setText("Name\t\t\tValue\n")

        self.projectSaveButton.clicked.connect(self.saveProject)

        self.projectDeleteButton.clicked.connect(self.deleteProject)

        self.analysisResultViewButton.clicked.connect(self.analysisResultWindow)

        self.outputFieldViewButton.clicked.connect(self.outputFieldWindow)

        self.commentViewButton.clicked.connect(self.commentWindow)

        self.runStaticButton.clicked.connect(self.isStaticButtonPressed)

        self.runDynamicButton.clicked.connect(self.isDynamicButtonPressed)

        self.stopDynamicButton.clicked.connect(self.isStopButtonPressed)

        self.poiTypeDropDownAnalysis.activated.connect(self.displayPOI)

        self.runDynamicButton.setEnabled(False)

        self.stopDynamicButton.setEnabled(False)

        self.projectList.clicked.connect(self.clickedProject)

        self.poiAnalysisList.clicked.connect(self.clickedPoi)

        self.poiAnalysisList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.poiAnalysisList.customContextMenuRequested.connect(self.listItemRightClicked)

        for document in self.collection.find():
            self.projectList.addItem(document.get("Project Name"))

    def listItemRightClicked(self, QPos):
        self.listMenu = QtWidgets.QMenu()
        menu_breakpoint = self.listMenu.addAction("Add Breakpoint")
        menu_watchpoint = self.listMenu.addAction("Add Watchpoint")
        menu_comment = self.listMenu.addAction("Add Comment")
        menu_breakpoint.triggered.connect(self.menuBreakpointClicked)
        menu_watchpoint.triggered.connect(self.menuWatchpointClicked)
        menu_comment.triggered.connect(self.menuCommentClicked)
        parentPosition = self.poiAnalysisList.mapToGlobal(QtCore.QPoint(0, 0))
        self.listMenu.move(parentPosition + QPos)
        self.listMenu.show()

    def menuBreakpointClicked(self):
        currentItemName = str(self.poiAnalysisList.currentItem().text())
        print("Breakpoint at: " + currentItemName)

    def menuWatchpointClicked(self):
        currentItemName = str(self.poiAnalysisList.currentItem().text())
        print("Watchpoint at: " + currentItemName)

    def menuCommentClicked(self):
        currentItemName = str(self.poiAnalysisList.currentItem().text())
        print("Comment at: " + currentItemName)

    def clickedPoi(self):
        selected = self.poiAnalysisList.currentItem().text()
        if self.display is "strings":
            for item in self.s:
                current = base64.b64decode(item["string"]).decode()
                if current == selected:
                    self.value = str(item["vaddr"])
                    self.section = item["section"]
                    break
            self.detailedPoiAnalysisField.setText("")
            self.detailedPoiAnalysisField.append("\t" + "\n")
            self.detailedPoiAnalysisField.append("\t" + "Value: " + "\t" + self.value)
            self.detailedPoiAnalysisField.append("\n")
            self.detailedPoiAnalysisField.append("\t" + "Section: " + "\t" + self.section)
            font = self.detailedPoiAnalysisField.font()
            font.setPointSize(30)
            self.detailedPoiAnalysisField.setFont(font)
            self.detailedPoiAnalysisField.repaint()

        if self.display is "dlls":
            for item in self.d:
                current = item["name"]
                if current == selected:
                    self.value = str(item["vaddr"])
                    self.section = item["section"]
                    break
            self.detailedPoiAnalysisField.setText("")
            self.detailedPoiAnalysisField.append("\t" + "\n")
            self.detailedPoiAnalysisField.append("\t" + "Order of Parameters: ")
            self.detailedPoiAnalysisField.append("\n")
            self.detailedPoiAnalysisField.append("\t" + "Parameter Type: ")
            self.detailedPoiAnalysisField.append("\n")
            self.detailedPoiAnalysisField.append("\t" + "Parameter Value: ")
            self.detailedPoiAnalysisField.append("\n")
            self.detailedPoiAnalysisField.append("\t" + "Return Type: ")
            self.detailedPoiAnalysisField.append("\n")
            self.detailedPoiAnalysisField.append("\t" + "Return Value: ")
            self.detailedPoiAnalysisField.append("\n")
            self.detailedPoiAnalysisField.append("\t" + "Relation: ")
            font = self.detailedPoiAnalysisField.font()
            font.setPointSize(30)
            self.detailedPoiAnalysisField.setFont(font)
            self.detailedPoiAnalysisField.repaint()


    def setupUiCreate(self, Dialog):

        self.project = ""

        Dialog.setObjectName("New Project")
        Dialog.resize(492, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.projectNameLabel = QtWidgets.QLabel(Dialog)
        self.projectNameLabel.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.projectNameLabel.setObjectName("projectNameLabel")
        self.projectNameEdit = QtWidgets.QTextEdit(Dialog)
        self.projectNameEdit.setGeometry(QtCore.QRect(20, 30, 431, 21))
        self.projectNameEdit.setObjectName("projectNameEdit")
        self.projectDescriptionLabel = QtWidgets.QLabel(Dialog)
        self.projectDescriptionLabel.setGeometry(QtCore.QRect(20, 60, 131, 16))
        self.projectDescriptionLabel.setObjectName("projectDescriptionLabel")
        self.projectDescriptionEdit = QtWidgets.QTextEdit(Dialog)
        self.projectDescriptionEdit.setGeometry(QtCore.QRect(20, 80, 431, 141))
        self.projectDescriptionEdit.setObjectName("projectDescriptionEdit")

        self.retranslateUiCreate(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.buttonBox.accepted.connect(
            lambda: self.createProject(self.projectNameEdit.toPlainText(), self.projectDescriptionEdit.toPlainText()))

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

    def setupUiFileError(self, fileSpecifiedErrorWindow):
        fileSpecifiedErrorWindow.setObjectName("fileSpecifiedErrorWindow")
        fileSpecifiedErrorWindow.resize(400, 99)
        self.buttonBox = QtWidgets.QDialogButtonBox(fileSpecifiedErrorWindow)
        self.buttonBox.setGeometry(QtCore.QRect(30, 60, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.messageLabel = QtWidgets.QLabel(fileSpecifiedErrorWindow)
        self.messageLabel.setGeometry(QtCore.QRect(10, 10, 371, 31))
        self.messageLabel.setObjectName("messageLabel")
        self.messageLabel_2 = QtWidgets.QLabel(fileSpecifiedErrorWindow)
        self.messageLabel_2.setGeometry(QtCore.QRect(10, 30, 371, 31))
        self.messageLabel_2.setObjectName("messageLabel_2")

        self.retranslateUiFileError(fileSpecifiedErrorWindow)
        self.buttonBox.accepted.connect(fileSpecifiedErrorWindow.accept)
        self.buttonBox.rejected.connect(fileSpecifiedErrorWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(fileSpecifiedErrorWindow)

    def setupOutputFieldView(self, OutputFieldView):
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

        self.retranslateOutputFieldView(OutputFieldView)
        QtCore.QMetaObject.connectSlotsByName(OutputFieldView)

    def setupCommentView(self, commentView):
        commentView.setObjectName("commentView")
        commentView.resize(616, 402)
        self.clearButton = QtWidgets.QPushButton(commentView)
        self.clearButton.setGeometry(QtCore.QRect(490, 360, 113, 32))
        self.clearButton.setObjectName("clearButton")
        self.saveCommentButton = QtWidgets.QPushButton(commentView)
        self.saveCommentButton.setGeometry(QtCore.QRect(360, 360, 113, 32))
        self.saveCommentButton.setObjectName("saveCommentButton")
        self.commentField = QtWidgets.QTextEdit(commentView)
        self.commentField.setGeometry(QtCore.QRect(20, 20, 581, 331))
        self.commentField.setObjectName("commentField")

        self.retranslateCommentView(commentView)
        QtCore.QMetaObject.connectSlotsByName(commentView)

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


    def retranslateUiMain(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BEAT: Binary Extraction and Analysis Tool"))
        self.projectViewGroup.setTitle(_translate("MainWindow", "Project View"))
        self.projectNewButton.setText(_translate("MainWindow", "New"))
        self.projectSearch.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-style:italic; color:#7e7e7e;\">Project Search </span></p></body></html>"))
        self.projectSearchButton.setText(_translate("MainWindow", "🔍 "))
        self.projectNameLabel.setText(_translate("MainWindow", "Project Name"))
        self.projectDescriptionLabel.setText(_translate("MainWindow", "Project Description"))
        self.binaryFilePathLabel.setText(_translate("MainWindow", "Binary File Path"))
        self.binaryFilePropertiesLabel.setText(_translate("MainWindow", "Binary File Properties"))
        self.projectNoteLabel1.setText(_translate("MainWindow", "** User cannot modify the binary file path once the project is "))
        self.projectBrowseButton.setText(_translate("MainWindow", "Browse"))
        self.projectDeleteButton.setText(_translate("MainWindow", "- Delete"))
        self.projectSaveButton.setText(_translate("MainWindow", "+ Save"))
        self.detailedProjectViewLabel.setText(_translate("MainWindow", "Detailed Project View"))
        self.projectNoteLabel.setText(_translate("MainWindow", "     created."))
        self.UI.setTabText(self.UI.indexOf(self.tab), _translate("MainWindow", "Project"))



        self.detailedPoiViewLabel.setText(_translate("MainWindow", "Detailed Point of Interest View"))
        self.analysisResultViewButton.setText(_translate("MainWindow", "Analysis Result View"))
        self.terminalLabel.setText(_translate("MainWindow", "Terminal"))
        self.outputFieldViewButton.setText(_translate("MainWindow", "Output Field View"))
        self.commentViewButton.setText(_translate("MainWindow", "Comment View"))
        self.pluginLabel.setText(_translate("MainWindow", "Plugin"))
        self.staticAnalysisLabel.setText(_translate("MainWindow", "Static Analysis"))
        self.poiTypeLabel.setText(_translate("MainWindow", "POI Type"))
        self.dynamicAnalysisLabel.setText(_translate("MainWindow", "Dynamic Analysis"))
        self.pluginDropDownAnalysis.setItemText(0, _translate("MainWindow", "Select"))
        self.pluginDropDownAnalysis.setItemText(1, _translate("MainWindow", "Network"))
        self.runStaticButton.setText(_translate("MainWindow", "Run"))
        self.poiTypeDropDownAnalysis.setItemText(0, _translate("MainWindow", "Select"))
        self.poiTypeDropDownAnalysis.setItemText(1, _translate("MainWindow", "Strings"))
        self.poiTypeDropDownAnalysis.setItemText(2, _translate("MainWindow", "Functions"))
        self.poiTypeDropDownAnalysis.setItemText(3, _translate("MainWindow", "Variables"))
        self.poiTypeDropDownAnalysis.setItemText(4, _translate("MainWindow", "DLLs"))
        self.runDynamicButton.setText(_translate("MainWindow", "Run"))
        self.stopDynamicButton.setText(_translate("MainWindow", "Stop"))
        self.poiView.setTitle(_translate("MainWindow", "Point of Interest View"))
        self.UI.setTabText(self.UI.indexOf(self.analysisTab), _translate("MainWindow", "Analysis"))



        self.pluginView.setTitle(_translate("MainWindow", "Plugin View"))
        self.newPluginButton.setText(_translate("MainWindow", "New"))
        self.pluginSearch.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:13pt; font-style:italic; color:#7e7e7e;\">Plugin </span></p></body></html>"))
        self.searchPluginButton.setText(_translate("MainWindow", "🔍 "))
        self.pluginStructureLabel.setText(_translate("MainWindow", "Plugin Structure"))
        self.pluginPredefinedLabel.setText(_translate("MainWindow", "Plugin Predefined Data Set"))
        self.pluginNameLabel.setText(_translate("MainWindow", "Plugin Name"))
        self.pluginDescriptionLabel.setText(_translate("MainWindow", "Plugin Description"))
        self.defaultOutputFieldLabel.setText(_translate("MainWindow", "Default Output Field"))
        self.poiLabel.setText(_translate("MainWindow", "Points of Interest"))
        self.outputFieldDropDown.setItemText(0, _translate("MainWindow", "Output Field"))
        self.pluginStructureBrowseButton.setText(_translate("MainWindow", "Browse"))
        self.deletePluginButton.setText(_translate("MainWindow", "- Delete"))
        self.savePluginButton.setText(_translate("MainWindow", "+ Save"))
        self.detailedPluginViewLabel.setText(_translate("MainWindow", "Detailed Plugin View"))
        self.XMLEditorButton.setText(_translate("MainWindow", "XML Editor"))
        self.pluginPredifinedButton.setText(_translate("MainWindow", "Browse"))
        self.UI.setTabText(self.UI.indexOf(self.pluginManagementTab), _translate("MainWindow", "Plugin Management"))



        self.poiView_2.setTitle(_translate("MainWindow", "Point of Interest View"))
        self.newPOIButton.setText(_translate("MainWindow", "New"))
        self.poiSearch.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-style:italic; color:#7e7e7e;\">Point of Interest</span></p></body></html>"))
        self.poiSearchButton.setText(_translate("MainWindow", "🔍 "))
        self.pluginPoiLabel.setText(_translate("MainWindow", "Plugin"))
        self.poiFilterLabel.setText(_translate("MainWindow", "POI Filter"))
        self.poiSaveButton.setText(_translate("MainWindow", "+ Save"))
        self.poiPluginDropDown.setItemText(0, _translate("MainWindow", "Select"))
        self.poiPluginDropDown.setItemText(1, _translate("MainWindow", "Network"))
        self.poiFilterDropDown.setItemText(0, _translate("MainWindow", "Select"))
        self.poiFilterDropDown.setItemText(1, _translate("MainWindow", "Strings"))
        self.poiFilterDropDown.setItemText(2, _translate("MainWindow", "Functions"))
        self.poiFilterDropDown.setItemText(3, _translate("MainWindow", "Variables"))
        self.poiFilterDropDown.setItemText(4, _translate("MainWindow", "DLLs"))
        self.detailedPoiViewLabel_2.setText(_translate("MainWindow", "Detailed Points of Interest View"))
        self.poiDeleteButton.setText(_translate("MainWindow", "- Delete"))
        self.UI.setTabText(self.UI.indexOf(self.poiTab), _translate("MainWindow", "Points of Interest"))



        self.documentViewField.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The purpose of the Software Requirements Specification (SRS) is to give the customer a clear and precise description of the functionality of the Behavior Extraction and Analysis Tool (BEAT). The SRS divides the system requirements into two parts, behavioral and non-behavioral requirements. The behavioral requirements describe the interaction between the system and its environment. Non-behavioral requirements relate to the definition of the attributes of the product as it performs its functions. This includes performance requirements of the product. The intended audience of the SRS is Dr. Jaime Acosta, Dr. Oscar Perez, Mr. Vincent Fonseca, Ms. Herandy Vazquez, Mr. Baltazar Santaella, Ms. Florencia Larsen, Mr. Juan Ulloa, Mr. Jesus Martinez, and the Software Engineering teams. This document serves as an agreement between both parties regarding the product to be developed. </p></body></html>"))
        self.detailedDocumentationViewLabel.setText(_translate("MainWindow", "Detailed Documentation View"))
        self.documentView.setTitle(_translate("MainWindow", "Documentation View"))
        self.documentSearch.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-style:italic; color:#7e7e7e;\">Document</span></p></body></html>"))
        __sortingEnabled = self.documentList.isSortingEnabled()
        self.documentList.setSortingEnabled(False)
        item = self.documentList.item(0)
        item.setText(_translate("MainWindow", "BEAT Documentation"))
        item = self.documentList.item(1)
        item.setText(_translate("MainWindow", "Plugin Structure"))
        self.documentList.setSortingEnabled(__sortingEnabled)
        self.searchDocumentButton.setText(_translate("MainWindow", "🔍 "))
        self.UI.setTabText(self.UI.indexOf(self.Documentation), _translate("MainWindow", "Documentation"))

    def retranslateUiCreate(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("New Project", "New Project"))
        self.projectNameLabel.setText(_translate("Dialog", "Project Name"))
        self.projectDescriptionLabel.setText(_translate("Dialog", "Project Description"))


    def retranslateUiBinaryError(self, binaryFileErrorWindow):
        _translate = QtCore.QCoreApplication.translate
        binaryFileErrorWindow.setWindowTitle(_translate("binaryFileErrorWindow", "Error Message: x86 Architecture Binary File"))
        self.messageLabel.setText(_translate("binaryFileErrorWindow", "The system only supports files that are of x86 architecture."))

    def retranslateUiFileError(self, fileSpecifiedErrorWindow):
        _translate = QtCore.QCoreApplication.translate
        fileSpecifiedErrorWindow.setWindowTitle(_translate("fileSpecifiedErrorWindow", "Error Message: File Specified"))
        self.messageLabel.setText(_translate("fileSpecifiedErrorWindow", "A project is associated with one binary file and cannot be "))
        self.messageLabel_2.setText(_translate("fileSpecifiedErrorWindow", "saved without a binary file. Please provide a binary file."))

    def retranslateAnalysisResultView(self, analysisResultView):
        _translate = QtCore.QCoreApplication.translate
        analysisResultView.setWindowTitle(_translate("analysisResultView", "Analysis Result View"))
        self.deleteAnalysisButton.setText(_translate("analysisResultView", "- Delete"))
        self.saveAnalysisButton.setText(_translate("analysisResultView", "+ Save"))
        self.newAnalysisButton.setText(_translate("analysisResultView", "New"))
        self.analysisViewGroup.setTitle(_translate("analysisResultView", "Analysis Result Area"))
        self.nameAnalysisLabel.setText(_translate("analysisResultView", "Name"))
        self.descriptionAnalysisLabel.setText(_translate("analysisResultView", "Description"))
        self.analysisSearch.setHtml(_translate("analysisResultView",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-style:italic; color:#7e7e7e;\">Analysis Search</span></p></body></html>"))
        self.analysisSearchButton.setText(_translate("analysisResultView", "🔍 "))

    def retranslateOutputFieldView(self, OutputFieldView):
        _translate = QtCore.QCoreApplication.translate
        OutputFieldView.setWindowTitle(_translate("OutputFieldView", "Output Field View"))
        self.generateOutputButton.setText(_translate("OutputFieldView", "Generate"))
        self.browseOutputButton.setText(_translate("OutputFieldView", "Browse"))
        self.descriptionOutputLabel.setText(_translate("OutputFieldView", "Description"))
        self.nameOutputLabel.setText(_translate("OutputFieldView", "Name"))
        self.locationOutputLabel.setText(_translate("OutputFieldView", "Location"))

    def retranslateCommentView(self, commentView):
        _translate = QtCore.QCoreApplication.translate
        commentView.setWindowTitle(_translate("commentView", "Comment View"))
        self.clearButton.setText(_translate("commentView", "Clear"))
        self.saveCommentButton.setText(_translate("commentView", "+Save"))

    def retranslatePluginError(self, pluginSelected):
        _translate = QtCore.QCoreApplication.translate
        pluginSelected.setWindowTitle(_translate("pluginSelected", "Error Message: Plugin Selected"))
        self.messageLabel.setText(_translate("pluginSelected", "You need to select a plugin before running an analysis."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiMain(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
