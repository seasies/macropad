# Macropad deployment recipes

CIRCUITPY := "/media/alsobrsp/CIRCUITPY"

# Default recipe - show available commands
default:
    @just --list

# Deploy all files to the macropad
deploy: check-mount
    cp boot.py {{CIRCUITPY}}/
    cp code.py {{CIRCUITPY}}/
    cp -r macros {{CIRCUITPY}}/
    @echo "Deployed to {{CIRCUITPY}}"

# Deploy only macro files (faster iteration)
deploy-macros: check-mount
    cp -r macros {{CIRCUITPY}}/
    @echo "Macros deployed to {{CIRCUITPY}}"

# Check if the macropad is mounted
check-mount:
    @test -d {{CIRCUITPY}} || (echo "Error: CIRCUITPY not mounted at {{CIRCUITPY}}" && exit 1)

# Reset the macropad by copying reset_boot.py
reset: check-mount
    cp reset_boot.py {{CIRCUITPY}}/boot.py
    @echo "Reset boot.py deployed - reconnect the macropad"

# Watch for changes and auto-deploy macros
watch:
    @echo "Watching for changes in macros/..."
    @while true; do \
        inotifywait -q -e modify -e create -e delete -r macros/; \
        just deploy-macros; \
    done
