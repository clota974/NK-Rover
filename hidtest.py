import os, sys
from time import sleep
from io import FileIO

report_fd = os.open("/dev/input/js1", os.O_RDWR | os.O_NONBLOCK)
fd = FileIO(report_fd, "rb+", closefd=False)

defBuf = bytearray(100)

while True:
    buf = defBuf 
    r = fd.readinto(buf)
    p = ' '.join(format(x, '02x') for x in buf)
    p = p.replace("\r", "")
    print("\r"+p, end="") 
    sleep(0.1)
    sys.stdout.flush()