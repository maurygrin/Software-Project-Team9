# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import self as self
from PyQt5 import QtCore, QtGui, QtWidgets
from savePM import Ui_confirmationWindow
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_confirmationWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1318, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1281, 721))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 261, 681))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 620, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget_3.setGeometry(QtCore.QRect(10, 80, 231, 521))
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        item.setFont(font)
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        self.poiSearch_4 = QtWidgets.QTextEdit(self.groupBox)
        self.poiSearch_4.setGeometry(QtCore.QRect(10, 30, 231, 31))
        self.poiSearch_4.setObjectName("poiSearch_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 10, 951, 681))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 131, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 650, 421, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(840, 140, 99, 25))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(170, 140, 671, 21))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(170, 60, 671, 71))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(170, 30, 671, 21))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 620, 113, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea.setGeometry(QtCore.QRect(170, 170, 671, 441))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
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
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setGeometry(QtCore.QRect(110, 0, 16, 471))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_10.setGeometry(QtCore.QRect(0, 0, 121, 441))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser_11.setGeometry(QtCore.QRect(120, 0, 531, 441))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_19.setGeometry(QtCore.QRect(830, 620, 113, 32))
        self.pushButton_19.setObjectName("pushButton_19")

        self.pushButton_19.clicked.connect(self.openWindow)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(310, 120, 911, 571))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 420, 841, 131))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 40, 841, 361))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_16.setGeometry(QtCore.QRect(870, 40, 32, 30))
        self.pushButton_16.setObjectName("pushButton_16")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 120, 261, 571))
        self.groupBox_4.setObjectName("groupBox_4")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox.setGeometry(QtCore.QRect(10, 50, 141, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 80, 141, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 110, 141, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(240, 20, 41, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(190, 50, 91, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(150, 90, 131, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(590, 50, 111, 16))
        self.label_9.setObjectName("label_9")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(290, 10, 131, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.runButtonStatic = QtWidgets.QPushButton(self.tab_2)
        self.runButtonStatic.setGeometry(QtCore.QRect(290, 50, 113, 32))
        self.runButtonStatic.setObjectName("runButtonStatic")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(290, 90, 121, 32))
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.runButtonDynamic = QtWidgets.QPushButton(self.tab_2)
        self.runButtonDynamic.setGeometry(QtCore.QRect(710, 50, 113, 32))
        self.runButtonDynamic.setObjectName("runButtonDynamic")
        self.stopButton = QtWidgets.QPushButton(self.tab_2)
        self.stopButton.setGeometry(QtCore.QRect(830, 50, 113, 32))
        self.stopButton.setObjectName("stopButton")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_18.setGeometry(QtCore.QRect(1230, 160, 32, 30))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_20 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_20.setGeometry(QtCore.QRect(1230, 130, 32, 30))
        self.pushButton_20.setObjectName("pushButton_20")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 10, 261, 681))
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_10.setGeometry(QtCore.QRect(140, 620, 113, 32))
        self.pushButton_10.setObjectName("pushButton_10")
        self.poiSearch_2 = QtWidgets.QTextEdit(self.groupBox_5)
        self.poiSearch_2.setGeometry(QtCore.QRect(10, 30, 231, 31))
        self.poiSearch_2.setObjectName("poiSearch_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_5)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 80, 231, 521))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        item.setFont(font)
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_6.setGeometry(QtCore.QRect(310, 10, 951, 681))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_10 = QtWidgets.QLabel(self.groupBox_6)
        self.label_10.setGeometry(QtCore.QRect(30, 30, 101, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_6)
        self.label_11.setGeometry(QtCore.QRect(30, 60, 171, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_6)
        self.label_12.setGeometry(QtCore.QRect(30, 90, 101, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_6)
        self.label_13.setGeometry(QtCore.QRect(30, 120, 111, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_6)
        self.label_14.setGeometry(QtCore.QRect(30, 220, 121, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_6)
        self.label_15.setGeometry(QtCore.QRect(30, 250, 111, 16))
        self.label_15.setObjectName("label_15")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_4.setGeometry(QtCore.QRect(200, 60, 641, 21))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_5.setGeometry(QtCore.QRect(200, 30, 641, 21))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_6.setGeometry(QtCore.QRect(200, 90, 641, 21))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_7.setGeometry(QtCore.QRect(200, 120, 641, 21))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_8.setGeometry(QtCore.QRect(200, 250, 641, 211))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_3.setGeometry(QtCore.QRect(200, 210, 121, 32))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_9.setGeometry(QtCore.QRect(840, 30, 99, 25))
        self.pushButton_9.setObjectName("pushButton_9")


        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 620, 113, 32))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_12.setGeometry(QtCore.QRect(830, 620, 113, 32))
        self.pushButton_12.setObjectName("pushButton_12")

        self.pushButton_12.clicked.connect(self.openWindow)

        self.pushButton_8 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_8.setGeometry(QtCore.QRect(1150, 70, 99, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_7.setGeometry(QtCore.QRect(20, 10, 261, 681))
        self.groupBox_7.setObjectName("groupBox_7")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_13.setGeometry(QtCore.QRect(140, 620, 113, 32))
        self.pushButton_13.setObjectName("pushButton_13")
        self.poiSearch = QtWidgets.QTextEdit(self.groupBox_7)
        self.poiSearch.setGeometry(QtCore.QRect(10, 30, 231, 31))
        self.poiSearch.setObjectName("poiSearch")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_7)
        self.listWidget.setGeometry(QtCore.QRect(10, 80, 231, 521))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_8.setGeometry(QtCore.QRect(310, 10, 951, 681))
        self.groupBox_8.setObjectName("groupBox_8")
        self.label_16 = QtWidgets.QLabel(self.groupBox_8)
        self.label_16.setGeometry(QtCore.QRect(120, 30, 41, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_8)
        self.label_17.setGeometry(QtCore.QRect(30, 60, 131, 16))
        self.label_17.setObjectName("label_17")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_15.setGeometry(QtCore.QRect(830, 620, 113, 32))
        self.pushButton_15.setObjectName("pushButton_15")

        self.pushButton_15.clicked.connect(self.openWindow)

        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox_4.setGeometry(QtCore.QRect(170, 20, 131, 32))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox_5.setGeometry(QtCore.QRect(170, 50, 121, 32))
        self.comboBox_5.setEditable(False)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.textEdit_4 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 90, 911, 511))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_14.setGeometry(QtCore.QRect(330, 630, 113, 32))
        self.pushButton_14.setObjectName("pushButton_14")
        self.tabWidget.addTab(self.tab_4, "")
        self.Documentation = QtWidgets.QWidget()
        self.Documentation.setObjectName("Documentation")
        self.groupBox_9 = QtWidgets.QGroupBox(self.Documentation)
        self.groupBox_9.setGeometry(QtCore.QRect(310, 10, 951, 681))
        self.groupBox_9.setObjectName("groupBox_9")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_9)
        self.textEdit.setGeometry(QtCore.QRect(20, 30, 911, 631))
        self.textEdit.setObjectName("textEdit")
        self.groupBox_10 = QtWidgets.QGroupBox(self.Documentation)
        self.groupBox_10.setGeometry(QtCore.QRect(20, 10, 261, 681))
        self.groupBox_10.setObjectName("groupBox_10")
        self.poiSearch_3 = QtWidgets.QTextEdit(self.groupBox_10)
        self.poiSearch_3.setGeometry(QtCore.QRect(10, 40, 231, 31))
        self.poiSearch_3.setObjectName("poiSearch_3")
        self.listWidget_4 = QtWidgets.QListWidget(self.groupBox_10)
        self.listWidget_4.setGeometry(QtCore.QRect(10, 80, 231, 521))
        self.listWidget_4.setObjectName("listWidget_4")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        item.setFont(font)
        self.listWidget_4.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_4.addItem(item)
        self.tabWidget.addTab(self.Documentation, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BEAT: Binary Extraction and Analysis Tool"))
        self.groupBox.setTitle(_translate("MainWindow", "Project View"))
        self.pushButton_2.setText(_translate("MainWindow", "New"))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        item = self.listWidget_3.item(0)
        item.setText(_translate("MainWindow", "Project A"))
        item = self.listWidget_3.item(1)
        item.setText(_translate("MainWindow", "Project B"))
        item = self.listWidget_3.item(2)
        item.setText(_translate("MainWindow", "Project C"))
        item = self.listWidget_3.item(3)
        item.setText(_translate("MainWindow", "Project D"))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        self.poiSearch_4.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-style:italic; color:#7e7e7e;\">Project Search </span><span style=\" font-family:\'Roboto,arial,sans-serif\'; font-size:12pt; color:#222222; background-color:#ffffff;\">🔍</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-style:italic; color:#7e7e7e;\"> </span></p></body></html>"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Detailed Project View"))
        self.label.setText(_translate("MainWindow", "Project Name"))
        self.label_2.setText(_translate("MainWindow", "Project Description"))
        self.label_3.setText(_translate("MainWindow", "Binary File Path"))
        self.label_4.setText(_translate("MainWindow", "Binary File Properties"))
        self.label_5.setText(
            _translate("MainWindow", "** User cannot modify the binary file path once the project is created."))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt;\">C:\\Users\\Documents\\BEAT\\ProjectA</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\">Reduces the amount of time required to perform binary analysis and performs a more targeted binary analysis.</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\">Project A</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete"))
        self.textBrowser_10.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:600;\">Name</span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:600;\"><br /></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">OS</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Binary Type</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Machine</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Class Bits</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Language</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Canary</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Nx</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Pic</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Relocs</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Relro</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Stripped</span></p></body></html>"))
        self.textBrowser_11.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:600;\">Value</span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:600;\"><br /></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">CentOS</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Binary(n)</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Linux</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">MACH064</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Python 3</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">True</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">False</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">True</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">False</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">Full</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">False</span></p></body></html>"))
        self.pushButton_19.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Project"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Detailed Point of Interest View"))
        self.lineEdit_2.setText(_translate("MainWindow", "$ "))
        self.textEdit_3.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">    </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#00557f;\">main:</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#aa0000;\">(fcn) sym.main 133</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#00557f;\">    ; DATA XREF from 0x0040080d (entry0)</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#00557f;\">    0x0040095a    55    push rbp</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#00557f;\">    0x0040095b    4889e5    mov rbp, rsp</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#00557f;\">    0x0040095c    4881ec200100    sub rsp, 0x120</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#00557f;\">    0x0040095d    89bdfcfefff    mov dword</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#00557f;\">    0x0040095e    b800000000    mov qword</span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#00557f;\"><br /></p></body></html>"))
        self.pushButton_16.setText(_translate("MainWindow", "C"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Point of Interest View"))
        self.checkBox.setText(_translate("MainWindow", "Point of Interest A"))
        self.checkBox_2.setText(_translate("MainWindow", "Point of Interest B"))
        self.checkBox_3.setText(_translate("MainWindow", "Point of Interest C"))
        self.label_6.setText(_translate("MainWindow", "Plugin"))
        self.label_7.setText(_translate("MainWindow", "Static Analysis"))
        self.label_8.setText(_translate("MainWindow", "Point of Interest Type"))
        self.label_9.setText(_translate("MainWindow", "Dynamic Analysis"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Existing Plugin"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Network"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Security"))
        self.runButtonStatic.setText(_translate("MainWindow", "Run"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Type"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Function Calls"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Variable Names"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Dll"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Data Structures"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Strings"))
        self.runButtonDynamic.setText(_translate("MainWindow", "Run"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.pushButton_18.setText(_translate("MainWindow", "O"))
        self.pushButton_20.setText(_translate("MainWindow", "A"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Analysis"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Plugin View"))
        self.pushButton_10.setText(_translate("MainWindow", "New"))
        self.poiSearch_2.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-style:italic; color:#7e7e7e;\">Plugin 🔍 </span></p></body></html>"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("MainWindow", "Plugin A"))
        item = self.listWidget_2.item(1)
        item.setText(_translate("MainWindow", "Plugin B"))
        item = self.listWidget_2.item(2)
        item.setText(_translate("MainWindow", "Plugin C"))
        item = self.listWidget_2.item(3)
        item.setText(_translate("MainWindow", "Plugin D"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.groupBox_6.setTitle(_translate("MainWindow", "Detailed Plugin View"))
        self.label_10.setText(_translate("MainWindow", "Plugin Structure"))
        self.label_11.setText(_translate("MainWindow", "Plugin Predefined Data Set"))
        self.label_12.setText(_translate("MainWindow", "Plugin Name"))
        self.label_13.setText(_translate("MainWindow", "Plugin Description"))
        self.label_14.setText(_translate("MainWindow", "Default Output Field"))
        self.label_15.setText(_translate("MainWindow", "Points of Interest"))
        self.textBrowser_4.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt;\">C:\\Users\\Documents\\BEAT\\Plugins\\Security\\DataSet</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt;\">C:\\Users\\Documents\\BEAT\\Plugins\\Security</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt;\">Security Plugin</span></p>\n"
                                              "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:9.75pt;\"><br /></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9.75pt;\">Plugin that finds and analyzes points of interest that are to do with security protocols only.</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">&lt;xs:element name=&quot;</span><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#ff0000;\">SecuritySuitabilityPolicy</span><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">&quot;</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">        type=&quot;dssc:SecuritySuitabilityPolicyType&quot;/&gt;</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">   &lt;xs:complexType name=&quot;</span><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#ff0000;\">SecuritySuitabilityPolicyType</span><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">&quot;&gt;</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">     &lt;xs:sequence&gt;</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">       &lt;xs:element ref=&quot;dssc:PolicyName&quot;/&gt;</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">       &lt;xs:element ref=&quot;dssc:Publisher&quot;/&gt;</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">       &lt;xs:element name=&quot;PolicyIssueDate&quot; type=&quot;xs:dateTime&quot;/&gt;</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">       &lt;xs:element name=&quot;</span><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#ff0000;\">NextUpdate</span><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">&quot; type=&quot;xs:dateTime&quot; minOccurs=&quot;0&quot;/&gt;</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">       &lt;xs:element name=&quot;Usage&quot; type=&quot;xs:string&quot; minOccurs=&quot;0&quot;/&gt;</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">       &lt;xs:element ref=&quot;</span><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#ff0000;\">dssc:Algorithm</span><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">&quot; maxOccurs=&quot;unbounded&quot;/&gt;</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">       &lt;xs:element ref=&quot;ds:Signature&quot; minOccurs=&quot;0&quot;/&gt;</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">     &lt;/xs:sequence&gt;</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">     &lt;xs:attribute name=&quot;version&quot; type=&quot;xs:string&quot; default=&quot;1&quot;/&gt;</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">     &lt;xs:attribute name=&quot;lang&quot; default=&quot;en&quot;/&gt;</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">     &lt;xs:attribute name=&quot;</span><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#ff0000;\">id</span><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">&quot; type=&quot;xs:ID&quot;/&gt;</span></p>\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:10pt; color:#000000;\">   &lt;/xs:complexType&gt;</span></p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Output Field"))
        self.pushButton_9.setText(_translate("MainWindow", "Browse"))
        self.pushButton_11.setText(_translate("MainWindow", "Delete"))
        self.pushButton_12.setText(_translate("MainWindow", "Save"))
        self.pushButton_8.setText(_translate("MainWindow", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Plugin Management"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Point of Interest View"))
        self.pushButton_13.setText(_translate("MainWindow", "New"))
        self.poiSearch.setHtml(_translate("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-style:italic; color:#7e7e7e;\">Point of Interest Search </span><span style=\" font-family:\'Roboto,arial,sans-serif\'; font-size:12pt; color:#222222; background-color:#ffffff;\">🔍</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-style:italic; color:#7e7e7e;\"> </span></p></body></html>"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Point of Interest A"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Point of Interest B"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Point of Interest C"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Point of Interest D"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_8.setTitle(_translate("MainWindow", "Detailed Point of Interest View"))
        self.label_16.setText(_translate("MainWindow", "Plugin"))
        self.label_17.setText(_translate("MainWindow", "Point of Interest Type"))
        self.pushButton_15.setText(_translate("MainWindow", "Save"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Existing Plugin"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Network"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Security"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Type"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Function Calls"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Variable Names"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "Dll"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "Data Structures"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "Strings"))
        self.textEdit_4.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">    </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#00557f;\">main:</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#aa0000;\">(fcn) sym.main 133</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#00557f;\">    ; DATA XREF from 0x0040080d (entry0)</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#00557f;\">    0x0040095a    55    push rbp</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#00557f;\">    0x0040095b    4889e5    mov rbp, rsp</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#00557f;\">    0x0040095c    4881ec200100    sub rsp, 0x120</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#00557f;\">    0x0040095d    89bdfcfefff    mov dword</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#00557f;\">    0x0040095e    b800000000    mov qword</span></p>\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; color:#00557f;\"><br /></p></body></html>"))
        self.pushButton_14.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Points of Interest"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Detailed Documentation View"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The purpose of the Software Requirements Specification (SRS) is to give the customer a clear and precise description of the functionality of the Behavior Extraction and Analysis Tool (BEAT). The SRS divides the system requirements into two parts, behavioral and non-behavioral requirements. The behavioral requirements describe the interaction between the system and its environment. Non-behavioral requirements relate to the definition of the attributes of the product as it performs its functions. This includes performance requirements of the product. The intended audience of the SRS is Dr. Jaime Acosta, Dr. Oscar Perez, Mr. Vincent Fonseca, Ms. Herandy Vazquez, Mr. Baltazar Santaella, Ms. Florencia Larsen, Mr. Juan Ulloa, Mr. Jesus Martinez, and the Software Engineering teams. This document serves as an agreement between both parties regarding the product to be developed. </p></body></html>"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Documentation View"))
        self.poiSearch_3.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-style:italic; color:#7e7e7e;\">Document </span><span style=\" font-family:\'Roboto,arial,sans-serif\'; font-size:12pt; color:#222222; background-color:#ffffff;\">🔍</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-style:italic; color:#7e7e7e;\"> </span></p></body></html>"))
        __sortingEnabled = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        item = self.listWidget_4.item(0)
        item.setText(_translate("MainWindow", "BEAT Documentation"))
        item = self.listWidget_4.item(1)
        item.setText(_translate("MainWindow", "Plugin Structure"))
        self.listWidget_4.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Documentation), _translate("MainWindow", "Documentation"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
