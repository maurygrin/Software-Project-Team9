from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from views.ProjectTab import ProjectTab
from views.AnalysisTab import AnalysisTab
from views.PluginTab import PluginTab
from views.POITab import POITab
from views.DocumentationTab import DocumentationTab

class ProjectController(object):

    def __init__(self, project_tab):
        self.project_tab = project_tab
        self.project_tab.projectNewButton.clicked.connect(self.projectWindow)

    def projectWindow(self):
        self.project_tab.setupUiCreateProject(self.project_tab.windowNew)
        self.project_tab.windowNew.show()
