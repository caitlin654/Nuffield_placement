from microbit import *

while True:
    positionx = accelerometer.get_x()
    positiony = accelerometer.get_y()
    positionz = accelerometer.get_z()

    if positionx > 0 and positionz > 0:
        display.show(Image.ARROW_NE)
    elif positionx > 0 and positionz < 0 :
        display.show(Image.ARROW_SE)
    elif positionx < 0 and positionz > 0 :
        display.show(Image.ARROW_NW)
    elif positionx < 0 and positionz < 0 :
        display.show(Image.ARROW_SW)



