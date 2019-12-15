# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 23:44:14 2019

@author: Larson
"""

from PyQt5 import QtWidgets, uic
import os
import hmac
import hashliib
from CryptoPlus.Cipher import python_AES

path = os.getcwd()
qtCreatorFile = path + os.sep + "UI" + os.sep + "Main_UI.ui"  # 設計好的ui檔案路徑
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)   # 讀入用Qt Designer設計的GUI layout

class MainUi(QtWidgets.QMainWindow, Ui_MainWindow):  # Python的多重繼承 MainUi 繼承自兩個類別
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.iniGuiEvent()
    
    def iniGuiEvent(self):
        self.PB_calcKgNB.clicked.connect(self.calcKgNB_onClick)
        
    def calcKgNB_onClick(self):
        _ulNASCount = self.PT_ulNASCount.toPlainText()
        print("ul NAS Count = " + _ulNASCount)
        _Kamf = self.PT_Kamf.toPlainText()
        print("Kamf = " + _Kamf)
        self.PT_KgNB.setPlainText("hellousiajflksjflajlkfjakl;fj;akljfdkladjkl")
    
    def func_calcKgNB():
        KgNB = 0
        return KgNB
    