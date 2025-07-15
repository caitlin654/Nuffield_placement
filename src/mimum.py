def readin():
    entirefile = ""
    readings = []
    entirefile = open("test.csv", "r")
    linesarray = entirefile.read().splitlines()
    entirefile.close()

    for line in linesarray:
        readings.append(line)
        print(readings)
    return readings

def findminimum(readings):
    minimum = readings[0]
    maximum = readings[0]

    for loops in range(0 ,len(readings)):
        if readings[loops] < minimum:
            minimum =
readings = readin()
minimum, maximum = findminimum(readings)
