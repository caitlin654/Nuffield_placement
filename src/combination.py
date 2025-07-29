import tkinter as tk

def readin():
    entirefile = ""
    readingx = []
    readingy = []
    readingz = []
    #file_path = r'../data/test(45steps).csv'
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
    # getting the magnitude of the three axis to use to count steps
    mag = []
    for loops in range(0, len(readingx)):
        addmag = ((readingx[loops]**2) + (readingy[loops]**2)
                  + (readingz[loops]**2))**0.5
        addmag = round(addmag, 0)
        mag.append(addmag)
    return mag

def findminmax(mag):
    # getting the maxmimum to use to count steps
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
    count = 0
    for loops in range(0, len(mag)):
        if mag[loops] > (max * 0.55):  # number changes based on activity and placement
            # if the mag is > than a % of the max then true
            boo.append("True")
        else:
            boo.append("False")
        if boo[loops] == "True" and boo[loops-1] == "False":
            # if the previous mag wasnt over the boundary(true), count as step
            steps = steps + 1
            over.append(mag[loops])
    return steps, over

def distance(steps, ay):
    #basic stride * steps distance calculator
    dist = 0
    time = 0.1 * len(ay)

    stride = 0
    dist = stride * steps

    dist = round(dist, 2)
    time = round(time, 1)

    return dist, time

# top level
readingx, readingy, readingz = readin()
mag = getmag(readingx, readingy, readingz)
minimum, maximum = findminmax(mag)
steps, over = countstep(maximum, mag)
dist, tt = distance(steps, readingy)

# tkinter output

def getInformation():
    # function that is called to print the output, and use the stride
    stride1 = stride.get()
    dist = (float(stride1) * steps)
    speed = dist/tt
    speed = round(speed,1)
    dist = round(dist,1)
    show_information.config(text="Distance: " + str(dist) + " meters in " + str(tt)
                            + " seconds \n" + "Steps: " + str(steps) + "\n"+ "Average Speed :" + str(speed) + " m/s")

#set up the window
window = tk.Tk()
window.configure(bg="#c7e3c1")
window.title("UI")
window.geometry("500x350")
frame = tk.Frame(bg="#c7e3c1")

#set up the input within that window
info_frame = tk.Frame(window, bg="white" )
info_frame.grid(row=1, column=1, columnspan=3, padx=100, pady=15)


stride_label = tk.Label(info_frame, text="Enter Stride Length (m) ", bg="white")
stride_label.grid(row=0, column=0, padx=5, pady=5)

stride = tk.Entry(info_frame)
stride.grid(row=0, column=1, padx=5, pady=5)

#add input button
get_info = tk.Button(info_frame, text="Show output", command=getInformation, bg="white")
get_info.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

#output styling
show_information = tk.Label(font='serif', bg="#c7e3c1", fg="#3b3e45")
show_information.grid(row=2, column=2, pady=7, padx=10)



#execution
window.mainloop()
