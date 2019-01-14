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
        arr.append(val)
        if(i in key):
            arr.append(colored.bg("green")+format(val, "06d")+colored.attr("reset"))
            data.append(val)
        else:
            arr.append(val)
        
        i+=2

    if(data[0]>1 or data[1]>1):
        print("\rError",end="")
        #continue

    p = ' '.join(format(x,"06d") for x in data)
    #print("\r"+p, end="") 
    print("\r",p, end="\r")
    sleep(0.1)
    sys.stdout.flush()