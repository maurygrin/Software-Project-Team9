import sys
import r2pipe

from Script import Script

r2 = r2pipe.open("./a.out")
display = "variables"
analysis = Script()
analysis.analyzeFile(r2, display)
