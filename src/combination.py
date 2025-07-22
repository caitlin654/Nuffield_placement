import tkinter as tk

def readin():
    entirefile = ""
    readingx = []
    readingy = []
    readingz = []
    # file_path = r'C:/Users/Summer School - 1/mu_code/test.csv'
    file_path = r'../data/upstairnoswing.csv'
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
    return steps, over

def getdisplacement(readingx, readingy):
    disp = 0
    time = 0.1
    t = 0
    magd = 0.0
    vel = 0.0

    for loops in range(0, len(readingx)):
        magd = ((readingx[loops]**2) + (readingy[loops]**2))**0.5
        magd = (magd/1000)*9.8
        print(magd)

        vel = (magd*time)
        disp = disp + (vel*time)

        t = t + time

    disp = round(disp, 2)
    disp = abs(disp)
    t = round(t, 1)

    return disp, t

def distance(ay, ax):
    dist = 0
    tt = 0
    for loops in range(0, len(ay)):
        changex = 0
        changey = 0
        changedist = 0
        time = 0.1

        accx = ((ax[loops]/1000) * 9.8)  # converting from mg to g to ms-2
        accy = ((ay[loops]/1000) * 9.8)
        velx = (accx)*time
        vely = (accy)*time

        changex = abs((velx * time) + (0.5 * accx * (time)**2))
        changey = abs((vely * time) + (0.5 * accy * (time)**2))
        changedist = ((changex**2) + (changey**2))**0.5
        dist = dist + changedist
        tt = tt + time

    dist = round(dist, 2)
    tt = round(tt, 1)

    return dist, tt


# top level
readingx, readingy, readingz = readin()
mag = getmag(readingx, readingy, readingz)
minimum, maximum = findminmax(mag)
steps, over = countstep(maximum, mag)
disp, t = getdisplacement(readingx, readingy)
dist, tt = distance(readingy, readingx)

# outputs
root = tk.Tk()
root.geometry("500x350")
text_widget = tk.Text(root, wrap='word', height=20, width=80,
                      font='serif', bg="#c7e3c1", fg="#3b3e45")
text_widget.insert(tk.END, "Displacement: " + str(disp)+" meters in " + str(tt)
                   + " seconds \n")
text_widget.insert(tk.END, "Distance: " + str(dist) + " meters in " + str(tt)
                   + " seconds \n")
text_widget.insert(tk.END, "Steps: " + str(steps) + "\n\n")
text_widget.insert(tk.END, "Max: " + str(maximum) + "\n")
text_widget.insert(tk.END, "Readings counted as steps: " + str(over) + "\n")
text_widget.pack(expand=True, fill='both')
root.mainloop()
