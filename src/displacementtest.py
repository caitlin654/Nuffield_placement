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
    for loops in range(0,len(readingx)):
        addmag = ((readingx[loops]**2) + (readingy[loops]**2) + (readingz[loops]**2))**0.5
        mag.append(addmag)
    return mag

def getdisplacement(readingx):
    vel = 0
    disp = 0
    time = 0.1
    tt = 0
    dist = 0.0
    disparray = []

    for loops in range(0, len(readingx)):
        acc = (readingx[loops]/1000) * 9.8 # converting from mg to g to ms-2
        vel =  vel + (acc)*time
        disparray.append((vel*time) +(0.5 * acc *(time**2)))
        disp = disp + (vel*time) +(0.5 * acc *(time**2))
        tt = tt + time

    for loops in range(0,len(readingx)):
        dist = dist + (disparray[loops]-disparray[loops-1])
    print(dist)

    disp = round(disp, 1)
    tt = round(tt,1)
    print(disp,"meters in", tt, "seconds")
    return disp,vel



readingx, readingy, readingz = readin()
#mag = getmag(readingx, readingy, readingz)
dis, vel = getdisplacement(readingx)
