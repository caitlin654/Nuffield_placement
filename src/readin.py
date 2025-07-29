from microbit import *
import time

time.sleep(1)#start warning sequence
display.show(Image.HEART)
time.sleep(5)
display.clear()

positions = []
for loops in range(0, 700):
    position = ""
    position = accelerometer.get_values()#obtain accelerometer values
    positions.append(position)#append to array
    time.sleep(0.1)#sleep to space out readings

with open('test.csv', 'w') as file:
    for loops in range(0, len(positions)):
        test1 = (str(positions[loops]))
        test1 = (test1[1:len(test1)-1] + "\n")
        file.write(str(test1))#write position without brackets to a new line

display.show(Image.YES)#signal end
