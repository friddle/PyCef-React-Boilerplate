import os
import importlib

from src.framework.libs.util import ToBindMethod, ModuleBase


class PySys(ModuleBase):
    def __init__(self):
        pass

    @ToBindMethod
    def env(self, key):
        return os.environ[key]

    @ToBindMethod
    def invoke(self, package, method, *args, **kwargs):
        lib = importlib.__import__(package)
        return lib

