import pystray
import os
from pystray import MenuItem as item
from PIL import Image

def on_quit():
    icon.visible = False
    icon.stop()
    
image = Image.open("icon.png")

menu = (
    item('Ready or Not', lambda: os.startfile("C:\Program Files (x86)\Steam\steamapps\common\Ready Or Not\ReadyOrNot.exe")),
    item('Quit', on_quit)
    )

icon = pystray.Icon("GameOpener", image, "GameOpener", menu)
icon.run()
