# Project Notes

[toc]

## Steps/Things to look at
- [x] get position from accelerometer every time period 

- [x] append position to array

- [x] print new position to file

- [x] read positions from file to python and change to graph

- [x] use data to measure SVT?

  ```python
  def getdisplacement(readingy):
      vel = 0
      dis = 0
      time = 0.1
      
      for loops in range(0, len(readingy)):
          acc = readingy[loops]/1000
          vel = vel + (acc)*time
          dis = dis + (vel*time) +(0.5 * acc *(time**2))
          
      dis = round(dis, 1)
  	return dis
  ```

  

- [x] see what positioning of pedometer are best, especially with calculating displacement(**seems like logo needs to be up for displacement to be positive**, **no arm swing also seems to give better results**) 

- [ ] try to find out how to increase range of micro:bit to prevent data loss(current max is 2040mg)  **code below doesn't work**  *attribute error*  
  
    ```python
    input.set_accelerometer_range(
        AcceleratorRange.FOUR_G)
    ```

- [x] calculate distance alongside displacement


``` python
for loops in range(0,len(x)):
	changex = ((velx * time) + (0.5 * accx * (time)**2))
    changey = ((vely * time) + (0.5 * accy * (time)**2))
   	changedist = ((changex**2) + (changey**2))**0.5
    dist = dist + changedist
```

- [ ] can it see the difference between activities (like stairs/walking)(ask remote) 

- [x] differences in accuracy of data depending on positions of accelerometer on the body(belt/holding(swing/no swing)/leg) 

- [ ] tell difference between people walking

- [x] could calculate speed



### REPORT attatchments needed
- [ ] ask to get more graphs printed off for Glasgow thing (long time ones)
- [ ] off load good spreadsheet(noswing3 and 1, downstairs, all users(mum2), )


## SL7 To Do
- [ ] complete outcome 3 & 6

  

- [ ] get dad to do SL7 stuff

### Sl7/report thigs to attach

- [ ] self development plan
- [ ] report
- [ ] poster
- [ ] readme

 ### crest award things to attach
- [ ] profile form
- [ ] report(updated to requirement)
- [ ] readme/ tidied to a log


## Project log

someone said something about a blog?

poster and report(+Sl7 stuff) due 31/8

crest due asap after report done(check current report fits requirement)

offload anything needed to git(excel sheets)

### Day 15 - 1/8
- [ ] export any final versions and excel sheets to git

- [ ] sort what is being sent where

- [ ] make crest version of report

- [ ] rename report

  

### Day 14 - 31/7
- [ ] finish poster(see notes)
- [ ] finish SL7 stuff

- [ ] stairs, longer walks(continue to count steps when doing these)
- [ ] sort README(add longer time graphs)



- updated report with user and activity graphs 
- finished report
- complied report, timeline and SL7 stuff

### Day 13 - 30/7
- proofread and continued report
- tested microbit on different users and activities and made graphs from data
- added different users and activities graphs into report 

### Day 12 - 29/7
- started poster 

- did more report
- tested step counting accuracy over longer periods of time(2-5% error)


### Day 11 - 28/7

- got more no swing data, counted steps and checked accuracy
- did more work on report


### Day 10 - 25/7

- finished styling the UI

- added speed calculation

- updated imgs with new output

- calculated percentage errors between old distance measurements and new ones

- tested max run time and file size for the microbit

- did more work on report

### Day 9 - 24/7
- Aileen visiting in morning(11-12)
- computer visit (1-4)
- added internal commentary to combination.py
- updated gui for stride length
- changed combination.py so that it calculates distance via stride length * steps
- combination.py *doesn't work because as you change direction, the coord system rotates, meaning its now at an angle compared to the original coord, and so the distance is over estimated, therefore it will work when tested in a straight-line, but once tested on an actual walk, both distance and displacement will be wrong* 

