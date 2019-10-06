import sys
import r2pipe


class Script:
    
    def __init__(self):
        pass

    def sendStrings(self, r2):  # Sends strings from the binary file
        results = r2.cmd("iz")
        print(results)

    def sendFunctions(self, r2):  # Sends functions from the binary file
        results = r2.cmd("afl")
        print(results)

    def sendVariables(self, r2):  # Sends variables from the binary file
        results = r2.cmd("afv")
        print(results)

    def analyzeFile(self, r2, display): # Analize the binary file
        r2.cmd("aa")
        if display == "strings":
            self.sendStrings(r2)
        if display == "functions":
            self.sendFunctions(r2)
        if display == "variables":
            self.sendVariables(r2)
        


#print(r2.cmd("iS")) # Prints sections
#print(r2.cmd("ii")) # Prints imports
#print(r2.cmd("ie")) # Prints entry points
#print(r2.cmd("pdb")) # Prints basic block disassembly
#print(r2.cmd("pdf")) # Prints function disassembly
#print(r2.cmd("afa")) # Prints function arguments
#print(r2.cmd("afv")) # Prints function variables
#print(r2.cmd("CC!")) # Add comment
#print(r2.cmd("CC <text>")) # Append comment
#print(r2.cmd("CCu <text>")) # Overwrite comment
#print(r2.cmd("CC.")) # Show comment
#print(r2.cmd("CCf")) # Show comment in this function


# JSON 
# list = []
# jsonstring = r2.cmdj("iz")[0]
# list.append(jsonstring['opcode'])
# print(list)

