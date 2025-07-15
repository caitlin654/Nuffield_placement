import time
entirefile = ""
readings = []
entirefile = open("test.csv", "r")
linesarray = entirefile.read().splitlines()
entirefile.close()

for line in linesarray:
    readings.append(line)

for loops in range(0, len(readings)):
    print(readings[loops])
    time.sleep(0.5)
