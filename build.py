import sys
import os
import subprocess
import time

def check_Py_Version():
    print("the python Version should be at least 3.6")
    print("Here is your version :")
    os.system("python -V")

def install_pip():
    
    try:
        if os.system("python -m pip install --upgrade pip") != 0:
            raise Exception('Have problem when installing pip')
    except Exception as e:
        print(e)
        print("plz try to solve it!")

def install_pip_plugin():
    try:
        if os.system("pip install luadata langid") != 0:
            raise Exception('Have problem when installing pip plugin')
    except Exception as e:
        print(e)
        print("plz try to solve it!")

check_Py_Version()
time.sleep(0.5)
install_pip()
time.sleep(0.5)
install_pip_plugin()
time.sleep(0.5)

print("Eveything is good to go")