from asyncio.windows_events import NULL

from numpy import delete
import os

from Ui_History import Ui_history
import FocusWindow
import ReportWindow

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog,QTableWidgetItem


class History(QDialog):

    def __init__(self):
        QDialog.__init__(self)

        self.child = Ui_history()
        self.child.setupUi(self)

        names=os.listdir(".vscode/Zhuyi/focus_history")
        for name in names:
            self.child.history_list.addItem(name)

        self.child.history_list.itemDoubleClicked.connect(lambda:self.openHistory())
        self.child.del_history.clicked.connect(lambda:self.delHistory())

    def openHistory(self):
        self.report = ReportWindow.ReportWindow(self.child.history_list.currentItem().text())
        self.report.show()

    def delHistory(self):
        os.remove(".vscode/Zhuyi/focus_history/"+self.child.history_list.currentItem().text())
        self.child.history_list.takeItem(self.child.history_list.currentIndex().row())