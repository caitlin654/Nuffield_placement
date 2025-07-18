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

def getmag(readingx, readingy, readingz):
    mag = []
    for loops in range(0,len(readingx)):
        addmag = ((readingx[loops]**2) + (readingy[loops]**2) + (readingz[loops]**2))**0.5
        mag.append(addmag)
    return mag

def getdisplacement(mag):
    vel = 0
    dis = 0
    time = 0.1
    tt = 0

    for loops in range(0, len(mag)):
        acc = (mag[loops]/1000) * 9.8
        vel = (acc)*time
        dis = dis + (vel*time) +(0.5 * acc *(time**2))
        tt = tt + time

    dis = round(dis, 1)
    tt = round(tt,1)
    print(dis,"meters in", tt, "seconds")
    return dis,vel


readingx, readingy, readingz = readin()
mag = getmag(readingx, readingy, readingz)
dis, vel = getdisplacement(mag)


