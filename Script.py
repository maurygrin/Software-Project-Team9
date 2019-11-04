import sys
import r2pipe


class Script:
    
    def __init__(self):
        pass

    def sendStrings(self, r2):  # Sends strings from the binary file
        results = r2.cmdj("izj")
        return results

    def sendFunctions(self, r2):  # Sends functions from the binary file
        results = r2.cmd("afl")
        return results

    def sendVariables(self, r2):  # Sends variables from the binary file
        results = r2.cmdj("afvj")
        return results

    def sendDLLs(self, r2):  # Sends variables from the binary file
        results = r2.cmdj("iij")
        return results



    def display(self, r2, display): # Analyze the binary file
        if display == "strings":
            return self.sendStrings(r2)
        if display == "functions":
            return self.sendFunctions(r2)
        if display == "variables":
            return self.sendVariables(r2)
        if display == "dlls":
            return self.sendDLLs(r2)

    def analyzeFile(self, r2): # Analyze the binary file
        r2.cmd("aa")
        return r2

    def startDynamic(self, r2):
        r2.cmd("oo")
        r2.cmd("ood")
        return r2


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


#DYNAMIC COMMANDS???
#do: Reopen program
#dp: Shows debugged process, child processes and threads
#dc: Continue
#dcu <address or symbol>: Continue until symbol (sets bp in address, continua until bp and remove bp)
#dc[sfcp]: Continue until syscall(eg: write), fork, call, program address (To exit a library)
#ds: Step in
#dso: Step out
#dss: Skip instruction
#dr register=value: Change register value
#dr(=)?: Show register values
#db address: Sets a breakpoint at address
#db sym.main add breakpoint into sym.main
#db 0x804800 add breakpoint
#db -0x804800 remove breakpoint
#dsi (conditional step): Eg: "dsi eax==3,ecx>0"
#dbt: Shows backtrace
#drr: Display in colors and words all the refs from registers or memory
#dm: Shows memory map (* indicates current section)

# JSON 
# list = []
# jsonstring = r2.cmdj("iz")[0]
# list.append(jsonstring['opcode'])
# print(list)

