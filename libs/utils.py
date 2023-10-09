from pathlib import Path
import sys
import os


SOURCEPATH = Path(__file__).parents[1]

def source_path(path):
    return os.path.abspath(os.path.join(SOURCEPATH, path))

def pyinstaller_path(path):
    bundlepath = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    return os.path.abspath(os.path.join(bundlepath, path))
