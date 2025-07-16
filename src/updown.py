from microbit import *

while True:
    positionx = accelerometer.get_x()
    positiony = accelerometer.get_y()
    positionz = accelerometer.get_z()
    if positionx > 0 :
        # a = Image('00900:09990:90909:00900:00900:')
        a = Image('00900:00900:99999:00900:00900')
        display.show(a)
    elif positionx < 0 :
        # b = Image('00900:00900:90909:09990:00900:')
        b = Image('00000:00000:99999:00000:00000')
        display.show(b)




