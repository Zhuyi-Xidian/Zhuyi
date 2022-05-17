from Ui_BeginWindow import Ui_MainWindow
import FocusWindow
import Settings

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog


class beginWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    focusWindow=0

    def __init__(self):
        super(beginWindow, self).__init__()
        self.setupUi(self)

        #日期时间星期显示
        self.Timer = QTimer()
        self.Timer.start(1000)  #间隔1s
        self.Timer.timeout.connect(self.showtime)
        self.Timer.timeout.connect(self.showdate)
        self.Timer.timeout.connect(self.showweek)

    #日期时间星期槽函数
    def showtime(self):
        self.time_display.setText(
            QDateTime.currentDateTime().toString('hh:mm:ss'))

    def showdate(self):
        self.date_display.setText(
            QDateTime.currentDateTime().toString('yyyy-MM-dd'))

    def showweek(self):
        self.week_display.setText(QDateTime.currentDateTime().toString('dddd'))

    #开始专注
    def showFocusWidow(self):
        if self.focusWindow!=0:
            del self.focusWindow
        self.focusWindow = FocusWindow.focusWindow(screen_height, screen_height)
        self.focusWindow.show()

    #打开设置
    def showSettigns(self):
        self.settings = Settings.Settings()
        self.settings.show()

if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    screen_width = app.primaryScreen().geometry().width()
    screen_height = app.primaryScreen().geometry().height()
    beginWindow = beginWindow()
    beginWindow.show()
    beginWindow.begin_focus.clicked.connect(
        lambda: beginWindow.showFocusWidow())
    beginWindow.settings.clicked.connect(lambda: beginWindow.showSettigns())

    sys.exit(app.exec_())
