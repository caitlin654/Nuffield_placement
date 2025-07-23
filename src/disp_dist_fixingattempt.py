def getdisplacement(readingx, readingy, readingz):
    disp = 0
    time = 0.1
    t = 0
    magd = 0.0
    vel = 0.0

    for loops in range(0, len(readingx)):
        magd = ((readingx[loops]**2) + (readingy[loops]**2))**0.5 # change
        magd = (magd/1000)*9.8

        vel = (magd*time)
        dispx = (vel * time) + (0.5 * magd * (time)**2)
        disp = disp + dispx

        t = t + time

    disp = round(disp, 2)
    disp = abs(disp)
    t = round(t, 1)

    return disp, t

def distance(ay, ax, az):
    dist = 0
    tt = 0
    xold = 0
    yold = 0
    for loops in range(0, len(ay)):
        changex = 0
        changey = 0
        changedist = 0
        time = 0.1

        accx = ((ax[loops]/1000) * 9.8)  # converting from mg to g to ms-2
        accy = ((ay[loops]/1000) * 9.8)
        velx = abs((accx)*time)
        vely = abs((accy)*time)

        changex = (velx * time)
        changey = (vely * time)
        changedist = ((changex-xold)**2) + (changey-yold)**2))**0.5 # distance forula using previos values
        dist = dist + changedist

        xold = ax[loops]
        yold = ay[loops]
        tt = tt + time

    dist = round(dist, 2)
    tt = round(tt, 1)

    return dist, tt

#intial velocity = u = v - at (a = ms-2) a=reading t = 0.1
#if t cant be a running total, think the same needs to be for v
#final velocity = v = u + at
#displacemnt = s = ut + (1/2)at²
#distance = st (s = abs(v))
