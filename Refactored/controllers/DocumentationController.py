from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

from controllers.DBController import DBController

class DocumentationController(object):

    def __init__(self, documentation_tab, db, plugin_tab):
        self.documentation_tab = documentation_tab
        self.db = db
        self.plugin_tab = plugin_tab
        self.documentation_tab.documentList.clicked.connect(self.documentationClicked)
        self.documentation_tab.documentSearch.textChanged[str].connect(self.filter_doc)
        self.documentation_tab.restoreDocumentButton.clicked.connect(self.restoreBeatDocumentation)
        self.documentation_tab.saveDocumentButton.clicked.connect(self.saveDocument)

        self.documentationTextChangeTimer = QtCore.QTimer()
        self.documentationTextChangeTimer.setSingleShot(True)
        self.documentationTextChangeTimer.timeout.connect(self.saveDocument)

        query_result = self.db.findDocument("file_name", "BEAT Documentation")

        if query_result is not None:
            self.documentation_tab.documentList.addItem(query_result["file_name"])
        else:
            text_file_doc = {"file_name": "BEAT Documentation", "contents": ""}
            self.db.insertDocument(text_file_doc)
            self.documentation_tab.documentList.addItem(text_file_doc["file_name"])
        self.documentation_tab.documentList.addItem("Plugin Structure")
        self.hidePluginStructure(False)

    def documentationClicked(self):
        currentDocument = self.documentation_tab.documentList.currentItem().text()
        print(self.documentation_tab.documentList.currentItem().text())
        if currentDocument == "BEAT Documentation":
            self.documentation_tab.documentViewField.setReadOnly(False)
            self.documentation_tab.saveDocumentButton.setEnabled(True)
            self.documentation_tab.restoreDocumentButton.setEnabled(True)
            query_result = self.db.findDocument("file_name", currentDocument)
            if query_result is not None:
                self.documentation_tab.documentViewField.setText(query_result["contents"])
            else:
                text_file_doc = {"file_name": currentDocument, "contents": ""}
                self.db.insertDocument(text_file_doc)
        elif currentDocument == "Plugin Structure":
            self.loadPluginStructureDocumentation()

    def restoreBeatDocumentation(self):
        currentDocument = self.documentation_tab.documentList.currentItem().text()
        print(self.documentation_tab.documentList.currentItem().text())
        if currentDocument == "BEAT Documentation":
            default_beat_documentation_path = "BEATDocumentationDefault.txt"
            try:
                with open(default_beat_documentation_path, 'r') as default_beat_documentation:
                    content = default_beat_documentation.read()
                text_file_doc = {"file_name": currentDocument, "contents": content}
                # insert the contents into the "file" collection
                if self.db.countDocuments("file_name", currentDocument) > 0:
                    self.db.replaceDocument("file_name", currentDocument, text_file_doc)
                else:
                    self.db.insertDocument("file_name", currentDocument, text_file_doc)
                self.documentation_tab.documentViewField.setText(content)
            except FileNotFoundError:
                print("Could Not Restore BEAT Documentation, BEATDocumentationDefault.txt file not found")

    def saveDocument(self):
        if self.documentation_tab.documentList.currentItem() is None:
            return
        currentDocument = self.documentation_tab.documentList.currentItem().text()
        if currentDocument == "Plugin Structure":
            return
        documentContent = self.documentation_tab.documentViewField.toPlainText()
        # build a document to be inserted
        text_file_doc = {"file_name": currentDocument, "contents": documentContent}
        # insert the contents into the "file" collection
        if self.db.countDocuments("file_name", currentDocument) > 0:
            self.db.replaceDocument("file_name", currentDocument, text_file_doc)
        else:
            self.db.insertDocument("file_name", currentDocument, text_file_doc)

    def handleDocumentationEdit(self):
        self.documentationTextChangeTimer.start(7500)
        pass

    def hidePluginStructure(self, hidden):
        items = self.documentation_tab.documentList.findItems("Plugin Structure", QtCore.Qt.MatchExactly)
        if len(items) > 0:
            for item in items:
                item.setHidden(hidden)

    def loadPluginStructureDocumentation(self):
        self.documentation_tab.documentViewField.setReadOnly(True)
        self.documentation_tab.saveDocumentButton.setEnabled(False)
        self.documentation_tab.restoreDocumentButton.setEnabled(False)
        currentPlugin = self.plugin_tab.pluginManagementList.currentItem()
        if currentPlugin is not None:
            query_result = self.db.findPlugin("Plugin Name", currentPlugin.text())
            if query_result is not None:
                pluginXsdPath = query_result["Structure File Path"]
                try:
                    with open(pluginXsdPath, 'r') as pluginXsd:
                        content = pluginXsd.read()
                    self.documentation_tab.documentViewField.setText(content)
                except FileNotFoundError as err:
                    self.documentation_tab.documentViewField.setText("Structure File Path Not Found")
            else:
                self.documentation_tab.documentViewField.setText("Plugin Not Found")
        else:
            self.documentation_tab.documentViewField.setText("No Plugin Selected")

    def filter_doc(self):
        for item in self.documentation_tab.documentList.findItems("*", QtCore.Qt.MatchWildcard):
            item.setHidden(True)
        for item in self.documentation_tab.documentList.findItems(self.documentation_tab.documentSearch.text(), QtCore.Qt.MatchStartsWith):
            item.setHidden(False)