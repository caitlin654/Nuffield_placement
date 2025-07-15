
def readin():
    entirefile = ""
    readingx = []
    readingy = []
    readingz = []
    entirefile = open("test.csv", "r")
    linesarray = entirefile.read().splitlines()
    entirefile.close()

    for line in linesarray:
        lineparts = line.split(",")
        readingx1 = (int(lineparts[0]))
        readingx.append(readingx1)
        readingy1 = (int(lineparts[1]))
        readingy.append(readingy1)
        readingz1 = (int(lineparts[2]))
        readingz.append(readingz1)
    return readingx, readingy, readingz

def findminmaxx(readingx):
    minimumx = readingx[0]
    maximumx = readingx[0]

    for loops in range(0 , len(readingx)):
        if readingx[loops] < minimumx:
            minimumx = readingx[loops]
        elif readingx[loops] > maximumx:
            maximumx = readingx[loops]

    print(minimumx, maximumx)
    return minimumx, maximumx

readingx, readingy, readingz = readin()
minimumx, maximumx = findminmaxx(readingx)
