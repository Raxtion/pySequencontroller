import sys
from cx_Freeze import setup, Executable

build_exe_options = {'optimize':2, 'includes':['pySequencontroller.py', 'fileSaveDialog.py', 'Form1.py', 'Form2.py',
                                               'Form3.py', 'windows_logo.png',
                                               'README.txt']}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable(script='pySequencontroller.py',
               base=base,
               targetName='pySequencontroller.exe',
               compress=True,
               icon='windows_logo.ico')]

setup(name='pySequencontroller',
      version='0.1',
      description='The Qt5 GUI app for dealing with bio-string, like DNA or RNA, written in python3',
      executables=executables,
      options={'build.exe': build_exe_options}
      )
