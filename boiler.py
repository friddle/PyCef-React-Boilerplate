#!/usr/bin/python3
# -*- coding: UTF-8 -*-
### 一个BuildTools。完成所有的功能

import argparse
import os
import sys
import shutil
import subprocess as subp
import time

###Check Name and Version

tool_names = ["node", "yarn"]
python_libs = ["venv"]
project_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(project_path)
tools = {}
PORT = 1314
DEBUG = True


def check_env():
    print("check env")
    for tool_name in tool_names:
        tool_location = shutil.which(tool_name)
        if tool_location is None:
            print("tool " + tool_name + " not found,please make sure you have installed,check README.md")
            exit(1)
        tools[tool_name] = tool_location
    for lib in python_libs:
        module = __import__(lib)
        if module is None:
            print("python lib " + lib + " not found,please sure make install")

    if shutil.which("tyarn") is not None:
        tools["yarn"] = shutil.which("tyarn")


def build_virtualenv():
    print("build virtualenv")
    import venv
    if not os.path.exists("venv"):
        venv.create("venv", with_pip=True, system_link=True, system_site_packages=True)

    env_path = os.path.join(project_path, "venv")
    activate_this_file = os.path.join(env_path, "./bin/activate_this.py")
    exec(open(activate_this_file).read(), {'__file__': activate_this_file})
    tools["pip"] = os.path.join(env_path, "bin/pip")
    tools["pip3"] = os.path.join(env_path, "bin/pip")
    tools["python"] = os.path.join(env_path, "bin/python")
    tools["python3"] = os.path.join(env_path, "bin/python3")


def build_python():
    print("build python")
    data = os.system(tools["pip"] + " install -r requirements.txt")
    print("build python success")


def build_nodejs():
    print("build nodejs")
    data = os.system(tools["yarn"] + " install")
    print("build nodejs success")


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


def run_node_js():
    print("run nodejs")
    if DEBUG:
        p = subp.Popen([tools["yarn"], "run", "start-render-dev"], shell=False, stdout=subp.PIPE, stderr=subp.PIPE)
        times = 0
        returncode = p.poll()
        while returncode is None:
            line = p.stdout.readline()
            returncode = p.poll()
            line = line.strip()
            if 'webpack' in str(line):
                break
    else:
        os.system(tools["yarn"] + " run build-renderer")


def run_web_backend():
    print("run backend")
    if os.getenv("PYTHONPATH") is None:
        os.putenv("PYTHONPATH", project_path)
    else:
        os.putenv("PYTHONPATH", os.getenv("PYTHONPATH") + ":" + project_path)
    script_file = os.path.join(project_path, "./src/Main.py")
    subp.Popen([tools["python3"], script_file])


def build():
    check_env()
    build_virtualenv()
    build_python()
    build_nodejs()


def package():
    pass


def update():
    check_env()
    build_virtualenv()
    build_python()
    build_nodejs()


def run():
    DEBUG = False
    check_env()
    build_virtualenv()
    run_node_js()
    run_web_backend()


def runDebug():
    DEBUG = True
    check_env()
    os.putenv("DEBUG", "True")
    os.putenv("PORT", str(PORT))
    build_virtualenv()
    run_node_js()
    run_web_backend()


parser = argparse.ArgumentParser(description='Action Run As Package')
parser.add_argument('action', action='store', help='操作行为',
                    choices=["check", "package", "update", "build", "run", "run-debug"],
                    default="check")

results = parser.parse_args(sys.argv[1:])
action = results.action

if action == 'check':
    check_env()

if action == 'package':
    package()

if action == 'update':
    update()

if action == 'build':
    build()

if action == 'run':
    run()

if action == 'run-debug':
    runDebug()
