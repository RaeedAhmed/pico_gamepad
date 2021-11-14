# pico_gamepad

## Installation

### Hard Reset
- Unplug the pico from power
- While holding the BOOTSEL button, plug in the pico
- Release BOOTSEL when `RPI-RP2` disk is mounted
- Download RPi Pico [Flash Reset](https://cdn-learn.adafruit.com/assets/assets/000/099/419/original/flash_nuke.uf2?1613329170)
- Copy Reset UF2 file to pico, which will then automatically reboot and mount

### CircuitPython
- Download the latest [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/)
- Copy the downloaded UF2 file to the pico mounted disk
- Pico will reboot and be mounted as `CIRCUITPY` device

### Program Files
- Copy `boot.py` to pico mounted device in the root directory.
  - Serial output should read 'Gamepad enabled'
- Copy `code.py` to pico
  - Serial output should read 'Gamepad found'
