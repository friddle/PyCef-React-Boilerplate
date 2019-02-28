import platform
import pycef as cef
from cefpython3 import cefpython as cef
import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QtCefApplication(QApplication):
    def __init__(self, args):
        super(QtCefApplication, self).__init__(args)
        if not cef.GetAppSetting("external_message_pump"):
            self.timer = self.createTimer()
        self.setupIcon()

    def createTimer(self):
        timer = QTimer()
        # noinspection PyUnresolvedReferences
        timer.timeout.connect(self.onTimer)
        timer.start(10)
        return timer

    def onTimer(self):
        cef.MessageLoopWork()

    def stopTimer(self):
        # Stop the timer after Qt's message loop has ended
        self.timer.stop()

    # TODO:set environment
    def setupIcon(self):
        icon_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "resources", "qt5.png")
        if os.path.exists(icon_file):
            self.setWindowIcon(QIcon(icon_file))
