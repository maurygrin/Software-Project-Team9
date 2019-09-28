import sys
import r2pipe

r2 = r2pipe.open("./a.out") # Opens binary file
r2.cmd("aa") # Analize the binary file
print(r2.cmd("iz")) # Prints strings
print(r2.cmd("iS")) # Prints sections
print(r2.cmd("afl")) # Prints functions
print(r2.cmd("ii")) # Prints imports
print(r2.cmd("ie")) # Prints entry points
#print(r2.cmd("pdb")) # Prints basic block disassembly
#print(r2.cmd("pdf")) # Prints function disassembly
print(r2.cmd("afa")) # Prints function arguments
print(r2.cmd("afv")) # Prints function variables
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

