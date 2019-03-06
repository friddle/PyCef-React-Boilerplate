from src.framework.libs.util import ToBindMethod, ModuleBase


class HelloWorld(ModuleBase):
    def __init__(self):
        self.times = 0

    @ToBindMethod
    def hello(self):
        self.times = self.times + 1
        return "Hello From Python Backend times " + str(self.times)

    @ToBindMethod
    def hello_from_sqlite(self):
        return "hello from sqlite"

    @ToBindMethod
    def hello_from_http(self):
        return "hello from http"

    @ToBindMethod
    def hello_from_http(self):
        return "hello from os"
