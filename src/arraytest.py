from microbit import *
import time

#microbit.accelerometer.set_range(4)

time.sleep(1)
display.show(Image.HEART)
time.sleep(2)
display.clear()

positions = []
for loops in range(0, 100):
    position = ""
    position = accelerometer.get_values()
    positions.append(position)
    time.sleep(0.1)

with open('test.csv', 'w') as file:
    for loops in range(0, len(positions)):
        test1 = (str(positions[loops]))
        test1 = (test1[1:len(test1)-1] + "\n")
        file.write(str(test1))

display.show(Image.ALL_ARROWS)
