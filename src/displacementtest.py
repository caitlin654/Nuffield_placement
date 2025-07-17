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

def getaccel(readingy):
    totalaccel = 0
    for loops in range(0, len(readingy)):
        totalaccel = (totalaccel + (readingy[loops]/1000))
    return totalaccel

def getdisplacement(totalaccel):
    time = 25
    initial_velocity = 0

    # velocity = initial_velocity + (totalaccel * time)
    displace = ((initial_velocity*time) + (0.5 * totalaccel * (time**2)))/2
    displace = round(displace,1)

    print(displace)

    return displace

readingx, readingy, readingz = readin()
totalaccel = getaccel(readingy)
displace = getdisplacement(totalaccel)

