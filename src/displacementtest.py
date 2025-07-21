def readin():
    entirefile = ""
    readingx = []
    readingy = []
    readingz = []
    file_path = r'../data/noswing.csv'
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
        mag.append(addmag)
    return mag

def getdisplacement(readingx):
    vel = 0
    disp = 0
    time = 0.1
    tt = 0

    for loops in range(0, len(readingx)):
        acc = (readingx[loops]/1000) * 9.8  # converting from mg to g to ms-2
        vel = vel + (acc)*time
        disp = disp + (vel*time) + (0.5 * acc * (time**2))
        tt = tt + time

    disp = round(disp, 1)
    disp = abs(disp)
    tt = round(tt, 1)

    print(disp, "meters in", tt, "seconds")
    return disp, vel

def distance(y, x):
    dist = 0
    for loops in range(1, len(y)):
        changex = 0
        changey = 0
        changedist = 0
        time = 0.1

        acc = (readingx[loops]/1000) * 9.8  # converting from mg to g to ms-2
        vel = (acc)*time

        x[loops] = x[loops - 1] + ((vel * time) + (0.5 * acc * (time)**2))
        changex = x[loops] - x[loops - 1]
        changex = (changex/1000) * 9.8
        changey = y[loops] - y[loops - 1]
        changey = (changey/1000) * 9.8
        changedist = ((changex**2) + (changey**2))**0.5
        dist = dist + changedist

    dist = round(dist,0)
    print(dist)

    return dist

readingx, readingy, readingz = readin()
# mag = getmag(readingx, readingy, readingz)
disp, vel = getdisplacement(readingx)
dist = distance(readingy, readingx)
