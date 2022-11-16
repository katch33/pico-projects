from machine import Pin
from time import sleep

interrupt_flag = 0
A = Pin(12, Pin.IN, Pin.PULL_UP)
B = Pin(13, Pin.IN, Pin.PULL_UP)
X = Pin(14, Pin.IN, Pin.PULL_UP)
Y = Pin(15, Pin.IN, Pin.PULL_UP)
def callbacka(A):
    global interrupt_flag
    interrupt_flag=1
def callbackb(B):
    global interrupt_flag
    interrupt_flag=2
def callbackx(X):
    global interrupt_flag
    interrupt_flag=3
def callbacky(Y):
    global interrupt_flag
    interrupt_flag=4
A.irq(trigger=Pin.IRQ_FALLING, handler=callbacka)
B.irq(trigger=Pin.IRQ_FALLING, handler=callbackb)
X.irq(trigger=Pin.IRQ_FALLING, handler=callbackx)
Y.irq(trigger=Pin.IRQ_FALLING, handler=callbacky)

while True:
        
    if interrupt_flag is 1:
        print("Button A")
        sleep(0.1)
        interrupt_flag=0
    if interrupt_flag is 2:
        print("Button B")
        sleep(0.1)
        interrupt_flag=0
    if interrupt_flag is 3:
        print("Button X")
        sleep(0.1)
        interrupt_flag=0
    if interrupt_flag is 4:
        print("Button Y")
        sleep(0.1)
        interrupt_flag=0
    print("Nothing happening here")
    sleep(1)
