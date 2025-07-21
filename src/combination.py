import tkinter as tk

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
        addmag = ((readingx[loops]**2) + (readingy[loops]**2)
                  + (readingz[loops]**2))**0.5
        addmag = round(addmag, 0)
        mag.append(addmag)
    return mag

def findminmax(mag):
    minimum = mag[0]
    maximum = mag[0]

    for loops in range(0, len(mag)):
        if mag[loops] < minimum:
            minimum = mag[loops]
        elif mag[loops] > maximum:
            maximum = mag[loops]
    return minimum, maximum

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
    return steps

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

    return disp, vel, tt

def distance(ay, ax):
    dist = 0
    for loops in range(1, len(ay)):
        changex = 0
        changey = 0
        changedist = 0
        time = 0.1

        accx = (ax[loops]/1000) * 9.8  # converting from mg to g to ms-2
        accy = (ay[loops]/1000) * 9.8
        velx = (accx)*time
        vely = (accy)*time

        changex = ((velx * time) + (0.5 * accx * (time)**2))
        changey = ((vely * time) + (0.5 * accy * (time)**2))
        changedist = ((changex**2) + (changey**2))**0.5
        dist = dist + changedist

    dist = round(dist, 0)

    return dist

# top level
readingx, readingy, readingz = readin()
mag = getmag(readingx, readingy, readingz)
minimum, maximum = findminmax(mag)
steps = countstep(maximum, mag)
disp, vel, tt = getdisplacement(readingx)
dist = distance(readingy, readingx)

# outputs
root = tk.Tk()
root.geometry("500x250")
text_widget = tk.Text(root, wrap='word', height=20, width=80, font='serif', bg ="#b9cded", fg = "#3b3e45")
text_widget.insert(tk.END, "Displacement: " + str(disp)+" meters in " + str(tt)+" seconds \n")
text_widget.insert(tk.END, "Distance: " + str(dist) + " meters in " + str(tt)+" seconds \n" )
text_widget.insert(tk.END, "Steps: " + str(steps) +"\n")
text_widget.insert(tk.END, "Max: " + str(maximum) +"\n")
text_widget.pack(expand=True, fill='both')
root.mainloop()
