from PluginSub.POI import POI

from PyQt5 import QtCore

import xml.etree.cElementTree as ET

class POIController(object):

    def __init__(self, poi_tab):
        self.poi_tab = poi_tab
        self.poi_tab.newPOIButton.clicked.connect(self.poiWindow)
        self.poi_tab.poiList.clicked.connect(self.poiClicked)
        self.poi_tab.poiDeleteButton.clicked.connect(self.deletePOI)
        self.poi_tab.poiFilterDropDown.activated.connect(self.dropDownChangePOI)

        self.poi_tab.poiSearch.textChanged[str].connect(self.filter_POI)

        self.list = []
        self.listStrings = []
        self.listFunctions = []

        self.poi_tab.poiDeleteButton.setEnabled(False)
        self.poi_tab.poiSaveButton.setEnabled(False)

    def poiWindow(self):
        self.poi_tab.setupUiPOI(self.poi_tab.windowPOI)
        self.poi_tab.windowPOI.show()

        self.poi_tab.buttonBox.accepted.connect(
            lambda: self.createPOI(self.poi_tab.poiNameEdit.toPlainText(), self.poi_tab.poiTypeEdit.toPlainText(),
                                   self.poi_tab.poiOutEdit.toPlainText()))

    def poiSelectedWindow(self):
        self.poi_tab.setupUiPOISelection(self.poi_tab.windowPOISelected)
        self.poi_tab.windowPOISelected.show()

    def dropDownChangePOI(self):
        dropDownSelect = self.poi_tab.poiFilterDropDown.currentText()

        if (dropDownSelect == "Strings"):
            self.poi_tab.poiList.clear()
            self.poi_tab.poiViewField.clear()
            self.poi_tab.poiViewField.repaint()
            i = 0
            while i < len(self.listStrings):
                self.poi_tab.poiList.addItem(str(self.listStrings[i]))
                i += 3
            self.poi_tab.poiList.repaint()

        elif (dropDownSelect == "Functions"):
            self.poi_tab.poiList.clear()
            self.poi_tab.poiViewField.clear()
            self.poi_tab.poiViewField.repaint()
            i = 0
            while i < len(self.listFunctions):
                self.poi_tab.poiList.addItem(str(self.listFunctions[i]))
                i += 3
            self.poi_tab.poiList.repaint()

        elif (dropDownSelect == "Select"):
            self.poi_tab.poiList.clear()
            self.poi_tab.poiList.repaint()
            self.poi_tab.poiViewField.clear()
            self.poi_tab.poiViewField.repaint()

    def createPOI(self, name, typeP, out):
        if not name or not typeP or not out:
            self.poiSelectedWindow()
        else:
            self.poi = POI(name, typeP, out)
            self.poi_tab.poiNameEdit.setText(self.poi.name)
            self.poi_tab.poiTypeEdit.setText(self.poi.typeP)
            self.poi_tab.poiOutEdit.setText(self.poi.out)

            self.poi_tab.poiViewField.clear()

            tree = ET.parse("./plugins/networkPlugin.xml")

            root = tree.getroot()
            child = ET.Element("item")
            subName = ET.SubElement(child, "nameStrings")
            subType = ET.SubElement(child, "typeStrings")
            subOutput = ET.SubElement(child, "outputString")
            subName.text = self.poi.name
            subType.text = self.poi.typeP
            subOutput.text = self.poi.out

            if typeP == "String":
                self.listStrings.append(name)
                self.listStrings.append(typeP)
                self.listStrings.append(out)

            if typeP == "Function":
                self.listFunctions.append(name)
                self.listFunctions.append(typeP)
                self.listFunctions.append(out)

            self.poi_tab.poiViewField.setText("")
            self.poi_tab.poiViewField.append("\t" + "\n")
            self.poi_tab.poiViewField.append("\t" + "Name: " + name)
            self.poi_tab.poiViewField.append("\t" + "\n")
            self.poi_tab.poiViewField.append("\t" + "Type: " +typeP)
            self.poi_tab.poiViewField.append("\n")
            self.poi_tab.poiViewField.append("\t" + "Output: " + out)
            font = self.poi_tab.poiViewField.font()
            font.setPointSize(12)
            self.poi_tab.poiViewField.setFont(font)
            self.poi_tab.poiViewField.repaint()

            root.append(child)
            tree.write("./plugins/networkPlugin.xml")
            self.poi_tab.poiList.addItem(self.poi.name)
            self.poi_tab.poiList.repaint()

    def deletePOI(self):
        self.poi_tab.poiList.takeItem(self.poi_tab.poiList.currentRow())
        self.poi_tab.poiViewField.clear()
        self.poi_tab.poiViewField.repaint()

    def poiClicked(self):
        select = self.poi_tab.poiList.currentItem().text()
        i = 0
        if self.poi_tab.poiFilterDropDown.currentText() == "Strings":
            while i < len(self.listStrings):
                current = self.listStrings[i]
                print(current)
                if current == select:
                    self.poi_tab.poiViewField.setText("")
                    self.poi_tab.poiViewField.append("\t" + "\n")
                    self.poi_tab.poiViewField.append("\t" + "Name: " + self.listStrings[i])
                    self.poi_tab.poiViewField.append("\t" + "\n")
                    self.poi_tab.poiViewField.append("\t" + "Type: " + self.listStrings[i + 1])
                    self.poi_tab.poiViewField.append("\n")
                    self.poi_tab.poiViewField.append("\t" + "Output: " + self.listStrings[i + 2])
                    font = self.poi_tab.poiViewField.font()
                    font.setPointSize(12)
                    self.poi_tab.poiViewField.setFont(font)
                    self.poi_tab.poiViewField.repaint()
                    break
                i += 3
        elif self.poi_tab.poiFilterDropDown.currentText() == "Functions":
            while i < len(self.listFunctions):
                current = self.listFunctions[i]
                if current == select:
                    self.poi_tab.poiViewField.setText("")
                    self.poi_tab.poiViewField.append("\t" + "\n")
                    self.poi_tab.poiViewField.append("\t" + "Name: " + self.listFunctions[i])
                    self.poi_tab.poiViewField.append("\t" + "\n")
                    self.poi_tab.poiViewField.append("\t" + "Type: " + self.listFunctions[i + 1])
                    self.poi_tab.poiViewField.append("\n")
                    self.poi_tab.poiViewField.append("\t" + "Output: " + self.listFunctions[i + 2])
                    font = self.poi_tab.poiViewField.font()
                    font.setPointSize(12)
                    self.poi_tab.poiViewField.setFont(font)
                    self.poi_tab.poiViewField.repaint()
                    break
                i += 3

    def filter_POI(self):
        for item in self.poi_tab.poiList.findItems("*", QtCore.Qt.MatchWildcard):
            item.setHidden(True)
        for item in self.poi_tab.poiList.findItems(self.poi_tab.poiSearch.text(), QtCore.Qt.MatchStartsWith):
            item.setHidden(False)

    def set_list(self, l):
        self.list = l

    def set_listStrings(self, s):
        self.listStrings = s

    def set_listFunctions(self, f):
        self.listFunctions = f