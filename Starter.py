from genericpath import exists
import os
import sys
import subprocess

current_dir = os.getcwd()

i = False

os.chdir(current_dir)

if os.path.isdir(current_dir + "/.venv") == True:
    if sys.platform.startswith('linux'):
        os.system('.venv/bin/python3 GameOpener.py')
    if sys.platform.startswith('win32'):
        subprocess.run('./.venv/Scripts/pythonw GameOpener.py')
        
if exists(current_dir + '/oldpath.txt') == False:
    with open(current_dir + '/oldpath.txt', 'w') as f:
        f.write('ano')

with open("oldpath.txt", "r") as file:
    line = file.readline()




if os.path.isdir(current_dir + '/.venv') == False and line == current_dir and exists(current_dir + '/oldpath.txt') == True:
    i = True
    if sys.platform.startswith('win32'):
        subprocess.run('python -m venv .venv')
        subprocess.run('./.venv/Scripts/python -m pip install pystray')
    if sys.platform.startswith('linux'):
        os.system('python3 -m venv .venv')
        os.system('.venv/bin/pip3 install pystray')
        os.system('.venv/bin/pip3 install PyGObject')

if line != current_dir and exists(current_dir + '/oldpath.txt') == True:
    i = True
    if sys.platform.startswith('win32'):
        subprocess.run('del .venv')
        subprocess.run('python -m venv .venv')
        subprocess.run('./.venv/Scripts/python -m pip install pystray')
    if sys.platform.startswith('linux'):
        os.system('rm -rf .venv')
        os.system('python3 -m venv .venv')
        os.system('.venv/bin/pip3 install pystray')
        os.system('.venv/bin/pip3 install PyGObject')

with open(current_dir + '/oldpath.txt', 'w') as f:
    f.write(current_dir)
    
if len(sys.argv) == 1 and i == True:
    print('running')
    os.execl(sys.executable, 'python', __file__, "1")