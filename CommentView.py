# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CommentView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_commentView(object):
    def setupUi(self, commentView):
        commentView.setObjectName("commentView")
        commentView.resize(616, 402)
        self.clearButton = QtWidgets.QPushButton(commentView)
        self.clearButton.setGeometry(QtCore.QRect(490, 360, 113, 32))
        self.clearButton.setObjectName("clearButton")
        self.saveCommentButton = QtWidgets.QPushButton(commentView)
        self.saveCommentButton.setGeometry(QtCore.QRect(360, 360, 113, 32))
        self.saveCommentButton.setObjectName("saveCommentButton")
        self.commentField = QtWidgets.QTextEdit(commentView)
        self.commentField.setGeometry(QtCore.QRect(20, 20, 581, 331))
        self.commentField.setObjectName("commentField")

        self.retranslateUi(commentView)
        QtCore.QMetaObject.connectSlotsByName(commentView)

    def retranslateUi(self, commentView):
        _translate = QtCore.QCoreApplication.translate
        commentView.setWindowTitle(_translate("commentView", "Comment View"))
        self.clearButton.setText(_translate("commentView", "Clear"))
        self.saveCommentButton.setText(_translate("commentView", "+Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    commentView = QtWidgets.QDialog()
    ui = Ui_commentView()
    ui.setupUi(commentView)
    commentView.show()
    sys.exit(app.exec_())
