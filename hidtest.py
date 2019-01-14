import os, sys
from time import sleep
from io import FileIO

report_fd = os.open("/dev/input/js1", os.O_RDWR | os.O_NONBLOCK)
fd = FileIO(report_fd, "rb+", closefd=False)

defBuf = bytearray(214)

while True:
    buf = defBuf 
    r = fd.readinto(buf)
    sys.stdout.write("\r" + (' '.join(format(x, '02x') for x in buf) )) 
    sys.flush()
    sleep(0.2)