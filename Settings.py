from asyncio.windows_events import NULL

from numpy import delete
from Ui_Settings import Ui_settings
import FocusWindow

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog,QTableWidgetItem


class Settings(QDialog):

    def __init__(self):
        QDialog.__init__(self)

        self.child = Ui_settings()
        self.child.setupUi(self)

        #读取文件初始化
        file=open(".vscode/Zhuyi/BlockedProc.txt","r",encoding = "utf-8")
        for line in file:
            self.child.now_proc.addItem(line[:-1])
        file.close()

        #添加
        self.child.add_proc.clicked.connect(lambda:self.addproc())
        #保存
        self.child.save.clicked.connect(lambda:self.save())
        #删除
        self.child.now_proc.itemClicked.connect(lambda:self.getrow())
        self.child.delnow.clicked.connect(lambda:self.delnow())
    
    def addproc(self):
        if (self.ifexists(self.child.new_proc.text())==False and self.child.new_proc.text()!=NULL):
            self.child.now_proc.addItem(self.child.new_proc.text())

    def ifexists(self,tofind):
        for i in range(self.child.now_proc.count()):
            if self.child.now_proc.item(i).text()==tofind:
                return True
        return False

    def save(self):
        file=open(".vscode/Zhuyi/BlockedProc.txt","r+",encoding = "utf-8")
        file.truncate()
        for i in range(self.child.now_proc.count()):
            file.write(self.child.now_proc.item(i).text()+'\n')
        file.close()

    def getrow(self):
        self.nowrow=self.child.now_proc.currentIndex().row()
        
    def delnow(self):
        self.child.now_proc.takeItem(self.nowrow)
