import RPi.GPIO as GPIO
import os, sys, datetime, colored
from time import sleep
from io import FileIO

pwma = 27
ain2 = 18
ain1 = 17
bin1 = 15
bin2 = 14
pwmb = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup([ain2,ain1,bin1,bin2,pwma,pwmb], GPIO.OUT)

_pwma = GPIO.PWM(pwma, 980)
_pwmb = GPIO.PWM(pwmb, 980)


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

    if(data[0]>1 or data[1]>1 or data[0]<0 or data[1]<0):
        print("\rError",end="")
        continue

    p = ' '.join(format(x,"06d") for x in data)
    #print("\r"+p, end="") 
    print("\r",p, end="\r")
    sys.stdout.flush()



    speed = int(data[19]/0x7fff*100)
    side = int(data[14]/0x7fff*50)+50


    if(speed<0):
        speed*=-1

        GPIO.output(ain1, 1)
        GPIO.output(bin1, 1)

        GPIO.output(ain2, 0)
        GPIO.output(bin2, 0)
    elif(speed>0):
        GPIO.output(ain1, 0)
        GPIO.output(bin1, 0)

        GPIO.output(ain2, 1)
        GPIO.output(bin2, 1)
    else:
        GPIO.output(ain1, 1)
        GPIO.output(bin1, 1)

        GPIO.output(ain2, 1)
        GPIO.output(bin2, 1)
    
    left = speed*(side/100)
    right = speed*((100-side)/100)

    _pwma.start(right)
    _pwmb.start(left)

    
    