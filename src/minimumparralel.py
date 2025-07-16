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
    midx = (maxx + minx)/2
    midy = (maxy + miny)/2
    midz = (maxz + minz)/2

    return midx, midy, midz, maxy

def countstep(int, array):
    steps = 0
    for loops in range(0, len(array)):
        if array[loops] > (int-100):
            steps = steps + 1

    return steps

def countstep2(midx, midy, midz, readingx, readingy, readingz):
    stepx = 0  # countstep(midx, readingx)
    stepy = countstep(maxy, readingy)
    stepz = 0  # countstep(midz, readingz)

    print(stepx, stepy, stepz)
    return stepx, stepy, stepz

readingx, readingy, readingz = readin()
midx, midy, midz, maxy = storeminmix(readingx, readingy, readingz)
stepx, stepy, stepz = countstep2(midx, midy, midz, readingx, readingy, readingz)

