# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstqtui2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 566)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pricebox = QtWidgets.QTextEdit(self.centralwidget)
        self.pricebox.setGeometry(QtCore.QRect(230, 160, 104, 31))
        self.pricebox.setObjectName("pricebox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 170, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.taxrate = QtWidgets.QSpinBox(self.centralwidget)
        self.taxrate.setGeometry(QtCore.QRect(250, 260, 42, 22))
        self.taxrate.setProperty("value", 20)
        self.taxrate.setObjectName("taxrate")
        self.calctaxbutton = QtWidgets.QPushButton(self.centralwidget)
        self.calctaxbutton.setGeometry(QtCore.QRect(230, 350, 75, 23))
        self.calctaxbutton.setObjectName("calctaxbutton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 270, 47, 13))
        self.label_2.setObjectName("label_2")
        self.resultswindow = QtWidgets.QTextEdit(self.centralwidget)
        self.resultswindow.setGeometry(QtCore.QRect(330, 340, 104, 31))
        self.resultswindow.setObjectName("resultswindow")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 20, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Price"))
        self.calctaxbutton.setText(_translate("MainWindow", "Calculate Tax"))
        self.label_2.setText(_translate("MainWindow", "Tax Rate"))
        self.label_3.setText(_translate("MainWindow", "Sales Tax Calculator"))

