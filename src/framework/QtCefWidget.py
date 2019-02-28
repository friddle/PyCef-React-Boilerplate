import ctypes
import os
import platform
import sys

# PyQt5
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from cefpython3 import cefpython as cef

WINDOWS = (platform.system() == "Windows")
LINUX = (platform.system() == "Linux")
MAC = (platform.system() == "Darwin")

WindowUtils = cef.WindowUtils()
CefWidgetParent = QWidget


class QtCefWidget(CefWidgetParent):
    def __init__(self, parent=None, url="App.html", module_registry=None, env={}):
        # noinspection PyArgumentList
        super(QtCefWidget, self).__init__(parent)
        self.parent = parent
        self.browser = None
        self.hidden_window = None  # Required for PyQt5 on Linux
        self.url = url
        if not os.path.exists(self.url.replace("file://", "")):
            print("url is not found:" + self.url)
            sys.exit(1)
        self.env = env
        self.module_registry = module_registry
        self.show()
        self.binding = cef.JavascriptBindings()

    def focusInEvent(self, event):
        # This event seems to never get called on Linux, as CEF is
        # stealing all focus due to Issue #284.
        if self.browser:
            if WINDOWS:
                WindowUtils.OnSetFocus(self.getHandle(), 0, 0, 0)
            self.browser.SetFocus(True)

    def focusOutEvent(self, event):
        # This event seems to never get called on Linux, as CEF is
        # stealing all focus due to Issue #284.
        if self.browser:
            self.browser.SetFocus(False)

    def embedBrowser(self):
        if LINUX:
            # noinspection PyUnresolvedReferences
            self.hidden_window = QWindow()
        window_info = cef.WindowInfo()
        rect = [0, 0, self.width(), self.height()]
        window_info.SetAsChild(self.getHandle(), rect)
        self.browser = cef.CreateBrowserSync(window_info, url=self.url)
        self.browser.SetClientHandler(LoadHandler(self.parent.navigation_bar, env=self.env))
        self.browser.SetClientHandler(FocusHandler(self))
        if self.module_registry:
            self.module_registry.bindToJavascript(self.binding)
        if self.binding:
            self.binding.SetProperty("ENV", self.env)
        self.browser.SetJavascriptBindings(self.binding)

    def getHandle(self):
        if self.hidden_window:
            # PyQt5 on Linux
            return int(self.hidden_window.winId())
        try:
            # PyQt4 and PyQt5
            return int(self.winId())
        except:
            # PySide:
            # | QWidget.winId() returns <PyCObject object at 0x02FD8788>
            # | Converting it to int using ctypes.
            if sys.version_info[0] == 2:
                # Python 2
                ctypes.pythonapi.PyCObject_AsVoidPtr.restype = (
                    ctypes.c_void_p)
                ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = (
                    [ctypes.py_object])
                return ctypes.pythonapi.PyCObject_AsVoidPtr(self.winId())
            else:
                # Python 3
                ctypes.pythonapi.PyCapsule_GetPointer.restype = (
                    ctypes.c_void_p)
                ctypes.pythonapi.PyCapsule_GetPointer.argtypes = (
                    [ctypes.py_object])
                return ctypes.pythonapi.PyCapsule_GetPointer(
                    self.winId(), None)

    def moveEvent(self, _):
        self.x = 0
        self.y = 0
        if self.browser:
            if WINDOWS:
                WindowUtils.OnSize(self.getHandle(), 0, 0, 0)
            elif LINUX:
                self.browser.SetBounds(self.x, self.y,
                                       self.width(), self.height())
            self.browser.NotifyMoveOrResizeStarted()

    def resizeEvent(self, event):
        size = event.size()
        if self.browser:
            if WINDOWS:
                WindowUtils.OnSize(self.getHandle(), 0, 0, 0)
            elif LINUX:
                self.browser.SetBounds(self.x, self.y,
                                       size.width(), size.height())
            self.browser.NotifyMoveOrResizeStarted()


class LoadHandler(object):
    def __init__(self, navigation_bar, env):
        self.initial_app_loading = True
        self.navigation_bar = navigation_bar
        self.debug = bool(env.get("DEBUG", "False"))

    def OnLoadingStateChange(self, **_):
        self.navigation_bar.updateState()

    def OnLoadStart(self, browser, **_):
        self.navigation_bar.url.setText(browser.GetUrl())
        if self.initial_app_loading:
            self.navigation_bar.cef_widget.setFocus()
            # Temporary fix no. 2 for focus issue on Linux (Issue #284)
            if LINUX:
                print("[qt.py] LoadHandler.OnLoadStart:"
                      " keyboard focus fix no. 2 (Issue #284)")
                browser.SetFocus(True)
            self.initial_app_loading = False
        if self.debug:
            browser.ShowDevTools()


class FocusHandler(object):
    def __init__(self, cef_widget):
        self.cef_widget = cef_widget

    def OnSetFocus(self, **_):
        pass

    def OnGotFocus(self, browser, **_):
        # Temporary fix no. 1 for focus issues on Linux (Issue #284)
        if LINUX:
            print("[qt.py] FocusHandler.OnGotFocus:"
                  " keyboard focus fix no. 1 (Issue #284)")
            browser.SetFocus(True)
