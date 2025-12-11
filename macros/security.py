# MACROPAD Hotkeys: Security/Passwords

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from secrets import CREDENTIALS

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Security', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFFFF00, CREDENTIALS['P1']['name'], [-Keycode.COMMAND, CREDENTIALS['P1']['password']]),
        (0x000000, ' ', [-Keycode.COMMAND, '']),
        (0x000000, ' ', [-Keycode.COMMAND, '']),
#         # 2nd row ----------
        (0x0000FF, CREDENTIALS['P2']['name'], [-Keycode.COMMAND, CREDENTIALS['P2']['password']]),
        (0x00FF00, CREDENTIALS['P3']['name'], [-Keycode.COMMAND, CREDENTIALS['P3']['password']]),
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

