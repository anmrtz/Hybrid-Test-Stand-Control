import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
               Executable('HybridEngineController.py',
                          icon="icon.ico",
                          base=base)
]
includefiles = ["icon.ico"]

setup(name='Hybrid Engine Controller',
      version='0.0',
      description='Engine Controller',
      author = "Anar Kazimov",
      options = {'build_exe': {'include_files':includefiles}},
      executables=executables
      )
