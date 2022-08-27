import os
import time
from pynput.keyboard import Key, Controller

os.system("open -a Messages")

time.sleep(4)

keyboard = Controller()

keyboard.type("hi how are you")
keyboard.press(Key.enter)