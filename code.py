import struct
import time
import usb_hid
import board
import digitalio
from adafruit_debouncer import Debouncer


class GamePad:
    def __init__(self) -> None:
        pad = None
        while True:
            for dev in usb_hid.devices:
                if dev.usage_page == 1 and dev.usage == 5:
                    pad = dev
            if pad:
                self.device = pad
                print("Gamepad found")
                break
            time.sleep(0.2)
        self.report = bytearray(2)
        self.prev_report = bytearray(2)
        self.button_states = 0
        self.hat_pos = 0

    def update(self):
        struct.pack_into("<BB",  # format of bytes
                         self.report,  # buffer to fill
                         0,  # offset
                         self.button_states,
                         self.hat_pos  # data sources
                         )
        if self.prev_report != self.report:
            print(self.report)
            self.device.send_report(self.report, None)
            self.prev_report[:] = self.report

    def info(self):
        print(f"Usage Page: {self.device.usage_page}",
              f"Usage: {self.device.usage}",
              sep="\n"
              )


def create_button(pin) -> Debouncer:
    button = digitalio.DigitalInOut(pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
    return Debouncer(button, 0)


gamepad = GamePad()

gamepad.info()

button_pins = [getattr(board, f"GP{pin}") for pin in range(2, 13)]

buttons = [create_button(pin) for pin in button_pins]

clicks = 0
while True:
    for i, button in enumerate(buttons):
        button.update()
        if button.fell:
            clicks += 1
            print(f"Button {i} fell")
            print(clicks)
            gamepad.button_states |= 1 << i
        if button.rose:
            print(f"Button {i} rose")
            gamepad.button_states &= ~(1 << i)
        gamepad.update()
