import os, sys, datetime, colored
from time import sleep
from io import FileIO

report_fd = os.open("/dev/input/js1", os.O_RDWR | os.O_NONBLOCK)
fd = FileIO(report_fd, "rb+", closefd=False)

defBuf = bytearray(230)

while True:
    sleep(0.1)
    buf = defBuf 
    r = fd.readinto(buf)
    key = []
    arr = []
    data = []
    sign = buf[2]

    i = 0
    while i < len(buf):
        try:
            if(buf[i]==sign and buf[i+1]==0):
                key.append(i+2) 
                key.append(i+3) 
        except Exception as e:
            pass

        i+=1
    
    if len(key)<5:
        continue

    i = 0
    while i < len(buf):
        val = (buf[i+1]<<2*4)+buf[i]

        if(val & 0x8000 > 0): # If negative
            val -= 0x10000

        arr.append(val)
        if(i in key):
            arr.append(colored.bg("green")+format(val, "=+5d")+colored.attr("reset"))
            data.append(val)
        else:
            arr.append(val)
        
        i+=2

    if(data[0]>1 or data[1]>1):
        print("\rError",end="")
        continue

    p = ' '.join(format(x,"02x") for x in data)
    #print("\r"+p, end="") 
    print("\r",p, end="\r")
    
    sys.stdout.flush()