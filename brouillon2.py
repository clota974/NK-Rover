import time 
import sys

for i in range(10):
    print('\r'+str(i), end='')
    time.sleep(0.5)
    sys.stdout.flush()