import importlib
import pkgutil


def import_submodules(package, recursive=True):
    """ Import all submodules of a module, recursively, including subpackages

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name))
    return results


def transformDict(ODict):
    NDict = {}
    for key in ODict.keys():
        NDict[key.decode()] = ODict[key].decode()
    return NDict


def putIfNotExists(env, key, value):
    if key not in env.keys():
        env[key] = value
    return env


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")
