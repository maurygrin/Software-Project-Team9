from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from views.ProjectTab import ProjectTab
from views.AnalysisTab import AnalysisTab
from views.PluginTab import PluginTab
from views.POITab import POITab
from views.DocumentationTab import DocumentationTab

from controllers.ProjectController import ProjectController
from controllers.AnalysisController import AnalysisController
from controllers.PluginController import PluginController
from controllers.POIController import POIController
from controllers.DocumentationController import DocumentationController


class Ui_MainWindow(object):

    def __init__(self):
        self.windowNew = QtWidgets.QDialog()

    def setupMain(self, MainWindow):

        self.project_tab = ProjectTab()
        self.analysis_tab = AnalysisTab()
        self.plugin_tab = PluginTab()
        self.poi_tab = POITab()
        self.documentation_tab = DocumentationTab()

        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1236, 656)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1236, 656))
        MainWindow.setMaximumSize(QtCore.QSize(1236, 656))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(12, 6, 1221, 638))
        self.tabWidget.setMinimumSize(QtCore.QSize(1221, 638))
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setObjectName("tabWidget")

        self.ProjectTab = QtWidgets.QWidget()
        self.ProjectTab.setObjectName("ProjectTab")
        self.ProjectTab = self.project_tab.setupProjectTab(self.ProjectTab)
        self.tabWidget.addTab(self.ProjectTab, "")

        self.AnalysisTab = QtWidgets.QWidget()
        self.AnalysisTab.setObjectName("AnalysisTab")
        self.AnalysisTab = self.analysis_tab.setupAnalysisTab(self.AnalysisTab)
        self.tabWidget.addTab(self.AnalysisTab, "")


        self.PluginTab = QtWidgets.QWidget()
        self.PluginTab.setObjectName("PluginManagementTab")
        self.PluginTab = self.plugin_tab.setupPluginTab(self.PluginTab)
        self.tabWidget.addTab(self.PluginTab, "")

        self.POITab = QtWidgets.QWidget()
        self.POITab.setObjectName("PointsOfInterestTab")
        self.POITab = self.poi_tab.setupPOITab(self.POITab)
        self.tabWidget.addTab(self.POITab, "")

        self.DocumentationTab = QtWidgets.QWidget()
        self.DocumentationTab.setObjectName("DocumentationTab")
        self.DocumentationTab = self.documentation_tab.setupDocumentationTab(self.DocumentationTab)
        self.tabWidget.addTab(self.DocumentationTab, "")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.project_controller = ProjectController(self.project_tab)
        self.analysis_controller = AnalysisController(self.analysis_tab)
        self.plugin_controller = PluginController(self.plugin_tab)
        self.poi_controller = POIController(self.poi_tab)
        self.documentation_controller = DocumentationController(self.documentation_tab)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Binary Extraction and Analysis Tool"))

        self.project_tab.retranslateProjectTab()
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ProjectTab), _translate("MainWindow", "Project"))

        self.analysis_tab.retranslateAnalysisTab()
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AnalysisTab), _translate("MainWindow", "Analysis"))

        self.plugin_tab.retranslatePluginTab()
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PluginTab), _translate("MainWindow", "Plugin Management"))

        self.poi_tab.retranslatePOITab()
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.POITab), _translate("MainWindow", "Points of Interest"))

        self.documentation_tab.retranslateDocumentationTab()
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DocumentationTab), _translate("MainWindow", "Documentation"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupMain(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())