from src.framework.jswrapper.util import ToBindMethod, ModuleBase


class HelloWorld(ModuleBase):
    @ToBindMethod
    def hello(self, text):
        return "from: " + text + "to:" + "world"

    @ToBindMethod
    def hello_from_sqlite(self):
        return "hello from sqlite"

    @ToBindMethod
    def hello_from_http(self):
        return "hello from http"
