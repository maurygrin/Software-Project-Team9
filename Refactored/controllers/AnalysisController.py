import os, sys, r2pipe, json, base64, threading

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

staticFunctionList=[]
dictList = []

class AnalysisController(object):

    def __init__(self, analysis_tab):
        self.analysis_tab = analysis_tab
        self.analysis_tab.runStaticButton.clicked.connect(self.runStaticAnalysis)

        self.analysis_tab.runDynamicButton.clicked.connect(self.dynamicAnalysisThread)
        self.analysis_tab.poiAnalysisList.itemSelectionChanged.connect(self.analysisClicked)
        self.analysis_tab.poiTypeDropDownAnalysis.activated.connect(self.displayPOI)

        self.analysis_tab.terminalField.setReadOnly(True)
        self.analysis_tab.runDynamicButton.setEnabled(False)
        self.analysis_tab.stopDynamicButton.setEnabled(False)

        self.static = 0

        self.stringsStatic = ""
        self.vaddr = ""
        self.value = ""
        self.section = ""
        self.function = ""
        self.functionsStatic = ""
        self.temp2 = ""
        self.dynamicRun = False


    def runStaticAnalysis(self):
        if (self.analysis_tab.pluginDropDownAnalysis.currentText() == "Select"):
            self.analysis_tab.setupPluginError(self.windowPluginError)
            self.analysis_tab.windowPluginError.show()
        else:
            self.analysis_tab.runDynamicButton.setEnabled(True)

            self.static = 1

            self.analysis_tab.terminalField.append("Static Analysis Performed!")
            self.analysis_tab.terminalField.append("")
            self.r2.cmd("aaa")
            self.functionsStatic = self.r2.cmdj("afllj")
            self.stringsStatic = self.r2.cmdj("izzj")
            poiSelected = self.analysis_tab.poiTypeDropDownAnalysis.currentText()

            if (poiSelected=="Strings"):
                self.analysis_tab.terminalField.append("Command: izz")
                self.display = "strings"
                self.analysis_tab.detailedPoiAnalysisField.setText("")
                self.analysis_tab.poiAnalysisList.clear()
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Virtual Memory Address: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Value: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Section: ")
                font = self.analysis_tab.detailedPoiAnalysisField.font()
                font.setPointSize(12)
                self.analysis_tab.detailedPoiAnalysisField.setFont(font)
                self.analysis_tab.detailedPoiAnalysisField.repaint()
                for item in self.stringsStatic:
                    item = QtWidgets.QListWidgetItem(item["string"])
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                    item.setCheckState(QtCore.Qt.Checked)
                    self.analysis_tab.poiAnalysisList.addItem(item)
            elif (poiSelected=="Functions"):
                self.analysis_tab.terminalField.append("Command: afl")
                self.display = "functions"
                self.analysis_tab.detailedPoiAnalysisField.setText("")
                self.analysis_tab.poiAnalysisList.clear()
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Virtual Memory Address: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Function: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Parameters: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Parameter Value: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Return Value: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Order num: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\n")
                font = self.analysis_tab.detailedPoiAnalysisField.font()
                font.setPointSize(12)
                self.analysis_tab.detailedPoiAnalysisField.setFont(font)
                self.analysis_tab.detailedPoiAnalysisField.repaint()
                counter = 0
                for item in self.functionsStatic:
                    staticFunctionList.append(item["name"])
                    item = QtWidgets.QListWidgetItem(item["name"])
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                    item.setCheckState(QtCore.Qt.Checked)
                    self.analysis_tab.poiAnalysisList.addItem(item)
                    counter = counter + 1
                self.brianaFunction(staticFunctionList)

    def brianaFunction(self, staticFunctionList):
        keys = ['fName', 'argNum', 'argName', 'argType', 'argVal', 'retName', 'retType', 'retValue', 'locName',
                'locType', 'locNum', 'locVal']
        # will be used to add each function dictionary
        argCounter = 0
        locCounter = 0
        # create a dictionary with keys that correspond to fields needed for the functions
        funD = dict.fromkeys(keys, [])
        self.r2.cmd("aaa")  # initial analysis

        # start analysis process
        for i in range(len(staticFunctionList)):
            funD['fName'] = (staticFunctionList[i])
            funInfo = self.r2.cmd("afvj @ " + staticFunctionList[i])
            formatInfo = json.loads(funInfo)
            for key in formatInfo.keys():
                tempList = formatInfo[key]
                argNames = []
                argTypes = []
                localVarNames = []
                localVarTypes = []

                for j in range(len(tempList)):
                    if tempList[j]['kind'] == 'reg':
                        argCounter += 1
                        funD['argNum'] = argCounter
                        argNames.append(tempList[j]['name'])
                        argTypes.append(tempList[j]['type'])
                        funD['argName'] = argNames
                        funD['argType'] = argTypes
                    if tempList[j]['kind'] == 'var':
                        locCounter += 1
                        funD['locNum'] = locCounter
                        localVarNames.append(tempList[j]['name'])
                        localVarTypes.append(tempList[j]['type'])
                        funD['locName'] = localVarNames
                        funD['locType'] = localVarTypes
            argCounter = 0
            locCounter = 0
            dictList.append(funD)
            sample = open('dictList.txt', 'w')
            print(str(dictList), file=sample)
            sample.close()
            funD = dict.fromkeys(keys, [])

    def stopDynamicAnalysis(self):
        self.r2.cmd("break")

    def dynamicAnalysisThread(self):
        threading.Thread(target=self.runDynamicAnalysis(), args=(10,)).start()
        self.analysis_tab.runStaticButton.setEnabled(False)
        self.dynamicRun = True

    def runDynamicAnalysis(self):
        for i in range(len(dictList)):  # iterate over list of functions
            validFlag = True #is arg num populated flag
            if(dictList[i]['argNum'] == []): #check to see if there is anything populated
                validFlag = False

            validFlag2 = True #is locNum populated flag
            if(dictList[i]['locNum'] == []): # check to see if there is anything populated
                validFlag2 = False


            self.r2.cmd("e dbg.bpinmaps=0")  # disable cannot set breakpoint on unmapped memory
            self.r2.cmd("ood")  # open in debug mode
            self.r2.cmd("aaa")

            if self.analysis_tab.poiAnalysisList.item(i).checkState() !=0:

                breakpointString = "db " + (dictList[i]['fName'])
                self.r2.cmd(breakpointString)  # first set the breakpoint
                self.r2.cmd("dc")  # Run until the first breakpoint
                returnVal = self.r2.cmd("dr rax")
                returnVal = returnVal.rstrip("\n")
                #start running after breakpoint get arguments first
                templistOfVals = []
                templistOfLoc = []
                # for arguments
                if(validFlag):
                    for j in range(dictList[i]['argNum']):
                        # set return value
                        dictList[i]['retVal'] = returnVal
                        commandToVal = self.r2.cmd("afvd " + str(dictList[i]['argName'][j]))
                        if commandToVal != "":
                            commandList = commandToVal.split(" ")
                            validCommand = commandList[0] + "j " + commandList[1] + " " + commandList[2]
                            lineWithval = self.r2.cmd(validCommand)
                            formattedVal = json.loads(lineWithval)
                            templistOfVals.append(formattedVal[0]['value'])
                            dictList[i]['argVal'] = templistOfVals

                # for local variables
                if(validFlag2):
                    for k in range(dictList[i]['locNum']):
                            commandToVal = self.r2.cmd("afvd " + str(dictList[i]['locName'][k]))
                            if commandToVal != "":
                                try:
                                    commandList = commandToVal.split(" ")
                                    validCommand = commandList[0] + "j " + commandList[1] + " " + commandList[2]
                                    lineWithval = self.r2.cmd(validCommand)
                                    formattedVal = json.loads(lineWithval)
                                    templistOfLoc.append(formattedVal[0]['value'])
                                    dictList[i]['locVal'] = templistOfLoc
                                except:
                                    pass

                self.r2.cmd("db-*")
        print(dictList)
        #Display Dynamic results
        poiSelected = self.analysis_tab.poiTypeDropDownAnalysis.currentText()

        if (poiSelected == "Strings"):
            self.analysis_tab.terminalField.append("Command: izz")
            self.display = "strings"
            self.analysis_tab.detailedPoiAnalysisField.setText("")
            self.analysis_tab.poiAnalysisList.clear()
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Virtual Memory Address: ")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Value: ")
            self.analysis_tab.detailedPoiAnalysisField.append("\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Section: ")
            font = self.analysis_tab.detailedPoiAnalysisField.font()
            font.setPointSize(12)
            self.analysis_tab.detailedPoiAnalysisField.setFont(font)
            self.analysis_tab.detailedPoiAnalysisField.repaint()
            for item in self.stringsStatic:
                item = QtWidgets.QListWidgetItem(item["string"])
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Checked)
                self.analysis_tab.poiAnalysisList.addItem(item)
        elif (poiSelected == "Functions"):
            self.analysis_tab.terminalField.append("Command: afll")
            self.display = "functions"
            self.analysis_tab.detailedPoiAnalysisField.setText("")
            self.analysis_tab.poiAnalysisList.clear()
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Virtual Memory Address: ")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Function Name: ")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Arg Name: ")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Arg Number: ")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Arg Type: ")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Arg Value: ")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Return Name: ")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Return Type: ")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Return Value: ")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Local Variable Name: ")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Local Variable Type: ")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Local Variable Number: ")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Local Variable Value: ")
            self.analysis_tab.detailedPoiAnalysisField.append("\n")
            font = self.analysis_tab.detailedPoiAnalysisField.font()
            font.setPointSize(12)
            self.analysis_tab.detailedPoiAnalysisField.setFont(font)
            self.analysis_tab.detailedPoiAnalysisField.repaint()
            for item in self.functionsStatic:
                item = QtWidgets.QListWidgetItem(item["name"])
                item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                item.setCheckState(QtCore.Qt.Checked)
                self.analysis_tab.poiAnalysisList.addItem(item)

    def displayPOI(self):
        if (self.static == 1):

            poiSelected = self.analysis_tab.poiTypeDropDownAnalysis.currentText()

            if (poiSelected == "Functions"):
                self.display = "functions"
                self.analysis_tab.terminalField.append("Command: afll")
                self.analysis_tab.detailedPoiAnalysisField.setText("")
                self.analysis_tab.poiAnalysisList.clear()
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Virtual Memory Address: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Function Name: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Arg Name: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Arg Number: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Arg Type: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Arg Value: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Return Name: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Return Type: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Return Value: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Local Variable Name: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Local Variable Type: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Local Variable Number: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Local Variable Value: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\n")
                font = self.analysis_tab.detailedPoiAnalysisField.font()
                font.setPointSize(12)
                self.analysis_tab.detailedPoiAnalysisField.setFont(font)
                self.analysis_tab.detailedPoiAnalysisField.repaint()
                for item in self.functionsStatic:
                    self.analysis_tab.poiAnalysisList.addItem(item["name"])

            elif (poiSelected == "Strings"):
                self.display = "strings"
                self.analysis_tab.terminalField.append("Command: iz")
                self.analysis_tab.detailedPoiAnalysisField.setText("")
                self.analysis_tab.poiAnalysisList.clear()
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Virtual Memory Address: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Value: ")
                self.analysis_tab.detailedPoiAnalysisField.append("\n")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Section: ")
                font = self.analysis_tab.detailedPoiAnalysisField.font()
