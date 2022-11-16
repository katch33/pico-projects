from machine import Pin
from time import sleep
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_RGB332
from pimoroni import Button, RGBLED
import random
import qrcode

display = PicoGraphics(display = DISPLAY_PICO_DISPLAY, rotate = 45, pen_type=PEN_RGB332)
#display is 240 x 135

# display.set_backlight(x) where x= 0.0 - 1.0
display.set_backlight(1.0)

#led = Pin(25, Pin.OUT) #used for the onboard pico LED
led = RGBLED(6, 7, 8) #used for the neopixel
# led.set_rgb(r,g,b)

# butt stuff
A = Pin(12, Pin.IN, Pin.PULL_UP)
B = Pin(13, Pin.IN, Pin.PULL_UP)
X = Pin(14, Pin.IN, Pin.PULL_UP)
Y = Pin(15, Pin.IN, Pin.PULL_UP)

interrupt_flag = 0

def callbacka(A):
    global interrupt_flag
    interrupt_flag = 1
    
def callbackb(B):
    global interrupt_flag
    interrupt_flag = 2
    
def callbackx(X):
    global interrupt_flag
    interrupt_flag = 3
    
def callbacky(Y):
    global interrupt_flag
    interrupt_flag = 4
    
A.irq(trigger=Pin.IRQ_FALLING, handler=callbacka)
B.irq(trigger=Pin.IRQ_FALLING, handler=callbackb)
X.irq(trigger=Pin.IRQ_FALLING, handler=callbackx)
Y.irq(trigger=Pin.IRQ_FALLING, handler=callbacky)

# my_pen = display.create_pen(r, g, b) #create a pen colour
# display.set_pen(my_pen) #sets pen colour
# display.clear() #clears to current pen colour
# display.update() # Send the contents of your Pico Graphics buffer to your screen

# display.set_font(font)
# BITMAP FONTS
# bitmap6
# bitmap8
# bitmap14_outline
# VECTOR FONTS
# sans
# gothic
# cursive
# serif_italic
# serif

# display.text(text, x, y, wordwrap, scale, angle, spacing)

# angle applies to vector fonts only
#Text scale can be a whole number (integer) for Bitmap font
# or a decimal (float) for Vector (Hershey) fonts.

WHITE = display.create_pen(255, 255, 255)
RED = display.create_pen(255, 0, 0)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)

# counts asks for help
n = 0

# sets up a handy function we can call to clear the screen
def clear(col):
    display.set_pen(col)
    display.clear()
    display.update()
    
# allows us to blink the RGB LED with a colour and amount of time to stay on
def blink(r, g, b, delay):
    led.set_rgb(r,g,b)
    sleep(delay)
    led.set_rgb(0,0,0)
    
#function that blinks SOS, allows for different colours for each blink and how long the
#LED stays on, and what the PAUSE is between letters, as well as the pen colour for the screen print
def SOS(r, g, b, s_spd, o_spd, pause, interval_spd, PEN_COL):
    display.set_pen(PEN_COL)
    
    for x in range(3):
        blink(r, g, b, s_spd)
        sleep(interval_spd)
    #print S to screen
    display.text("S", 15, 25, 9999, 12)
    display.update()
    
    sleep(pause)
    
    for x in range(3):
        blink(r, g, b, o_spd)
        sleep(interval_spd)
    #print S to screen
    display.text("O", 95, 25, 9999, 12)
    display.update()
    
    sleep(pause)
    
    for x in range(3):
        blink(r, g, b, s_spd)
        sleep(interval_spd)
    #print S to screen
    display.text("S", 175, 25, 9999, 12)
    display.update()
    
    sleep(pause)

# faces
sad = "( O__O )"
blinking = "( -__- )"
question = "? ( @ _ @ ) ?"
happy = "( ^_^)"

