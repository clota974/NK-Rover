import time 
import sys

for i in range(10):
    buf = [1,2,3,4,5,i]
    p = ' '.join(format(x, '02x') for x in buf)
    print("\r"+p+"\n"+p, end="") 
    time.sleep(0.5)
    sys.stdout.flush()