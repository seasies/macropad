# MACROPAD Hotkeys: Security/Passwords

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from secrets import CREDENTIALS

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Security', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFF0000, CREDENTIALS['R1C1']['name'], [-Keycode.COMMAND, CREDENTIALS['R1C1']['password']]),
        (0x00FF00, CREDENTIALS['R1C2']['name'], [-Keycode.COMMAND, CREDENTIALS['R1C2']['password']]),
        (0x0000FF, CREDENTIALS['R1C3']['name'], [-Keycode.COMMAND, CREDENTIALS['R1C3']['password']]),
#         # 2nd row ----------
        (0xBB0000, CREDENTIALS['R2C1']['name'], [-Keycode.COMMAND, CREDENTIALS['R2C1']['password']]),
        (0x00BB00, CREDENTIALS['R2C2']['name'], [-Keycode.COMMAND, CREDENTIALS['R2C2']['password']]),
        (0x0000BB, CREDENTIALS['R2C3']['name'], [-Keycode.COMMAND, CREDENTIALS['R2C3']['password']]),
#         # 3rd row ----------
        (0x770000, CREDENTIALS['R3C1']['name'], [-Keycode.COMMAND, CREDENTIALS['R3C1']['password']]),
        (0x007700, CREDENTIALS['R3C2']['name'], [-Keycode.COMMAND, CREDENTIALS['R3C2']['password']]),
        (0x000077, CREDENTIALS['R3C3']['name'], [-Keycode.COMMAND, CREDENTIALS['R3C3']['password']]),
#         # 4th row ----------
        (0x330000, CREDENTIALS['R4C1']['name'], [-Keycode.COMMAND, CREDENTIALS['R4C1']['password']]),
        (0x003300, CREDENTIALS['R4C2']['name'], [-Keycode.COMMAND, CREDENTIALS['R4C2']['password']]),
        (0x000033, CREDENTIALS['R4C3']['name'], [-Keycode.COMMAND, CREDENTIALS['R4C3']['password']]),
#         # Encoder button ---
        (0x000000, CREDENTIALS['ENCODER']['name'], [-Keycode.COMMAND, CREDENTIALS['ENCODER']['password']]),
    ]
}

