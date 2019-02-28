import os

from src.framework.jswrapper.util import ToBindMethod, ModuleBase


class PySys(ModuleBase):
    def __init__(self):
        pass

    @ToBindMethod
    def env(self, key):
        return os.environ[key]



