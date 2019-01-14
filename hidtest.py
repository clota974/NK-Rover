import os, sys, datetime, colored
from time import sleep
from io import FileIO

report_fd = os.open("/dev/input/js1", os.O_RDWR | os.O_NONBLOCK)
fd = FileIO(report_fd, "rb+", closefd=False)

defBuf = bytearray(230)

while True:
    buf = defBuf 
    r = fd.readinto(buf)
    key = []
    arr = []
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
        val = format((buf[i+1]<<2*4)+buf[i], "06d")
        if(i in key):
            arr.append(colored.fg("light_gray")+str(i)+":"+colored.attr("reset"))
            arr.append(colored.bg("green")+val+colored.attr("reset"))
        else:
            arr.append(val)
        
        i+=2


    p = ' '.join(arr)
    p = p.replace("\r", "")
    print("\r"+p, end="") 
    print()
    print()
    sleep(0.1)
    sys.stdout.flush()