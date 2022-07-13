import pystray
import os
import sys
from pystray import MenuItem as item
from PIL import Image

def on_quit():
    icon.visible = False
    icon.stop()
    
image = Image.open("icon.png")
#python3 -m venv .venv
#source ./.venv/bin/activate
#pip install pystray
# path to that folder with your game shortcuts
current_dir = os.getcwd()
dir_path = current_dir +'//GameFiles'
#list with that stored files
res = []

for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        # add it to the list
        res.append(os.path.basename(path).split('.')[0])
        

menu = []
count = 0
# create menu with all files
for x in res:
    menu.append(item(x,lambda icon, item: os.startfile(dir_path + "\\" + item.text)))
    count += 1
        
menu.append(item("Quit", on_quit))


icon = pystray.Icon("GameOpener", image, "GameOpener", menu)
icon.run()
