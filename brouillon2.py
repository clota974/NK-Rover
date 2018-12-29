from smbus2 import SMBus, i2c_msg
from time import sleep

VCNL4040_ADDR = 0x60
bus = SMBus(1)

"""
def i2c_write_byte(data):
    bus.write_byte(0x60,0x04)
    data=bus.read_i2c_block_data(0x60, 0, 2)
    return data
"""

def setLedCurrent():
    mask = ~((1 << 2) | (1 << 1) | (1 << 0))
    currentValue = (1 << 2) | (1 << 1) | (1 << 0)
    bitmask(0x04, True, mask, currentValue)

def setIRDutyCycle():
    mask = ~((1 << 7) | (1 << 6))
    currentValue = 0
    bitmask(0x03, False, mask, currentValue)

def setProxIntegrationTime():
    mask = ~((1 << 3) | (1 << 2) | (1 << 1))
    currentValue = 0
    bitmask(0x03, False, mask, currentValue)

def setProxResolution():
    mask = ~((1 << 3))
    currentValue = (1 << 3)
    bitmask(0x03, True, mask, currentValue)

def enableSmartPersistance():
    mask = ~((1 << 4))
    currentValue = (1 << 1)
    bitmask(0x04, False, mask, currentValue)

def powerOnProximity():
    mask = ~((1 << 0))
    currentValue = 0
    bitmask(0x03, False, mask, currentValue)


def getProximity():
    print("entering")
    while True:
        print("enter2")
        print(readCommand(0x08))

        sleep(0.1)



def readCommand(cmdCode):
    bus.write_byte(0x60, cmdCode)
    data = bus.read_byte_data(0x60, 0, 1)
    return data

def readCommandLower(cmdCode):
    commandValue = readCommand(cmdCode)
    return (commandValue & 0xFF)

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

def writeCommandLower(cmdCode, newValue):
    cmdValue = readCommand(cmdCode)
    cmdValue &= 0xFF00
    cmdValue |= newValue 
    return writeCommand(cmdCode, cmdValue)


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
setIRDutyCycle()
setProxIntegrationTime()
setProxResolution()
enableSmartPersistance()
powerOnProximity()
getProximity()