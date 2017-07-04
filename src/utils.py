from PIL.ImageTk import PhotoImage
import os
import re
import sys
import tempfile

import res


def reformatPath(path):
    parts = re.split(r'\\|\/', path)
    return os.sep.join(parts)


def homePath():
    return os.path.expanduser("~")


def minecraftPath():
    if sys.platform == 'win32' or sys.platform == 'cygwin':
        return os.path.join(homePath(), 'AppData/Roaming/.minecraft')
    elif sys.platform == 'darwin':
        return os.path.join(homePath(), 'Library/Application Support/minecraft')
    else:
        return  os.path.join(homePath(), '.minecraft')


def tempPath(fileName = None):
    if not os.path.isdir(tempfile.gettempdir()):
        os.mkdir(tempfile.gettempdir())
    if fileName:
        return os.path.join(tempfile.gettempdir(), fileName)
    return tempfile.gettempdir()


def removeFile(filePath):
    try:
        os.remove(filePath)
    except Exception as e:
        print("The file " + filePath + " could not be removed.")


def image(name):
    return PhotoImage(data=res.read(name))