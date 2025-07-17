def readin():
    entirefile = ""
    readingx = []
    readingy = []
    readingz = []
    file_path = r'../data/360_904_-48.txt'
    entirefile = open(file_path, "r")
    linesarray = entirefile.read().splitlines()
    entirefile.close()

    for line in linesarray:
        lineparts = line.split("	")
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
    # mid = (max + min)/2
    print(min)

    return max

def countstep(max, readingy):
    steps = 0
    over = []
    for loops in range(0, len(readingy)):
        if readingy[loops] > (max - 300):
            steps = steps + 1
            over.append(readingy[loops])
    print(steps, over)

    return over


readingx, readingy, readingz = readin()
max = storeminmix(readingy)
over = countstep(max, readingy)

