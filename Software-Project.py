from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMenu
from PyQt5.uic.Compiler.qtproxies import QtGui

Form, Window = uic.loadUiType("main.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec_()


