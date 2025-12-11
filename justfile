# Macropad deployment recipes

CIRCUITPY := "/media/alsobrsp/CIRCUITPY"
SERIAL_PATTERN := "/dev/serial/by-id/usb-Adafruit_Macropad_RP2040_*"

# Default recipe - show available commands
default:
    @just --list

# Deploy all files to the macropad
deploy: check-mount
    cp boot.py {{CIRCUITPY}}/
    cp code.py {{CIRCUITPY}}/
    cp reset_boot.py {{CIRCUITPY}}/
    cp secrets.py {{CIRCUITPY}}/
    cp -r macros {{CIRCUITPY}}/
    @echo "Deployed to {{CIRCUITPY}}"

# Deploy only macro files (faster iteration)
deploy-macros: check-mount
    cp -r macros {{CIRCUITPY}}/
    @echo "Macros deployed to {{CIRCUITPY}}"

# Check if the macropad is mounted
check-mount:
    @test -d {{CIRCUITPY}} || (echo "Error: CIRCUITPY not mounted at {{CIRCUITPY}}" && exit 1)

# Reset via serial console to re-enable USB storage
serial-reset:
    #!/usr/bin/env bash
    set -euo pipefail
    SERIAL=$(ls {{SERIAL_PATTERN}} 2>/dev/null | head -1)
    if [[ -z "$SERIAL" ]]; then
        echo "Error: No Macropad serial device found matching {{SERIAL_PATTERN}}"
        exit 1
    fi
    stty -F "$SERIAL" 115200 raw
    printf '\003' > "$SERIAL"
    echo "Sent Ctrl-C to $SERIAL - macropad will reboot with USB storage enabled"

# Watch for changes and auto-deploy macros
watch:
    @echo "Watching for changes in macros/..."
    @while true; do \
        inotifywait -q -e modify -e create -e delete -r macros/; \
        just deploy-macros; \
    done
