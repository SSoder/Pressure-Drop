# -*- coding: utf-8 -*-
"""
Created on Thu May  3 12:24:19 2018

@author: ssoder
"""

import sys
from PyQt5 import uic
from PyQt5 import QtWidgets



qtCreatorFile = "firstqtui.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MainWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.calctaxbutton.clicked.connect(self.CalculateTax)
        self.show()
    
    def CalculateTax(self):
        price = int(self.pricebox.toPlainText())
        tax = float(self.taxrate.value())
        totalprice = price + ((tax/100)*price)
        totalpricestr = "The total Price with tax is: " + str(totalprice)
        self.resultswindow.setText(totalpricestr)
    
        
if __name__ == "__main__":
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
