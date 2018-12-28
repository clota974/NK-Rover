with SMBusWrapper(1) as bus:
    # Write a block of 8 bytes to address 80 from offset 0
    data = [0x89,0x08]

    bus.write_i2c_block_data(0x60, 0, data)
with SMBusWrapper(1) as bus:
    # Write a block of 8 bytes to address 80 from offset 0
    data = [0x40,0x08]
    bus.write_i2c_block_data(0x60, 0, data)