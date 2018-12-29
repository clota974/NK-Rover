from smbus2 import SMBus, i2c_msg, SMBusWrapper

bus = SMBus(1)
bus.write_byte(0x60,0x04)
data=bus.read_i2c_block_data(0x60, 0, 2)
print(data)