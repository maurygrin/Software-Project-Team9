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

        self.project = ""
        self.binaryFile = ""

        self.projectName = ""
        self.projectBinary = ""
        self.projectDescription = ""

        self.binaryPath = ""
        self.binaryMetadata = ""
        self.binaryInfo = ""

        self.r2 = ""

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
            lambda: self.createProject(self.project_tab.projectNameEdit.toPlainText(),
                                       self.project_tab.binaryFilePathEdit.toPlainText(),
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

            self.projectName = self.project.get_name()
            self.projectBinary = self.project.get_binary()
            self.projectDescription = self.project.get_description()

            self.project_tab.projectNameField.setText(self.projectName)
            self.project_tab.binaryFilePathField.setText(self.projectBinary)
            self.project_tab.projectDescriptionField.setText(self.projectDescription)

            self.r2 = r2pipe.open(self.path)

            self.analysisController.set_r2(self.r2)

            self.binaryInfo = self.r2.cmdj('ij')

            self.binaryMetadata = Metadata(self.binaryInfo.get("bin").get("arch"), self.binaryInfo.get("bin").get("os"),
                                           self.binaryInfo.get("bin").get("bintype"),
                                           self.binaryInfo.get("bin").get("machine"),
                                           self.binaryInfo.get("bin").get("class"),
                                           str(self.binaryInfo.get("bin").get("bits")),
                                           self.binaryInfo.get("bin").get("lang"),
                                           str(self.binaryInfo.get("bin").get("canary")),
                                           self.binaryInfo.get("bin").get("endian"),
                                           str(self.binaryInfo.get("bin").get("crypto")),
                                           str(self.binaryInfo.get("bin").get("nx")),
                                           str(self.binaryInfo.get("bin").get("pic")),
                                           str(self.binaryInfo.get("bin").get("relocs")),
                                           str(self.binaryInfo.get("bin").get("striped")),
                                           self.binaryInfo.get("core").get("type"))

            self.binaryFile = BinaryFile(binary, self.binaryMetadata)

            self.arch = self.binaryMetadata.get_arch()
            self.os = self.binaryMetadata.get_os()
            self.bintype = self.binaryMetadata.get_binaryType()
            self.machine = self.binaryMetadata.get_machine()
            self.classVar = self.binaryMetadata.get_classVariable()
            self.bits = self.binaryMetadata.get_bits()
            self.language = self.binaryMetadata.get_language()
            self.canary = self.binaryMetadata.get_canary()
            self.endian = self.binaryMetadata.get_endian()
            self.crypto = self.binaryMetadata.get_crypto()
            self.nx = self.binaryMetadata.get_nx()
            self.pic = self.binaryMetadata.get_pic()
            self.relocs = self.binaryMetadata.get_relocs()
            self.stripped = self.binaryMetadata.get_stripped()
            self.extension = self.binaryMetadata.get_type()

            self.project_tab.binaryFilePathEdit.setText(self.path)
            self.project_tab.fileProperties.append("arch\t\t\t" + self.arch + "\n")
            self.project_tab.fileProperties.append("os\t\t\t" + self.os + "\n")
            self.project_tab.fileProperties.append("bintype\t\t\t" + self.bintype + "\n")
            self.project_tab.fileProperties.append("machine\t\t\t" + self.machine + "\n")
            self.project_tab.fileProperties.append("class\t\t\t" + self.classVar + "\n")
            self.project_tab.fileProperties.append("bits\t\t\t" + self.bits + "\n")
            self.project_tab.fileProperties.append("language\t\t\t" + self.language + "\n")
            self.project_tab.fileProperties.append("canary\t\t\t" + self.canary + "\n")
            self.project_tab.fileProperties.append("endian\t\t\t" + self.endian + "\n")
            self.project_tab.fileProperties.append("crypto\t\t\t" + self.crypto + "\n")
            self.project_tab.fileProperties.append("nx\t\t\t" + self.nx + "\n")
            self.project_tab.fileProperties.append("pic\t\t\t" + self.pic + "\n")
            self.project_tab.fileProperties.append("relocs\t\t\t" + self.relocs + "\n")
            self.project_tab.fileProperties.append("stripped\t\t\t" + self.stripped + "\n")
            self.project_tab.fileProperties.append("extension\t\t\t" + self.extension + "\n")

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

    def saveProject(self):
        project = {"Project Name": self.projectName,
                   "Project Description": self.projectDescription,
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

        it = QtWidgets.QListWidgetItem(self.projectName)

        self.project_tab.projectList.addItem(it)

        it.setSelected(True)

        self.project_tab.projectDescriptionField.setEnabled(True)

        self.project_tab.projectDeleteButton.setEnabled(True)


    def getBinaryFilePath(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self.project_tab.binaryFilePathField,
                                                            "Browse Binary File",
                                                            "", "Binary Files (*.exe *.out *.class *.docx)",
                                                            options=options)
        if fileName:
            self.path = str(fileName)
            self.r2 = r2pipe.open(self.path)

            self.binaryInfo = self.r2.cmdj('ij')

            try:
                if (self.binaryInfo.get("bin").get("arch") != "x86") or (
                        self.binaryInfo.get("core").get("type") != "Executable file"
                        and self.binaryInfo.get("core").get("type") != "EXEC (Executable file)"):
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

    def filter_projects(self):  # filtering list of project
        for item in self.project_tab.projectList.findItems("*", QtCore.Qt.MatchWildcard):
            item.setHidden(True)
        for item in self.project_tab.projectList.findItems(self.project_tab.projectSearch.text(),
                                                           QtCore.Qt.MatchStartsWith):
            item.setHidden(False)
