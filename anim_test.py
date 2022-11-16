from time import sleep
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_RGB332

display = PicoGraphics(display = DISPLAY_PICO_DISPLAY, rotate = 45, pen_type=PEN_RGB332)
display.set_backlight(1.0)

WHITE = display.create_pen(255, 255, 255)
RED = display.create_pen(255, 0, 0)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)

frame = 0
animation =["(O__O  )", "( O__O )", "(  O__O)", "( O__O )"]

# def animate()
#     frame = frame + 1
#     if floor(frame) > 5 :
#         frame=1  
#     sprt = animation(floor[frame])
# 
# def draw_face():
#     clear()
#     display.text(sprt, 40, 99, 9999, 1, 1, 1)
#     sleep(0.3)
    
def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()
    
# "( O__O )"
# "? ( @ _ @ ) ?"
# "( ^_^)"

display.set_font("serif")

while True:
    
    frame = frame + 1
    
    if frame > len(animation)-1 :
        frame = 0
    
    clear()
    display.set_pen(WHITE)
    display.text(animation[frame], 40, 50, 9999, 1.3, 1, 1)
    display.update()
    
    sleep(0.5)
