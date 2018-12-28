# pylint: disable=import-error
from smbus2 import SMBusWrapper
import os

clear = lambda: os.system('clear')

while True:
    with SMBusWrapper(1) as bus:
        # Read a block of 16 bytes from address 80, offset 0
        clear()
        block = bus.read_i2c_block_data(0x60, 0, 16)
        # Returned value is a list of 16 bytes
        print(block)