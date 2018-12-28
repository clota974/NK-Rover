from smbus2 import SMBusWrapper
from time import sleep

former = None

while True:
    with SMBusWrapper(1) as bus:
        sleep(0.01)

        # Read a block of 16 bytes from address 80, offset 0
        block = bus.read_i2c_block_data(0x60, 0, 16)

        if former==block:
            continue

        former = block
        # Returned value is a list of 16 bytes
        print '[{}]'.format(', '.join(hex(x) for x in block))