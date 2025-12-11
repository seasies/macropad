# Macropad

Custom macro configurations for the [Adafruit MACROPAD RP2040](https://www.adafruit.com/product/5128) running CircuitPython.

## Setup

1. Install CircuitPython on your MACROPAD
2. Copy `secrets.py.sample` to `secrets.py` and add your passwords:
   ```bash
   cp macros/secrets.py.sample macros/secrets.py
   # Edit macros/secrets.py with your passwords
   ```
3. Deploy to the macropad:
   ```bash
   just deploy
   ```

## Deployment

Requires [just](https://github.com/casey/just) command runner.

| Command | Description |
|---------|-------------|
| `just deploy` | Deploy all files to the macropad |
| `just deploy-macros` | Deploy only the macros folder (faster) |
| `just reset` | Deploy reset_boot.py to re-enable USB storage |
| `just watch` | Auto-deploy on file changes |

The macropad mounts at `/media/alsobrsp/CIRCUITPY/`.

## Macro Files

Macros are stored in the `macros/` folder. Each file defines a macro set that can be selected using the rotary encoder.

### Included Macros

- **media.py** - Media playback controls
- **numpad.py** - Numeric keypad
- **linux-firefox.py** - Firefox shortcuts
- **security.py** - Password entry (uses secrets.py)
- **off.py** - Blank/off state

### Creating a Macro

Each macro file must export an `app` dict:

```python
from adafruit_hid.keycode import Keycode

app = {
    'name': 'My Macros',
    'macros': [
        # (LED color, Label, Key sequence)
        (0xFF0000, 'Cut', [Keycode.CONTROL, Keycode.X]),
        (0x00FF00, 'Copy', [Keycode.CONTROL, Keycode.C]),
        (0x0000FF, 'Paste', [Keycode.CONTROL, Keycode.V]),
        # ... up to 12 keys + encoder button
    ]
}
```

### Key Sequence Types

- **Positive int**: Key press (e.g., `Keycode.A`)
- **Negative int**: Key release (e.g., `-Keycode.SHIFT`)
- **String**: Type text (e.g., `'Hello'`)
- **Float**: Delay in seconds (e.g., `0.5`)
- **List**: Consumer control codes (media keys)
- **Dict**: Mouse actions

## Boot Configuration

- **boot.py** - Disables USB mass storage for security, keeps REPL enabled
- **reset_boot.py** - Use `just reset` to restore USB mass storage access
