import copy
import os
import platform
import sys

import pycef as cef
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from cefpython3 import cefpython as cef

from src.framework.QtCefWidget import QtCefWidget
from src.framework.jswrapper.util import ModuleRegister, ModuleBase
from src.framework.qt.QCefApplication import QtCefApplication
from src.framework.qt.widget.NavigationBar import NavigationBar
from src.framework.util.framework.module_utils import import_submodules, transformDict

WINDOWS = (platform.system() == "Windows")
LINUX = (platform.system() == "Linux")
MAC = (platform.system() == "Darwin")

## TODO:这里都从环境变量里面Get到
## TODO:初始化部分模块也在这里初始化。
## React:

WIDTH = 800
HEIGHT = 600
Title = "周林傻逼"
BEGIN_URL = "file://" + os.path.abspath(os.path.join(os.path.abspath(__file__), "../../dist/app.html"))
NVIGATE_BAR = False
DEBUG = True

os.putenv("DEBUG", str(DEBUG))

##添加SubModule
import_submodules("src.backend")
import_submodules("src.framework.jswrapper")




# 版本号检查
def check_versions():
    print("[qt.py] CEF Python {ver}".format(ver=cef.__version__))
    assert cef.__version__ >= "55.4", "CEF Python v55.4+ required to run this"


class MainWindow(QMainWindow):
    def __init__(self):
        # noinspection PyArgumentList
        super(MainWindow, self).__init__(None)
        # Avoids crash when shutting down CEF (issue #360)
        self.setWindowTitle(Title)
        self.setFocusPolicy(Qt.StrongFocus)
        self.env = transformDict(os.environ._data)
        self.module_registry = self.generateModule()
        self.setupLayout()
        self.navigation_bar = None

    def generateModule(self):
        module_register = ModuleRegister()
        for module in ModuleBase.__subclasses__():
            module_register.registry(module())
        return module_register

    def setupLayout(self):
        self.resize(WIDTH, HEIGHT)
        self.cef_widget = QtCefWidget(self, BEGIN_URL, self.module_registry, self.env)
        self.navigation_bar = NavigationBar(self.cef_widget)
        layout = QGridLayout()

        if NVIGATE_BAR:
            layout.addWidget(self.navigation_bar, 0, 0)

        layout.addWidget(self.cef_widget, 1, 0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setRowStretch(0, 0)
        layout.setRowStretch(1, 1)
        # noinspection PyArgumentList
        frame = QFrame()
        frame.setLayout(layout)
        self.setCentralWidget(frame)

        if WINDOWS:
            # On Windows with PyQt5 main window must be shown first
            # before CEF browser is embedded, otherwise window is
            # not resized and application hangs during resize.
            self.show()
        # Browser can be embedded only after layout was set up
        self.cef_widget.embedBrowser()
        if LINUX:
            # On Linux with PyQt5 the QX11EmbedContainer widget is
            # no more available. An equivalent in Qt5 is to create
            # a hidden window, embed CEF browser in it and then
            # create a container for that hidden window and replace
            # cef widget in the layout with the container.
            # noinspection PyUnresolvedReferences, PyArgumentList
            self.container = QWidget.createWindowContainer(
                self.cef_widget.hidden_window, parent=self)
            # noinspection PyArgumentList
            layout.addWidget(self.container, 1, 0)

    def closeEvent(self, event):
        # Close browser (force=True) and free CEF reference
        if self.cef_widget.browser:
            self.cef_widget.browser.CloseBrowser(True)
            self.clear_browser_references()

    def clear_browser_references(self):
        # Clear browser references that you keep anywhere in your
        # code. All references must be cleared for CEF to shutdown cleanly.
        self.cef_widget.browser = None


def main():
    check_versions()
    sys.excepthook = cef.ExceptHook
    settings = {}
    if MAC:
        # Issue #442 requires enabling message pump on Mac
        # in Qt example. Calling cef.DoMessageLoopWork in a timer
        # doesn't work anymore.
        settings["external_message_pump"] = True
    cef.Initialize(settings)
    app = QtCefApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.activateWindow()
    main_window.raise_()
    app.exec_()
    if not cef.GetAppSetting("external_message_pump"):
        app.stopTimer()
    del main_window  # Just to be safe, similarly to "del app"
    del app  # Must destroy app object before calling Shutdown
    cef.Shutdown()


if __name__ == "__main__":
    main()
