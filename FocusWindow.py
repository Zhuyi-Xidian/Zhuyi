from __future__ import unicode_literals
import cv2

from turtle import screensize
from Ui_Focus import Ui_focus

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt, QPropertyAnimation, QDateTime, QTimer, QTime
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *

import psutil

fd = cv2.CascadeClassifier(
    r'E:/S/VSCforPython/.vscode/haarcascades/haarcascade_frontalface_alt.xml')
ed = cv2.CascadeClassifier(
    r'E:/S/VSCforPython/.vscode/haarcascades/haarcascade_eye_tree_eyeglasses.xml'
)
vc = cv2.VideoCapture(0)
flag = 0


class focus():

    begin_time = QDateTime.currentDateTime()
    end_time = QDateTime.currentDateTime()
    eye_close_time = 0
    eye_close_due = 0
    app_time = 0
    

    def __init__(self) -> None:
        self.begin_time = QDateTime.currentDateTime()

    def __del__(self):
        pass

    def eyeMonitor(self):
        frame = vc.read()[1]
        frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = fd.detectMultiScale(frame, 1.3, 5)
        face = vc.read()[1]
        for l, t, w, h in faces:
            a, b = int(w / 2), int(h / 2)
            cv2.ellipse(frame, (l + a, t + b), (a, b), 0, 0, 360,
                        (255, 0, 255), 2)
            face = frame[t:t + h, l:l + w]

        eyes = ed.detectMultiScale(face, 1.3, 5)
        for l, t, w, h in eyes:
            a, b = int(w / 2), int(h / 2)
            cv2.ellipse(face, (l + a, t + b), (a, b), 0, 0, 360, (0, 255, 0),
                        2)

        cv2.imshow('eyes', frame)

        if len(eyes) != 0:
            cv2.putText(frame, 'eyes open', (10, 10), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 255, 0), 2)
            print('eyes open!\n')
            flag = 1
        if len(eyes) == 0:
            cv2.putText(frame, 'eyes close', (10, 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            print('eyes close!\n')
            flag = 0

    def procMonitor(self):
        pl = psutil.pids()
        for pid in pl:
            print( psutil.Process(pid).name())

class focusWindow(QDialog):

    screen_width = 1
    screen_height = 1
    window_width = 1
    window_height = 1

    hidden = False

    focus_class = 1

    def __init__(self, screen_width, screen_height):
        QDialog.__init__(self)

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.child = Ui_focus()
        self.child.setupUi(self)

        self.focus_class = focus()

        #人眼识别计时器
        self.eye_monitor_timer = QTimer()
        self.eye_monitor_timer.start(100)  #每0.1s进行一次人眼识别
        self.eye_monitor_timer.timeout.connect(
            lambda: self.focus_class.eyeMonitor())

        #专注时间计时器
        self.time_display_timer = QTimer()
        self.time_display_timer.start(1000) #每1s更新专注时间
        #elf.time_display_timer.timeout.connect(lambda:self.focusTimeDisplay())

        #进程监控
        self.focus_class.procMonitor()

        #识别窗口大小
        window_width = self.geometry().width()
        window_height = self.geometry().height()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
                            | Qt.Tool)
        # 窗口背景透明
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # 明度(0~1)
        self.setWindowOpacity(0.5)
        # 手状鼠标
        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            # event.pos() 鼠标相对窗口的位置
            # event.globalPos() 鼠标在屏幕的绝对位置
            self._startPos = event.pos()

    # 鼠标移动时，移动窗口跟上鼠标；同时限制窗口位置，不能移除主屏幕
    def mouseMoveEvent(self, event: QMouseEvent):
        # event.pos()减去最初相对窗口位置，获得移动距离(x,y)
        self._wmGap = event.pos() - self._startPos
        # 移动窗口，保持鼠标与窗口的相对位置不变
        # 检查是否移除了当前主屏幕
        # 左方界限
        final_pos = self.pos() + self._wmGap
        if self.frameGeometry().topLeft().x() + self._wmGap.x() <= 0:
            final_pos.setX(0)
        # 上方界限
        if self.frameGeometry().topLeft().y() + self._wmGap.y() <= 0:
            final_pos.setY(0)
        # 右方界限
        if self.frameGeometry().bottomRight().x() + self._wmGap.x(
        ) >= self.screen_width:
            final_pos.setX(self.screen_width - self.window_width)
        # 下方界限
        if self.frameGeometry().bottomRight().y() + self._wmGap.y(
        ) >= self.screen_height:
            final_pos.setY(self.screen_height - self.window_height)
        self.move(final_pos)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self._startPos = None
            self._wmGap = None
        if event.button() == Qt.RightButton:
            self._startPos = None
            self._wmGap = None

    #以下实现贴边隐藏
    def enterEvent(self, event):
        self.hide_or_show('show', event)

    def leaveEvent(self, event):
        self.hide_or_show('hide', event)

    def hide_or_show(self, mode, event):
        # 获取窗口左上角x,y
        pos = self.frameGeometry().topLeft()
        if mode == 'show' and self.hidden:
            # 窗口左上角x + 窗口宽度 大于屏幕宽度，从右侧滑出
            if pos.x() + self.window_width >= self.screen_width:
                # 需要留10在里边，否则边界跳动
                self.startAnimation(self.screen_width - self.window_width,
                                    pos.y())
                event.accept()
                self.hidden = False
            # 窗口左上角x 小于0, 从左侧滑出
            elif pos.x() <= 0:
                self.startAnimation(0, pos.y())
                event.accept()
                self.hidden = False
            # 窗口左上角y 小于0, 从上方滑出
            elif pos.y() <= 0:
                self.startAnimation(pos.x(), 0)
                event.accept()
                self.hidden = False
        elif mode == 'hide' and (not self.hidden):
            if pos.x() + self.window_width >= self.screen_width:
                # 留10在外面
                self.startAnimation(self.screen_width - 10, pos.y(), mode,
                                    'right')
                event.accept()
                self.hidden = True
            elif pos.x() <= 0:
                # 留10在外面
                self.startAnimation(10 - self.window_width, pos.y(), mode,
                                    'left')
                event.accept()
                self.hidden = True
            elif pos.y() <= 0:
                # 留10在外面
                self.startAnimation(pos.x(), 10 - self.window_height, mode,
                                    'up')
                event.accept()
                self.hidden = True

    def startAnimation(self, x, y, mode='show', direction=None):
        animation = QPropertyAnimation(self, b"geometry", self)
        # 滑出动画时长
        animation.setDuration(200)
        # 隐藏时，只留10在外边，防止跨屏
        # QRect限制其大小，防止跨屏
        num = QApplication.desktop().screenCount()
        if mode == 'hide':
            if direction == 'right':
                animation.setEndValue(
                    QtCore.QRect(x, y, 10, self.window_height))
            elif direction == 'left':
                # 多屏时采用不同的隐藏方法，防止跨屏
                if num < 2:
                    animation.setEndValue(
                        QtCore.QRect(x, y, self.window_width,
                                     self.window_height))
                else:
                    animation.setEndValue(
                        QtCore.QRect(0, y, 10, self.window_height))
            else:
                if num < 2:
                    animation.setEndValue(
                        QtCore.QRect(x, y, self.window_width,
                                     self.window_height))
                else:
                    animation.setEndValue(
                        QtCore.QRect(x, 0, self.window_width, 10))
        else:
            animation.setEndValue(
                QtCore.QRect(x, y, self.window_width, self.window_height))
        animation.start()
    #贴边隐藏结束

    def focusTimeDisplay(self):
        q_time=QDateTime.currentDateTime()
        q_time.setTime(QTime())
        self.child.focus_time.setText(q_time.addSecs(focus.begin_time.secsTo(QDateTime.currentDateTime())).toString("hh:mm:ss"))


    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:

        return super().paintEvent(a0)