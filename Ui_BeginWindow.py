# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\S\VSCforPython\.vscode\Zhuyi\BeginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 597)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.begin_focus = QtWidgets.QPushButton(self.centralwidget)
        self.begin_focus.setGeometry(QtCore.QRect(330, 250, 121, 41))
        self.begin_focus.setObjectName("begin_focus")
        self.chicken_soup = QtWidgets.QLabel(self.centralwidget)
        self.chicken_soup.setGeometry(QtCore.QRect(140, 520, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.chicken_soup.setFont(font)
        self.chicken_soup.setObjectName("chicken_soup")
        self.date_display = QtWidgets.QLabel(self.centralwidget)
        self.date_display.setGeometry(QtCore.QRect(620, 40, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.date_display.setFont(font)
        self.date_display.setObjectName("date_display")
        self.week_display = QtWidgets.QLabel(self.centralwidget)
        self.week_display.setGeometry(QtCore.QRect(620, 90, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.week_display.setFont(font)
        self.week_display.setObjectName("week_display")
        self.time_display = QtWidgets.QLabel(self.centralwidget)
        self.time_display.setGeometry(QtCore.QRect(620, 140, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.time_display.setFont(font)
        self.time_display.setObjectName("time_display")
        self.focus_history = QtWidgets.QPushButton(self.centralwidget)
        self.focus_history.setGeometry(QtCore.QRect(40, 20, 121, 41))
        self.focus_history.setObjectName("focus_history")
        self.settings = QtWidgets.QPushButton(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(170, 20, 111, 41))
        self.settings.setObjectName("settings")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "铸意"))
        self.begin_focus.setText(_translate("MainWindow", "开始专注"))
        self.chicken_soup.setText(_translate("MainWindow", "chicken soup here"))
        self.date_display.setText(_translate("MainWindow", "date here"))
        self.week_display.setText(_translate("MainWindow", "week here"))
        self.time_display.setText(_translate("MainWindow", "time here"))
        self.focus_history.setText(_translate("MainWindow", "专注历史"))
        self.settings.setText(_translate("MainWindow", "设置"))