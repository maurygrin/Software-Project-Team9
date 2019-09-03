from tkinter import *

from tkinter import Menu
 
window = Tk()
 
window.title("Binary Extraction and Analysis Tool")

menu = Menu(window)
 
file = Menu(menu)

file.add_command(label = 'Open File')

file.add_separator()
 
file.add_command(label = 'Upload File')
 
file.add_separator()
 
file.add_command(label = 'Open File')

file.add_separator()
 
file.add_command(label = 'Save')

file.add_separator()
 
file.add_command(label = 'Save As')

file.add_separator()
 
file.add_command(label = 'Properties')

file.add_separator()
 
file.add_command(label = 'Close')

jump = Menu(menu)

jump.add_command(label = 'Hexa')
 
jump.add_separator()

jump.add_command(label = 'Address')
 
jump.add_separator()

jump.add_command(label = 'String')

# Name Conflict(View) 
#view = Menu(menu)

#view.add_command(label = 'Graph View')
 
#view.add_separator()

#view.add_command(label = 'Text View')

plugin = Menu(menu)

plugin.add_command(label = 'Choose Plugin')
 
plugin.add_separator()

plugin.add_command(label = 'Generate Output')
 
menu.add_cascade(label = 'File', menu = file)

menu.add_cascade(label = 'Jump', menu = jump)
 
#menu.add_cascade(label = 'View', menu = view)

menu.add_cascade(label = 'Plugin', menu = plugin)

window.config(menu = menu)
 
window.geometry('1274x1024')
 
#lbl = Label(window, text="Hello")
 
#lbl.grid(column=0, row=0)
 
def clicked():
 
    lbl.configure(text="Button was clicked !!")
 
btn = Button(window, text="Click Me", command=clicked)
 
btn.grid(column=1, row=0)
 
window.mainloop()