while True:
    #clear the screen for start
    clear(BLACK)
    
    display.set_font("bitmap8")
    #SOS(r, g, b, s_spd, o_spd, pause, interval_spd, PEN_COL)
    SOS(20, 0, 20, 0.1, 0.3, 0.3, 0.1, MAGENTA)
    sleep(1)
    
    clear(BLACK)
    
    n += 1
    num = str(n)
    
    display.set_pen(MAGENTA)
    
    #display.text(text, x, y, wordwrap, scale, angle, spacing)
    
    display.text("I must have asked for help " + num + " times by now!", 40, 10, 150, 2, 1, 1)
    display.set_font("serif")
    display.text(sad, 40, 90, 9999, 1, 1, 1)
    display.update()
    sleep(1.0)
    
    clear(BLACK)
    
    display.set_pen(MAGENTA)
    display.set_font("bitmap8")
    display.text("I must have asked for help " + num + " times by now!", 40, 10, 150, 2, 1, 1)
    display.set_font("serif")
    display.text(blinking, 40, 90, 9999, 1, 1, 1)
    display.update()
    sleep(0.20)
    
    clear(BLACK)
    
    display.set_pen(MAGENTA)
    display.set_font("bitmap8")
    display.text("I must have asked for help " + num + " times by now!", 40, 10, 150, 2, 1, 1)
    display.set_font("serif")
    display.text(sad, 40, 90, 9999, 1, 1, 1)
    display.update()
    sleep(1.5)
    
    clear(BLACK)
    
    interrupt_flag=0
    wait = 100 #300 = 6ish seconds
    
    while wait > 0:
        #display.text(text, x, y, wordwrap, scale, angle, spacing)
        
        display.set_pen(MAGENTA)
        display.set_font("bitmap8")
        display.text("Are you going to help or not?", 40, 10, 150, 2, 1, 1)
        display.set_font("serif")
        display.text(question, 2, 90, 9999, 1, 1, 1)
        
        display.set_pen(GREEN)
        
        x = random.randint(0, 230)
        y = random.randint(0, 125)
        scale = random.randint(1, 4)
        angle = random.randint(-100, 100)
        
        if wait < 30:
            display.text("?",  x,  y, 9999, scale, angle, 1)
            sleep(0.1)
        
        display.update()
    
        if interrupt_flag is 1:
            clear(BLACK)
            display.set_pen(MAGENTA)
            display.set_font("bitmap8")
            n=0
            display.text("Finally, a bit of help around here...", 40, 10, 150, 2, 1, 1)
            display.set_font("serif")
            display.text(happy, 40, 90, 9999, 1, 1, 1)
            display.update()
            interrupt_flag=0
            print("Button A")
            sleep(3)
            wait=0
            
        elif interrupt_flag is 2:
            clear(BLACK)
            display.set_pen(MAGENTA)
            display.set_font("bitmap8")
            n=0
            display.text("I appreciate the help...", 40, 10, 150, 2, 1, 1)
            display.set_font("serif")
            display.text(happy, 40, 90, 9999, 1, 1, 1)
            display.update()
            interrupt_flag=0
            print("Button B")
            sleep(3)
            wait=0
            
        elif interrupt_flag is 3:
            clear(BLACK)
            display.set_pen(MAGENTA)
            display.set_font("bitmap8")
            n=0
            display.text("It's about bloody time...", 40, 10, 150, 2, 1, 1)
            display.set_font("serif")
            display.text(happy, 40, 90, 9999, 1, 1, 1)
            display.update()
            interrupt_flag=0
            print("Button X")
            sleep(3)
            wait=0
            
        elif interrupt_flag is 4:
            clear(BLACK)
            display.set_pen(MAGENTA)
            display.set_font("bitmap8")
            n=0
            display.text("I thought you'd never offer...", 40, 10, 150, 2, 1, 1)
            display.set_font("serif")
            display.text(happy, 40, 90, 9999, 1, 1, 1)
            display.update()
            interrupt_flag=0
            print("Button Y")
            sleep(3)
            wait=0
            
        wait -= 1
    
    #post credits scene maybe?
    #display.text(text, x, y, wordwrap, scale, angle, spacing)
#     clear(RED)
#     sleep(1)
#     display.set_font("bitmap14_outline")
#     display.set_pen(BLACK)
#     display.text("I guess I'll ask again...", 10, 10, 130, 2, 1,)
#     display.update()
#     sleep(2)

