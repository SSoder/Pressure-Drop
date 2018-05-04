# -*- coding: utf-8 -*-
"""
Created on Fri May  4 13:16:51 2018

@author: ssoder
"""

import sys
from PyQt5 import QtWidgets
import presgui.presUI as GUI



if __name__ == "__main__":
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    window = GUI.MainWindow()
    window.show()
    sys.exit(app.exec_())