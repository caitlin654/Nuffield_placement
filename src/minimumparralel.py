def readin():
    entirefile = ""
    readingx = []
    readingy = []
    readingz = []
    file_path = r'C:/Users/Summer School - 1/mu_code/test.csv'
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

def getmag(readingx, readingy, readingz):
    mag = []
    for loops in range(0, len(readingx)):
        addmag = ((readingx[loops]**2) + (readingy[loops]**2) + (readingz[loops]**2))**0.5
        addmag = round(addmag, 0)
        mag.append(addmag)
    return mag


def findminmax(array):
    minimum = array[0]
    maximum = array[0]

    for loops in range(0, len(array)):
        if array[loops] < minimum:
            minimum = array[loops]
        elif array[loops] > maximum:
            maximum = array[loops]
    return minimum, maximum

def storeminmix(mag):
    min, max = findminmax(mag)
    # mid = (max + min)/2

    return max

def countstep(max, mag):
    steps = 0
    over = []
    boo = []
    for loops in range(0, len(mag)):
        if mag[loops] > (max * 0.75):
            boo.append("True")
        else:
            boo.append("False")
        if boo[loops] == "True" and boo[loops-1] == "False":
            steps = steps + 1
            over.append(mag[loops])
    return over, steps


readingx, readingy, readingz = readin()
mag = getmag(readingx, readingy, readingz)
max = storeminmix(mag)
over, steps = countstep(max, mag)
print(max)
print(steps, "steps")
print(over)

