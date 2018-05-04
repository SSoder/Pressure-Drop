# -*- coding: utf-8 -*-
"""
Created on Fri May  4 13:14:11 2018

@author: ssoder
"""

from PyQt5 import uic

qtCreatorFile = ".\presgui\presMainUi.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MainWindow(QtBaseClass, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
