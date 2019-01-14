import os, sys, datetime
from time import sleep
from io import FileIO

report_fd = os.open("/dev/input/js1", os.O_RDWR | os.O_NONBLOCK)
fd = FileIO(report_fd, "rb+", closefd=False)

defBuf = bytearray(214)

while True:
    buf = defBuf 
    r = fd.readinto(buf)
    arr = []
    sign = buf[2]
    print("Sign = ", sign)

    for i in buf:
        try:
            if(buf[i]==sign and buf[i+1]==0):
                arr.append(buf[i+2]) 
                arr.append(buf[i+3]) 
        except:
            pass

    print(len(arr))
    p = ' '.join(format(x, '02x') for x in arr)
    p = p.replace("\r", "")
    print("\r"+p, end="") 
    sleep(0.1)
    sys.stdout.flush()