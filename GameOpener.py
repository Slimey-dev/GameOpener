import pystray
import os
from pystray import MenuItem as item
from PIL import Image

def on_quit():
    icon.visible = False
    icon.stop()
    
image = Image.open("icon.png")

menu = (
    # you can add more items for more games
    item('Game of your choice', lambda: os.startfile("C:\Path\to\that\file\that_file.exe")),
    item('Quit', on_quit)
    )

icon = pystray.Icon("GameOpener", image, "GameOpener", menu)
icon.run()
