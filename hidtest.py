import os, sys
from time import sleep
from io import FileIO

report_fd = os.open("/dev/input/js1", os.O_RDWR | os.O_NONBLOCK)
fd = FileIO(report_fd, "rb+", closefd=False)

defBuf = bytearray(214)

while True:
    buf = defBuf 
    r = fd.readinto(buf)
    p = ' '.join(format(x, '02x') for x in buf)
    print("\r"+p, end="") 
    sleep(0.2)
    sys.stdout.flush()