from asyncio.windows_events import NULL
from Ui_Report import Ui_report
import FocusWindow

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog,QTableWidgetItem


from time import strftime
from time import gmtime


class ReportWindow(QDialog):

    def __init__(self,filename):
        QDialog.__init__(self)

        self.child = Ui_report()
        self.child.setupUi(self)

        file = open(".vscode/Zhuyi/focus_history/"+filename, "r", encoding="utf-8")
        lines=file.readlines()
        print(lines)
        self.child.focus_time.setText(strftime("%H:%M:%S", gmtime(int(lines[0][:-1]))))
        self.child.eye_det_fail_time.setText(lines[1][:-1])
        self.child.eye_det_fail_per.setText(lines[2][:-1])
        self.child.proc_det_fail_time.setText(lines[3][:-1])