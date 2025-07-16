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

def storeminmix(readingx):
    min, max = findminmax(readingx)
    #mid = (max + min)/2
    print(max)

    return max

def countstep(int, array):
    steps = 0
    over = []
    for loops in range(0, len(array)):
        if array[loops] > (int-400):
            steps = steps + 1
            over.append(array[loops])

    return steps, over

def countstep2(max, readingx):
    step , over = countstep(max, readingx)

    print(step, over)
    return  step

readingx, readingy, readingz = readin()
max = storeminmix(readingx)
step = countstep2(max, readingx)

