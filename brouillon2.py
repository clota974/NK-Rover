from smbus2 import SMBus, i2c_msg

VCNL4040_ADDR = 0x60
bus = SMBus(1)

"""
def i2c_write_byte(data):
    bus.write_byte(0x60,0x04)
    data=bus.read_i2c_block_data(0x60, 0, 2)
    return data
"""

def setLedCurrent():
    led_i_mask = ~((1 << 2) | (1 << 1) | (1 << 0))
    currentValue = (1 << 2) | (1 << 1) | (1 << 0)
    currentValue = 0
    bitmask(0x04, True, led_i_mask, currentValue)

def readCommand(cmdCode):
    bus.write_byte(0x60, cmdCode)
    data = bus.read_byte_data(0x60, 0, 1)
    return data

def readCommandLower(cmdCode):
    return False

def readCommandUpper(cmdCode):
    commandValue = readCommand(cmdCode)
    return (commandValue >> 8)

def writeCommand(cmdCode, value):
    data = [(value & 0xFF), (value >> 8)]
    bus.write_i2c_block_data(0x60, cmdCode, data)

def writeCommandUpper(cmdCode, newValue):
    cmdValue = readCommand(cmdCode)
    cmdValue &= 0x00FF
    cmdValue |= newValue << 8
    return writeCommand(cmdCode, cmdValue)

def writeCommandLower(cmdCode, value):
    return False

def bitmask(cmdAddr, isUpper, mask, thing):
    registerContents = None

    if(not isUpper):
        registerContents = readCommandLower(cmdAddr)
    else:
        registerContents = readCommandUpper(cmdAddr)
    
    registerContents &= mask

    registerContents |= thing

    if(isUpper):
        print(writeCommandUpper(cmdAddr, registerContents))
    else:
        writeCommandLower(cmdAddr, registerContents)


setLedCurrent()