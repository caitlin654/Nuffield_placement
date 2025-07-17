def readin():
    entirefile = ""
    readingx = []
    readingy = []
    readingz = []
    file_path = r'../data/test.csv'
    entirefile = open(file_path, "r")
    linesarray = entirefile.read().splitlines()
    entirefile.close()

    for line in linesarray:
        lineparts = line.split(",")
        readingx1 = int(lineparts[0])
        readingx.append(readingx1)
        readingy1 = int(lineparts[1])
        readingy.append(readingy1)
        readingz1 = int(lineparts[2])
        readingz.append(readingz1)
    return readingx, readingy, readingz
def getaccel(readingx):
    totalaccel = 0
    for loops in range(0,len(readingx)):
        totalaccel = totalaccel + readingx[loops]
    return
def getdisplacement(totalaccel):
    time = 25
    velocity = 0
    displace = 0

readingx, readingy, readingz = readin()
totalaccel = getaccel(readingx)
displace,velocity = getdisplacement(totalaccel)

