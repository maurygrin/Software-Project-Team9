import json, threading

from PyQt5 import QtCore, QtWidgets

staticFunctionList=[]
functionDict = []

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
        #The error to see if the user has not selected a plugin.
        if (self.analysis_tab.pluginDropDownAnalysis.currentText() == "Select"):
            self.analysis_tab.setupPluginError(self.windowPluginError)
            self.analysis_tab.windowPluginError.show()
        #Everything is ok to start static analysis
        else:
            self.analysis_tab.runDynamicButton.setEnabled(True)

            self.static = 1
            #Terminal Show what analysis was performed
            self.analysis_tab.terminalField.append("Static Analysis Performed!")
            self.analysis_tab.terminalField.append("")
            #Radare command to start analysis
            self.r2.cmd("aaa")
            #Radare command to list functions
            self.functionsStatic = self.r2.cmdj("afllj")
            #Radare command to list strings, izz lists strings in the whole library
            self.stringsStatic = self.r2.cmdj("izzj")

            #Get what the user selected from the drop down menu.
            poiSelected = self.analysis_tab.poiTypeDropDownAnalysis.currentText()
            #Populate if strings was choosen
            if (poiSelected=="Strings"):
                #Append command to the terminal
                self.analysis_tab.terminalField.append("Command: izz")
                #Saying that we are going to display strings
                self.display = "strings"
                self.analysis_tab.detailedPoiAnalysisField.setText("")
                self.analysis_tab.poiAnalysisList.clear()
                #This part is not apending the values, it is just simply appending the text.
                #These is what we are looking for here.
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
                #for every string you found in the analysis
                for item in self.stringsStatic:
                    #Add the string name to the widget list
                    item = QtWidgets.QListWidgetItem(item["string"])
                    #Set up the checkable boxes for breakpoints
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                    item.setCheckState(QtCore.Qt.Checked)
                    #Add the String as an item to the list located to the left of the window.
                    self.analysis_tab.poiAnalysisList.addItem(item)
            #If the Functions drop down was selceted
            elif (poiSelected=="Functions"):
                #Append command to the terminal
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
                #for every string found in the analysis of functions
                for item in self.functionsStatic:
                    #Add the name of the function to a list,
                    #this is important for dynamic analysis.
                    staticFunctionList.append(item["name"])
                    item = QtWidgets.QListWidgetItem(item["name"])
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                    item.setCheckState(QtCore.Qt.Checked)
                    #Append the function item to the left of the window.
                    self.analysis_tab.poiAnalysisList.addItem(item)
                #Call the method that populates the dictionary to hold the values of the functions analysis.
                self.populateFunctionsDict(staticFunctionList)

    def populateFunctionsDict(self, staticFunctionList):
        keys = ['funcName', 'argNum', 'argName', 'argType', 'argVal', 'retName', 'retType', 'retValue', 'locName',
                'locType', 'locNum', 'locVal']
        # These will be used to know the order.
        argOrder = 0
        locOrder = 0
        # Dictionary to hold values needed for functions.
        funcKeys = dict.fromkeys(keys, [])
        #start the analysis
        self.r2.cmd("aaa")
        #For every function from static analysis
        for i in range(len(staticFunctionList)):
            #add the mname of the function to the dictionary in apropriate field
            funcKeys['funcName'] = (staticFunctionList[i])
            #Radare command to get th args, registers, and variables in that function.
            arvFunc = self.r2.cmd("afvj @ " + staticFunctionList[i])
            formatARV = json.loads(arvFunc)
            for key in formatARV.keys():
                #to hold list of args, registers, and variables found for that function.
                tempList = formatARV[key]
                #to hold the name of the args
                namesArgs = []
                #to hold the types of the args
                typesArgs = []
                #to hold the local variable names
                namesLocal = []
                #to hold the local variable types
                typesLocal = []
                #iterate to populate information
                for j in range(len(tempList)):
                    #we will populate different things accordingly
                    if tempList[j]['kind'] == 'reg':
                        #if it found a reg, update the counter to know the order
                        argOrder += 1
                        funcKeys['argNum'] = argOrder
                        namesArgs.append(tempList[j]['name'])
                        typesArgs.append(tempList[j]['type'])
                        funcKeys['argName'] = namesArgs
                        funcKeys['argType'] = typesArgs
                    if tempList[j]['kind'] == 'var':
                        #if it found a var, update the counter to know the order
                        locOrder += 1
                        funcKeys['locNum'] = locOrder
                        namesLocal.append(tempList[j]['name'])
                        typesLocal.append(tempList[j]['type'])
                        funcKeys['locName'] = namesLocal
                        funcKeys['locType'] = typesLocal
            #once they step out of this loop it means it is done
            #populating the information for that specific function
            #therefore we need to retart the counter for the order
            argOrder = 0
            locOrder = 0
            #we also need to add it to the global list that holds what we will dipslay.
            functionDict.append(funcKeys)
            #for testing purposes only
            sample = open('functionDict.txt', 'w')
            print(str(functionDict), file=sample)
            sample.close()
            funcKeys = dict.fromkeys(keys, [])


    # function to stop dynamic analysis
    def stopDynamicAnalysis(self):
        self.r2.cmd("break")
    #making a thread to run in the background
    def dynamicAnalysisThread(self):
        threading.Thread(target=self.runDynamicAnalysis(), args=(10,)).start()
        self.analysis_tab.runStaticButton.setEnabled(False)
        self.dynamicRun = True

    #dynamic analysis
    #so now that the list is populated we can go ahead an do dynamic analysis
    def runDynamicAnalysis(self):
        #iterate through the dictionary populated before
        for i in range(len(functionDict)):
            validFlag = True #is arg num populated flag
            if(functionDict[i]['argNum'] == []): #check to see if there is anything populated
                validFlag = False

            validFlag2 = True #is locNum populated flag
            if(functionDict[i]['locNum'] == []): # check to see if there is anything populated
                validFlag2 = False


            self.r2.cmd("e dbg.bpinmaps=0")  # disable cannot set breakpoint on unmapped memory
            self.r2.cmd("ood")  # open in debug mode
            self.r2.cmd("aaa")  #do analsysis

            #before starting to set breakpoints, we must check user input to see if the user,
            #unchecked boxes, meaning that they do not wish to run dynamic with a breakpoint
            #in that location.
            if self.analysis_tab.poiAnalysisList.item(i).checkState() !=0:
                #get the name of the function, make a string that holds the command for bp
                breakpointCommand = "db " + (functionDict[i]['funcName'])
                self.r2.cmd(breakpointCommand)  # set breakpoint at that function
                self.r2.cmd("dc")  # Run until you hit the breakpoint
                #get the value of the rax register to get return value
                returnVal = self.r2.cmd("dr rax")
                #start running after breakpoint get arguments first
                templistVals = []
                templistLoc = []
                # get argument information
                if(validFlag):
                    for j in range(functionDict[i]['argNum']):
                        # set return value
                        functionDict[i]['retVal'] = returnVal
                        #r2 command for displaying the value of args/locals in the debugger
                        commandArgVal = self.r2.cmd("afvd " + str(functionDict[i]['argName'][j]))
                        #check that it actually has a value
                        if commandArgVal != "":
                            #split the output, so we could get it in json format
                            commandV = commandArgVal.split(" ")
                            jsonCommand = commandV[0] + "j " + commandV[1] + " " + commandV[2]
                            turnToJson = self.r2.cmd(jsonCommand)
                            formattedVal = json.loads(turnToJson)
                            templistVals.append(formattedVal[0]['value'])
                            functionDict[i]['argVal'] = templistVals

                # get locals information
                if(validFlag2):
                    for k in range(functionDict[i]['locNum']):
                            #r2 command for displaying the value of args/locals in the debugger
                            commandLocVal = self.r2.cmd("afvd " + str(functionDict[i]['locName'][k]))
                            #check that it actually returned something
                            if commandLocVal != "":
                                #not sure why it was breaking here, but i just passed it if it couldnt perform it.
                                try:
                                    #split the output, so we could get it in json format
                                    commandL = commandLocVal.split(" ")
                                    jsonCommand = commandL[0] + "j " + commandL[1] + " " + commandL[2]
                                    turnToJson = self.r2.cmd(jsonCommand)
                                    formattedVal = json.loads(turnToJson)
                                    templistLoc.append(formattedVal[0]['value'])
                                    functionDict[i]['locVal'] = templistLoc
                                except:
                                    pass

                self.r2.cmd("db-*") # remove all the breakpoints
        #Display Dynamic results
        poiSelected = self.analysis_tab.poiTypeDropDownAnalysis.currentText()

        if (poiSelected == "Strings"):
            self.analsysis_tab.terminalField.append("Dynamic Analysis performed!")
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
                counter = 0
                for item in self.functionsStatic:
                    staticFunctionList.append(item["name"])
                    item = QtWidgets.QListWidgetItem(item["name"])
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                    item.setCheckState(QtCore.Qt.Checked)
                    self.analysis_tab.poiAnalysisList.addItem(item)
                    counter = counter + 1

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
                font.setPointSize(12)
                self.analysis_tab.detailedPoiAnalysisField.setFont(font)
                self.analysis_tab.detailedPoiAnalysisField.repaint()
                for item in self.stringsStatic:
                    item = QtWidgets.QListWidgetItem(item["string"])
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
                    item.setCheckState(QtCore.Qt.Checked)
                    self.analysis_tab.poiAnalysisList.addItem(item)

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
                for i in range(len(functionDict)):
                    current = functionDict[i]['funcName']
                    if current == selected:
                        self.funcName = functionDict[i]['funcName']
                        self.funcArgNum = str(functionDict[i]['argNum'])
                        self.funcArgName = str(functionDict[i]['argName'])
                        self.funcArgType = str(functionDict[i]['argType'])
                        self.funcArgVal = str(functionDict[i]['argVal'])
                        self.funcLocNum = str(functionDict[i]['locNum'])
                        self.funcLocName = str(functionDict[i]['locName'])
                        self.funcLocType = str(functionDict[i]['locType'])
                        self.funcLocVal = str(functionDict[i]['locVal'])
                        self.funcRetName = str(functionDict[i]['retName'])
                        self.funcRetType = str(functionDict[i]['retType'])
                        self.funcRetVal = str(functionDict[i]['retValue'])


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