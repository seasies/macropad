# MACROPAD Hotkeys: Security/Passwords

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from secrets import PASSWORDS

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Security', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFFFF00, 'P1', [-Keycode.COMMAND, PASSWORDS['P1'] + '\n']),
        (0x000000, ' ', [-Keycode.COMMAND, '']),
        (0x000000, ' ', [-Keycode.COMMAND, '']),
#         # 2nd row ----------
        (0x0000FF, 'P2', [-Keycode.COMMAND, PASSWORDS['P2'] + '\n']),
        (0x00FF00, 'P3', [-Keycode.COMMAND, PASSWORDS['P3'] + '\n']),
        (0x000000, ' ', [-Keycode.COMMAND, '']),
#         # 3rd row ----------
        (0x000000, ' ', [-Keycode.COMMAND, '']),
        (0x000000, ' ', [-Keycode.COMMAND, '']),
        (0x000000, ' ', [-Keycode.COMMAND, '']),
#         # 4th row ----------
        (0x000000, ' ', [-Keycode.COMMAND, '']),
        (0x000000, ' ', [-Keycode.COMMAND, '']),
        (0x000000, ' ', [-Keycode.COMMAND, '']),
#         # Encoder button ---
        (0x000000, ' ', [-Keycode.COMMAND, '']),
    ]
}

