import sys
from cefpython3.cefpython_py36 import JavascriptCallback
from cefpython3 import cefpython as cef


def ToBindMethod(method):
    def wrapper(*argv, **kwargs):
        try:
            last_param_type = argv[argv.__len__() - 1]
            if isinstance(last_param_type, JavascriptCallback):
                value = method(*argv[:-1], **kwargs)
                argv[-1].Call(value)
            else:
                value = method(*argv, **kwargs)
            print("call method" + method.__name__ + " argv:" + str(argv)
                  + " kwargs:" + str(**kwargs)
                  + "return value:" + str(value))
            return value
        except Exception as e:
            print(e)
            last_param_type = argv[argv.__len__() - 1]
            if isinstance(last_param_type, JavascriptCallback):
                argv[-1].Call(None, str(e))
            return "error values"

    return wrapper


## 尽量做成两个部分。一个是模块。一个是方法.
## 好像没办法调用。那就只能直接全局名字注册。。
## 注入是最好的。没办法注入就做跳表做添加。。。

class ModuleBase(object):
    def __init__(self):
        pass

    def invoke(self, method_name, *args, **kwargs):
        return self.__getattribute__(method_name)(*args, **kwargs)


class ModuleRegister:
    def __init__(self):
        self.ModuleMap = {}
        self.ModuleList = []

    def registry(self, obj):
        self.ModuleList.append(obj)

    def wrapperModule(self, module):
        return module

    def bindToJavascript(self, bindings):
        for module in self.ModuleList:
            bindings.SetObject(module.__class__.__name__, self.wrapperModule(module))
