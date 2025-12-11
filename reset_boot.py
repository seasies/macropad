import os
import microcontroller

# Delete boot.py
os.remove("boot.py")

# Reboot the board
microcontroller.reset()
