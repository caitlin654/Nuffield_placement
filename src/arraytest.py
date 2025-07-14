from microbit import *
import time

positions = []
for loops in range(0, 10):
    position = accelerometer.get_values()
    positions.append(position)
    time.sleep(1)

open('test.txt', 'w')
for loops in range(0, len(positions)):
   test.txt.write(positions[loops])

