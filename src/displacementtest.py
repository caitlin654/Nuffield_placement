def readin():
    entirefile = ""
    readingx = []
    readingy = []
    readingz = []
    file_path = r'C:\Users/Summer School - 1/mu_code/test.csv'
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

def getaccel(readingy):
    totalaccel = 0
    for loops in range(0, len(readingy)):
        totalaccel = (totalaccel + (readingy[loops]/1000))
    return totalaccel


def getdisplacement(readingy):
    vel = 0
    dis = 0
    time = 0.1

    for loops in range(0, len(readingy)):
        acc = readingy[loops]/1000
        vel = vel + (acc)*time
        dis = dis + (vel*time) +(0.5 * acc *(time**2))

    dis = round(dis, 1)

    print(dis)
    return dis,vel


readingx, readingy, readingz = readin()
totalaccel = getaccel(readingy)
dis, vel = getdisplacement(readingy)


