import struct
import time
import usb_hid


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
        self.last_report = bytearray(2)

    def update(self):
        pass

    def info(self):
        print(f"Usage Page: {self.device.usage_page}",
              f"Usage: {self.device.usage}",
              sep="\n"
              )


gamepad = GamePad()

gamepad.info()
