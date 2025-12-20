# Macropad

Custom macro configurations for the [Adafruit MACROPAD RP2040](https://www.adafruit.com/product/5128) running CircuitPython.

## Setup

1. Install CircuitPython on your MACROPAD
2. Copy `secrets.py.sample` to `secrets.py` and add your credentials:

   ```bash
   cp secrets.py.sample secrets.py
   # Edit secrets.py with your credentials
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
| `just serial-reset` | Send Ctrl-C via serial to re-enable USB storage |
| `just watch` | Auto-deploy on file changes |

The macropad mounts at `/media/alsobrsp/CIRCUITPY/`.

## Macro Files

Macros are stored in the `macros/` folder. Each file defines a macro set that can be selected using the rotary encoder.

### Included Macros

- **media.py** - Media playback controls
- **numpad.py** - Numeric keypad
- **linux-firefox.py** - Firefox shortcuts
- **security.py** - Password entry (uses secrets.py, locked by default)
- **off.py** - Blank/off state

### Security Lock

The security macros page is locked by default to prevent accidental password entry. When locked, the page displays a blank screen with no labels or LEDs.

**To unlock:** Press all 3 bottom row keys (keys 10, 11, 12) simultaneously.

**Auto-lock:** The page automatically locks after 5 minutes of inactivity. Any key press while on the unlocked security page resets the timer.

Configuration in `code.py`:

- `SECURITY_APP_NAME` - Name of the protected app (default: `'Security'`)
- `UNLOCK_KEYS` - Key indices for unlock combo (default: `{9, 10, 11}`, 0-indexed)
- `LOCK_TIMEOUT` - Seconds before auto-lock (default: `300`)

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
- **reset_boot.py** - Deployed with code.py to enable recovery via serial console

### Restoring USB Storage Access

When `boot.py` disables USB mass storage, use `just serial-reset` to regain filesystem access:

```bash
just serial-reset
```

Or manually:

1. Connect to the MACROPAD serial console (e.g., `screen /dev/serial/by-id/usb-Adafruit_Macropad_RP2040_*-if00 115200`)
2. Press `Ctrl-C` to interrupt `code.py`
3. The KeyboardInterrupt handler runs `reset_boot.py`, which deletes `boot.py` and reboots
4. USB mass storage will be re-enabled on next boot