``` python
#old code, use in report to show what was being done before
def getdisplacement(readingx, readingy, readingz):
    disp = 0
    time = 0.1
    magd = 0.0
    vel = 0.0

    for loops in range(0, len(readingx)):
        magd = ((readingx[loops]**2) + (readingy[loops]**2))**0.5
        magd = (magd/1000)*9.8

        vel =  (magd*time)
        dispx = (vel * time) 
        disp = disp + dispx

    disp = round(disp, 2)
    disp = abs(disp)
  
    return disp, t

def distance(ay, ax, az):
    dist = 0
    xold = 0
    yold = 0
    velx = 0
    vely = 0
    for loops in range(0, len(ay)):
        time = 0.1

        accx = ((ax[loops]/1000) * 9.8)  # converting from mg to g to ms-2
        accy = ((ay[loops]/1000) * 9.8)

        changex = (velx * time) + (0.5 * accx *(time)**2)
        changey = (vely * time) + (0.5 * accy *(time)**2)
        changedist = ((changex)**2 + (changey)**2)**0.5
        dist = dist + changedist

        velx = (accx)*time
        vely = (accy)*time

    dist = round(dist, 2)
    return dist
```

  

### Day 8 - 23/7

- updated SL7 doc with feedback given 

- Updated Gantt chart
- formatted image section
- did more work on the report
- updated list of report/SL7/crest attachments
- tested different positions on the body **handheld no swing works best, other positions would likely work, however they need to be close to stationary during movement for most accuracy** ,**hand held (regardless of swing or not) works best** 
- updated images with 4 new graphs and results obtained from positions texting and swing testing
- added internal commentary to arraytest.py
- tested combination.py more (accuracy) (used measuring tape and did displacement/distance comparison) *distance and displacement seems to be a couple of meters off each time, but displacement more so* *think its because of logic errors in regards to v and u* 

### Day 7 - 22/7

- made Gantt chart for project
- completed further SL7 work
- added error logs back in to README.md
- wrote a Personal Development Plan
- did further poster design (added axis diagram)
- revised distance vs displacement and implemented new plan *think it works now*  
- collected and tested data with new displacement module
- tested how data looks when taken going upstairs
- made graphs for stairs data sets
- updated combi.py results for older data sets
- made further plans for reports, started writeup

### Day 6 - 21/7

- began to implement interface for display of outputs *doesn't kill program when close window* 
- implemented distance module and realized displacement one doesn't work *i think the distance one works but the displacement one doesn't work, (except with noswing data set* )
- collected data with arm swing to compare to data with no arm swing, made graphs(see images) **no arm swing gives better results for graphs, and more reliable step counting** 
- made a big program of both minimumparallel.py and displacementtest.py 
- read more articles for references 
- tried to set the range of the accelerometer again, *still doesn't work(attribute error)*
- started stem leader booklet

### Day 5 - 18/7


- tried to fix error in displacement calculating program *distance was calculated correctly, but displacement didn't, however because it was close to true on one data set, i didn't notice* 

- updated graph so that it uses magnitude of three axis, and then counts steps using percentage instead of chosen number 

- updated minimumparallel.py so that it uses magnitude to count steps instead of whatever axis i thought looked best, and uses the same step counting as the excel sheets

- tested pedometer with no swing of the arm (just held still) **no swing seems to give better results, especially on the y axis**

- started trying to get distance as well as displacement 

- made tidy graphs(labels,times) with no_swing data (see images)

### Day 4 - 17/7
- annotated accelerometer graph
- Attempted to increase the range of values measured by the accelerometer 
  *didn't work, have code that should work but doesn't* 
- collected further data with walks, checked accuracy of minparallel.py with these programs 
- revised the use of the integration of acceleration to find velocity and displacement 
- wrote initial pseudocode for displacement program **total acceleration?** 
- wrote initial program to find displacement(results seemed larger than they should) 

