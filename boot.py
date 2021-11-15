import usb_hid

"""
Packet Structure
----------------
Byte 0: 8x 1-bit buttons
Byte 1: 3x 1-bit buttons + 4-bit hat switch + 1x redundant bit
"""

REPORT_DESCRIPTOR = bytes((
    0x05, 0x01,  # Usage Page (Generic Desktop Controls)
    0x09, 0x05,  # Usage (Game Pad)
    0xA1, 0x01,  # Collection (Application)
    # Buttons
    0x05, 0x09,  # Usage Page (Buttons)
    0x19, 0x01,  # Usage Minimum (Button 1)
    0x29, 0x0B,  # Usage Maximum (Button 11)
    0x15, 0x00,  # Logical Minimum (0)
    0x25, 0x01,  # Logical Maximum (1)
    0x95, 0x0B,  # Report Count (11)
    0x75, 0x01,  # Report Size (1)
    0x81, 0x02,  # Input (Data, Var, Abs)
    # Hat Switch (Joystick)
    0x09, 0x39,  # Usage (Hat switch)
    0x15, 0x00,  # Logical Minimum (0)
    0x25, 0x07,  # Logical Maximum (7)
    0x35, 0x00,  # Physical Minimum (0)
    0x46, 0x3B, 0x01,  # Physical Maximum (315)
    0x65, 0x14,  # English Rotation: Angular Position
    0x95, 0x03,  # Report Count (1)
    0x75, 0x01,  # Report Size (4)
    0x81, 0x42,  # Input (Data, Var, Abs, Null State)
    # Redundant Bit
    0x95, 0x01,  # Report Count (1)
    0x75, 0x01,  # Report Size (1)
    0x81, 0x03,  # Input (Cnst, Var, Abs)
    0xC0,  # End Collection
))

gamepad = usb_hid.Device(
    report_descriptor=REPORT_DESCRIPTOR,
    usage_page=0x01,  # Generic
    usage=0x05,  # Gamepad
    report_ids=(0,),  # No report IDs in descriptor
    in_report_lengths=(2,),  # Send 2 bytes of data
    out_report_lengths=(0,),  # No expected received bytes
)

usb_hid.enable((gamepad,))