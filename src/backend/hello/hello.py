from src.framework.libs.util import ToBindMethod, ModuleBase


class HelloWorld(ModuleBase):
    @ToBindMethod
    def hello(self):
        return "Hello From Python Backend"

    @ToBindMethod
    def hello_from_sqlite(self):
        return "hello from sqlite"

    @ToBindMethod
    def hello_from_http(self):
        return "hello from http"

    @ToBindMethod
    def hello_from_http(self):
        return "hello from os"
