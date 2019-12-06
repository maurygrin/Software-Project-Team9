import r2pipe

from PyQt5 import QtCore, QtWidgets

from ProjectSub.Project import Project
from ProjectSub.BinaryFile import BinaryFile
from ProjectSub.Metadata import Metadata

class ProjectController(object):

    def __init__(self, project_tab, analysis_tab, analysisController, db):
        self.project_tab = project_tab
        self.analysis_tab = analysis_tab
        self.project_tab.projectNewButton.clicked.connect(self.projectWindow)
        self.project_tab.projectDeleteButton.clicked.connect(self.deleteConfirmation)
        self.project_tab.saveProjectButton.setEnabled(False)
        self.project_tab.projectList.clicked.connect(self.projectClicked)

        self.project_tab.fileProperties.append("Name\t\t\tValue\n")

        self.project_tab.projectNameField.setEnabled(False)
        self.project_tab.projectDescriptionField.setEnabled(False)
        self.project_tab.binaryFilePathField.setEnabled(False)
        self.project_tab.projectDeleteButton.setEnabled(False)

        self.project_tab.projectSearch.textChanged[str].connect(self.filter_projects)

        self.db = db

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

        self.analysisController = analysisController

        self.db.findProjects(self.project_tab)


    def projectWindow(self):
        self.project_tab.setupUiCreateProject(self.project_tab.windowNew)
        self.project_tab.windowNew.show()
        self.project_tab.binaryFilePathEdit.setEnabled(False)

        self.project_tab.binaryFilePathBrowse.clicked.connect(self.getBinaryFilePath)
        self.project_tab.buttonBox.accepted.connect(
            lambda: self.createProject(self.project_tab.projectNameEdit.toPlainText(), self.project_tab.binaryFilePathEdit.toPlainText(),
                                       self.project_tab.projectDescriptionEdit.toPlainText())
        )

    def deleteConfirmation(self):
        self.project_tab.setupUiDeleteProjectConfirmation(self.project_tab.windowDeleteConfirmation)
        self.project_tab.windowDeleteConfirmation.show()
        self.project_tab.buttonBox.accepted.connect(
            lambda: self.deleteProject()
        )

    def binaryErrorWindow(self):
        self.project_tab.setupUiBinaryError(self.project_tab.windowBinaryError)
        self.project_tab.windowBinaryError.show()

    def fileErrorWindow(self):
        self.project_tab.setupUiInvalidField(self.project_tab.windowFileError)
        self.project_tab.windowFileError.show()

    def createProject(self, name, binary, description):
        if not name or not binary or not description:
            self.fileErrorWindow()
        else:
            self.project = Project(name, binary, description)

            self.project_tab.projectNameField.setText(self.project.name)
            self.project_tab.binaryFilePathField.setText(self.project.binary)
            self.project_tab.projectDescriptionField.setText(self.project.description)

            self.r2 = r2pipe.open(self.path)

            self.analysisController.set_r2(self.r2)

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

            self.project_tab.binaryFilePathEdit.setText(self.path)
            self.project_tab.fileProperties.append("arch\t\t\t" + self.binary.metadata.arch + "\n")
            self.project_tab.fileProperties.append("os\t\t\t" + self.binary.metadata.os + "\n")
            self.project_tab.fileProperties.append("bintype\t\t\t" + self.binary.metadata.binaryType + "\n")
            self.project_tab.fileProperties.append("machine\t\t\t" + self.binary.metadata.machine + "\n")
            self.project_tab.fileProperties.append("class\t\t\t" + self.binary.metadata.classVariable + "\n")
            self.project_tab.fileProperties.append("bits\t\t\t" + str(self.binary.metadata.bits) + "\n")
            self.project_tab.fileProperties.append("language\t\t\t" + self.binary.metadata.language + "\n")
            self.project_tab.fileProperties.append("canary\t\t\t" + str(self.binary.metadata.canary) + "\n")
            self.project_tab.fileProperties.append("endian\t\t\t" + self.binary.metadata.endian + "\n")
            self.project_tab.fileProperties.append("crypto\t\t\t" + str(self.binary.metadata.crypto) + "\n")
            self.project_tab.fileProperties.append("nx\t\t\t" + str(self.binary.metadata.nx) + "\n")
            self.project_tab.fileProperties.append("pic\t\t\t" + str(self.binary.metadata.pic) + "\n")
            self.project_tab.fileProperties.append("relocs\t\t\t" + str(self.binary.metadata.relocs) + "\n")
            self.project_tab.fileProperties.append("stripped\t\t\t" + str(self.binary.metadata.stripped) + "\n")
            self.project_tab.fileProperties.append("extension\t\t\t" + self.binary.metadata.type + "\n")

            self.project_tab.binaryFilePathField.setText(self.path)
            self.saveProject()

    def deleteProject(self):
        self.project_tab.projectDeleteButton.setEnabled(False)

        p = self.db.findProject("Project Name", self.project_tab.projectList.currentItem().text())

        self.db.deleteProject(p)

        self.project_tab.projectList.takeItem(self.project_tab.projectList.currentRow())
        self.project_tab.projectNameField.clear()
        self.project_tab.projectDescriptionField.clear()
        self.project_tab.binaryFilePathField.clear()
        self.project_tab.fileProperties.clear()
        self.project_tab.projectNameField.repaint()
        self.project_tab.projectDescriptionField.repaint()
        self.project_tab.binaryFilePathField.repaint()
        self.project_tab.fileProperties.repaint()
        self.r2 = ""
        self.project_tab.projectList.clearSelection()
        #self.projectTabName = "Project"
        #self.analysisTabName = "Analysis"
        #self.retranslateUi(MainWindow)

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


        self.db.insertProject(project)

        it = QtWidgets.QListWidgetItem(self.project.name)

        self.project_tab.projectList.addItem(it)

        it.setSelected(True)

        self.project_tab.projectDescriptionField.setEnabled(True)

        self.project_tab.projectDeleteButton.setEnabled(True)

        #self.projectTabName = "Project - " + self.project.name
        #self.analysisTabName = "Analysis - " + self.project.name

        #self.retranslateUi(MainWindow)

    def getBinaryFilePath(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.project_tab.binaryFilePathField, "Browse Binary File", "",
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
                    self.project_tab.fileProperties.setText("")
                    self.path = ""
                    self.project_tab.binaryFilePathEdit.setText("")
                    self.r2 = ""
                    self.binaryInfo = ""

                else:
                    self.project_tab.binaryFilePathEdit.setText(fileName)

            except Exception as e:
                self.binaryErrorWindow()
                self.r2 = ""
                self.project_tab.fileProperties.setText("")
                self.path = ""
                self.project_tab.binaryFilePathEdit.setText("")
                self.r2 = ""
                self.binaryInfo = ""

    def projectClicked(self):
        p = self.db.findProject("Project Name", self.project_tab.projectList.currentItem().text())

        self.project_tab.fileProperties.clear()
        self.project_tab.projectNameField.setText(p.get("Project Name"))

        self.project_tab.projectDescriptionField.setText(p.get("Project Description"))

        self.project_tab.binaryFilePathField.setText(p.get("Binary File Path"))

        self.project_tab.fileProperties.append("arch\t\t\t" + p.get("arch") + "\n")
        self.project_tab.fileProperties.append("os\t\t\t" + p.get("os") + "\n")
        self.project_tab.fileProperties.append("bintype\t\t\t" + p.get("bintype") + "\n")
        self.project_tab.fileProperties.append("machine\t\t\t" + p.get("machine") + "\n")
        self.project_tab.fileProperties.append("class\t\t\t" + p.get("class") + "\n")
        self.project_tab.fileProperties.append("bits\t\t\t" + str(p.get("bits")) + "\n")
        self.project_tab.fileProperties.append("language\t\t\t" + p.get("language") + "\n")
        self.project_tab.fileProperties.append("canary\t\t\t" + str(p.get("canary")) + "\n")
        self.project_tab.fileProperties.append("endian\t\t\t" + p.get("endian") + "\n")
        self.project_tab.fileProperties.append("crypto\t\t\t" + str(p.get("crypto")) + "\n")
        self.project_tab.fileProperties.append("nx\t\t\t" + str(p.get("nx")) + "\n")
        self.project_tab.fileProperties.append("pic\t\t\t" + str(p.get("pic")) + "\n")
        self.project_tab.fileProperties.append("relocs\t\t\t" + str(p.get("relocs")) + "\n")
        self.project_tab.fileProperties.append("stripped\t\t\t" + str(p.get("stripped")) + "\n")
        self.project_tab.fileProperties.append("extension\t\t\t" + p.get("extension") + "\n")

        self.r2 = r2pipe.open(p.get("Binary File Path"))

        self.analysisController.set_r2(self.r2)

        self.analysis_tab.detailedPoiAnalysisField.clear()

        self.project_tab.projectDescriptionField.setEnabled(True)

        self.project_tab.projectDeleteButton.setEnabled(True)

        #self.projectTabName = "Project - " + self.projectList.currentItem().text()
        #self.analysisTabName = "Analysis - " + self.projectList.currentItem().text()
        #self.retranslateUi(MainWindow)

    def filter_projects(self):  ##filtering list of project
        for item in self.project_tab.projectList.findItems("*", QtCore.Qt.MatchWildcard):
            item.setHidden(True)
        for item in self.project_tab.projectList.findItems(self.project_tab.projectSearch.text(), QtCore.Qt.MatchStartsWith):
            item.setHidden(False)