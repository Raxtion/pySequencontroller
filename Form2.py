# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form2.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_Form(object):
    def setupUi(self, QDialog):
        QDialog.setObjectName("GeneCode")
        QDialog.resize(770, 533)
        self.graphicsView = QtWidgets.QGraphicsView(QDialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 641, 421))
        self.graphicsView.setMinimumSize(QtCore.QSize(771, 534))
        self.graphicsView.setMaximumSize(QtCore.QSize(771, 534))
        self.graphicsView.setObjectName("graphicsView")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("windows_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QDialog.setWindowIcon(icon)

        self.pic = QtGui.QPixmap(os.getcwd() + '\\' + 'genecode.bmp')
        self.QLabel = QtWidgets.QLabel(QDialog)
        self.QLabel.setPixmap(self.pic)

        self.retranslateUi(QDialog)
        QtCore.QMetaObject.connectSlotsByName(QDialog)

    def retranslateUi(self, QDialog):
        _translate = QtCore.QCoreApplication.translate
        QDialog.setWindowTitle(_translate("GeneCode", "GeneCode"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())