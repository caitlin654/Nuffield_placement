class reading():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def readin():
    entirefile = ""
    readings = []
    entirefile = open("test.csv", "r")
    linesarray = entirefile.read().splitlines()
    entirefile.close()

    for line in linesarray:
        lineparts = line.split(",")
        reading1 = reading(int(lineparts[0]), int(lineparts[1]), int(lineparts[2]))
        readings.append(reading1)
    return readings

def findminmaxx(readings):
    minimumx = readings[0].x
    maximumx = readings[0].x

    #for loops in range(0 , len(readings)):
     #   if readings[loops].x < minimumx:
      #      minimumx = reading[loops].x
       # elif readings[loops].x > maximumx:
        #    maximumx = reading[loops].x

    print(minimumx, maximumx)

readings = readin()
minimumx, maximumx = findminmaxx(readings)
