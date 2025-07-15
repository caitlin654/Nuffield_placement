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
        readingx1 = int(lineparts[0])
        readingx.append(readingx1)
        readingy1 = int(lineparts[1])
        readingy.append(readingy1)
        readingz1 = int(lineparts[2])
        readingz.append(readingz1)
    return readingx, readingy, readingz


def findminmax(array):
    minimum = array[0]
    maximum = array[0]

    for loops in range(0, len(array)):
        if array[loops] < minimum:
            minimum = array[loops]
        elif array[loops] > maximum:
            maximum = array[loops]
    return minimum, maximum

def storeminmix(readingx, readingy, readingz):
    minx, maxx = findminmax(readingx)
    miny, maxy = findminmax(readingy)
    minz, maxz = findminmax(readingz)

    return minx, maxx, miny, maxy, minz, maxz

readingx, readingy, readingz = readin()
minx, maxx, miny, maxy, minz, maxz = storeminmix(readingx, readingy, readingz)
print(minx, maxx, miny, maxy, minz, maxz)