### Day 3 - 16/7 
- made graphs from data sets(csv converted to excel) produced when the micro:bit was shaken, stationary and walking(swinging while held)
- test of axis' to see which ones showed the movement the best(shown in graphs)  - program to visualize z and x axis changes
- wrote functional requirements of minimumparallel.py, and defined the program 
- read papers on accelerometer graphs (see References.md )

> With this type of step counter, the number of zero crossings or peaks of the vertical acceleration of the body versus time curve is used to determine the number of steps. 

- updated max and min finding program to count every time a reading is within range of the max, and used this to count the steps (with walking graphs average peaks can be found much easier, so this will work better) 

- did mock walking(swinging arm ) tests with larger arrays, made graphs and counted steps(graph peaks) with minimumparallel.py 

- tested the effect of orientation of the usability of graphs produced by data (*best ones to use are logo facing left/right, but right will use maxes and left will use mins, both will use x axis(**edit parameter passing in minimumparalel.py depending on what one is used , and changed whether int is being added to or taken away from**) *realised minparalle wasn't efficient, and ended up switching so it used magnitude to fix this* 

  

### Day 2 - 15/7


- got the micro:bit to make a file
- wrote positions into the file **must be strs** *file writing wasn't working because i'd forgotten how to do it*  
- exported file to new program and printed as a mu graph
- made program to find min and max of each axis from the data file, find the midpoint and then count every time the midpoint was met (didn't work, cos midpoints were used)*logic error in how i was trying to count the steps*  
- converted csv files with the data to excel spreadsheet 
- increased range of data being taken in, and tested for error caused by this

### Day 1 - 14/7

- familiarization with software being used
  (Mu, Git, Typora)
- writing basic micro:bit programs for testing and refamiliarization 
- writing basic micro:bit programs involving accelerometer
- attempted setting up the micro:bit for remote use *add* 
- wrote basic program to turn a small array into a graph
- got data for multiple loops
- put info into arrays and print arrays
- got info in all three axis

## Images

### No arm swing
![no swing graphs](./imgs/no_swing_graphs.png)  
<img src="./imgs/noswing_reults_3.png" width="250" height="175" > 
<img src="./imgs/noswing_newresults.png" width="250" height="175">   


graphs and results for no swing walk test - magnitude of acceleration is include, however due to no swing, it is the same as the y axis acceleration graph (0.75)

### No arms swing 2
![no swing graphs](./imgs/noswing2_graphs.png)  
<img src="./imgs/NOSWING2_RESULTS.png" width="250" height="175">  
<img src="./imgs/NOSWING2_NEWRESULTS.png" width="250" height="175">  
(0.75)

### no arm swing 3 
![no swing graphs](./imgs/NOSWING3_GRAPHS.png)  
<img src="./imgs/NOSWING3_RESULTS.png" width="250" height="175" >  (0.75)


### Arm swing graphs
![swing graphs](./imgs/SWINGGRAPHS.png)  
<img src="./imgs/swing_newresults.png" width="250" height="175">   

graphs and results for arm swing test - magnitude of acceleration is still very similar to y axis, but now slightly different due to swing (0.5)

### Arm swing 2
![no swing graphs](./imgs/SWING2_GRAPHS.png)  
<img src="./imgs/SWING2_RESULTS.png" width="250" height="175"> 
(0.75)


### upstair no arm swing
![swing graphs](./imgs/downstair_noswing_graphs.png)     

<img src="./imgs/upstairnoswing_results.png" width="250" height="175"> 

results from combination.py for climbing up stairs with no arm swing(0.75)



### down no swing
![swing graphs](./imgs/upstair_noswing_graphs.png) 

<img src="./imgs/downstairnoswing_results.png" width="250" height="175"> 

results from combination.py for climbing down stairs with no arm swing (0.6)

### Back Pocket
![no swing graphs](./imgs/backpocket_graphs.png)  
<img src="./imgs/back_results.png" width="250" height="175">  
(0.55)

### Front Pocket
![no swing graphs](./imgs/frontpocket_graphs.png)  
<img src="./imgs/front_results.png" width="250" height="175">  
(0.55)