#                font.self.analysis_tab.setPointSize(12)
                self.analysis_tab.detailedPoiAnalysisField.setFont(font)
                self.analysis_tab.detailedPoiAnalysisField.repaint()
                for item in self.stringsStatic:
                    self.analysis_tab.poiAnalysisList.addItem(item["string"])

    def analysisClicked(self):
        selected = self.analysis_tab.poiAnalysisList.currentItem().text()
        if self.display is "strings":
            for item in self.stringsStatic:
                current = item["string"]
                if current == selected:
                    self.vaddr = hex(item["vaddr"])
                    self.vaddr = str(self.vaddr)
                    self.value = current
                    self.section = item["section"]
                    break
            self.analysis_tab.detailedPoiAnalysisField.setText("")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Virtual Memory Address: " + self.vaddr)
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Value: " + self.value)
            self.analysis_tab.detailedPoiAnalysisField.append("\n")
            self.analysis_tab.detailedPoiAnalysisField.append("\t" + "Section: " + self.section)
            font = self.analysis_tab.detailedPoiAnalysisField.font()
            font.setPointSize(12)
            self.analysis_tab.detailedPoiAnalysisField.setFont(font)
            self.analysis_tab.detailedPoiAnalysisField.repaint()

        elif self.display is "functions":
            if self.dynamicRun == False:
                for item in self.functionsStatic:
                    current = item["name"]
                    if current == selected:
                        self.vaddr = hex(item["minbound"])
                        self.vaddr = str(self.vaddr)
                        self.function = str(item["name"])
                        self.signature = str(item["signature"])
                        self.temp = self.signature.split('(')[1];
                        self.temp2 = self.temp.split(')')[0];
                        break
                self.analysis_tab.detailedPoiAnalysisField.setText("")
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("Virtual Memory Address: " + self.vaddr)
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("Function: " + self.function)
                self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                self.analysis_tab.detailedPoiAnalysisField.append("Parameters: " + self.temp2)
                font = self.analysis_tab.detailedPoiAnalysisField.font()
                font.setPointSize(12)
                self.analysis_tab.detailedPoiAnalysisField.setFont(font)
                self.analysis_tab.detailedPoiAnalysisField.repaint()
            elif self.dynamicRun:
                for i in range(len(dictList)):
                    current = dictList[i]['fName']
                    if current == selected:
                        self.funcName = dictList[i]['fName']
                        self.funcArgNum = str(dictList[i]['argNum'])
                        self.funcArgName = str(dictList[i]['argName'])
                        self.funcArgType = str(dictList[i]['argType'])
                        self.funcArgVal = str(dictList[i]['argVal'])
                        self.funcLocNum = str(dictList[i]['locNum'])
                        self.funcLocName = str(dictList[i]['locName'])
                        self.funcLocType = str(dictList[i]['locType'])
                        self.funcLocVal = str(dictList[i]['locVal'])
                        self.funcRetName = str(dictList[i]['retName'])
                        self.funcRetType = str(dictList[i]['retType'])
                        self.funcRetVal = str(dictList[i]['retValue'])


                        self.analysis_tab.detailedPoiAnalysisField.setText("")
                        self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                        self.analysis_tab.detailedPoiAnalysisField.append("Virtual Memory Address: " + self.vaddr)
                        self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                        self.analysis_tab.detailedPoiAnalysisField.append("Function Name: " + self.funcName)
                        self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                        self.analysis_tab.detailedPoiAnalysisField.append("Arg Number: " + self.funcArgNum)
                        self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                        self.analysis_tab.detailedPoiAnalysisField.append("Arg Name: " + self.funcArgName)
                        self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                        self.analysis_tab.detailedPoiAnalysisField.append("Arg Type: " + self.funcArgType)
                        self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                        self.analysis_tab.detailedPoiAnalysisField.append("Arg Value: " + self.funcArgVal)
                        self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                        self.analysis_tab.detailedPoiAnalysisField.append("Local Number: " + self.funcLocNum)
                        self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                        self.analysis_tab.detailedPoiAnalysisField.append("Local Name: " + self.funcLocName)
                        self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                        self.analysis_tab.detailedPoiAnalysisField.append("Local Type: " + self.funcLocType)
                        self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                        self.analysis_tab.detailedPoiAnalysisField.append("Local Value: " + self.funcLocVal)
                        self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                        self.analysis_tab.detailedPoiAnalysisField.append("Return Name: " + self.funcRetName)
                        self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                        self.analysis_tab.detailedPoiAnalysisField.append("Return Type: " + self.funcRetType)
                        self.analysis_tab.detailedPoiAnalysisField.append("\t" + "\n")
                        self.analysis_tab.detailedPoiAnalysisField.append("Return Value: " + self.funcRetVal)

                        font = self.analysis_tab.detailedPoiAnalysisField.font()
                        font.setPointSize(12)
                        self.analysis_tab.detailedPoiAnalysisField.setFont(font)
                        self.analysis_tab.detailedPoiAnalysisField.repaint()

    def set_r2(self, r2):
        self.r2 = r2