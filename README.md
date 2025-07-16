# Project Notes

[toc]

## Steps
- [ ] get position from accelerometer every time period  **Ensure they're not just random numbers**

- [x] append position to array

- [x] print new position to file

- [x] read positions from file to python and change to graph

- [ ] use graphs to measure DST?

> Given the same angles, the vertical displacement would be greater or smaller for taller or shorter people, thus accounting for differences in leg length.
Unfortunately, the accelerometer measures changes in acceleration rather than displacement. The acceleration must be converted to distance before it can be used. In the AN-602 setup, limited computing power required that a simple formula be used to approximate the double integral needed to convert acceleration into distance. (Adv higher physics :pensive: )

- [ ] see what positioning of pedometer are best, and if multiple ones are better or not(dk how you'd upload to multiple?the radio function could maybe be used?)

  

![walking acceleration graphs](./imgs/walking1graphs.png) 

  


## Project log

### Day 4 - 14/7
- [ ] finish functional requirements of minimumparallel.py 
- [ ] try to see what the acceleration means(make decipherable graph)+(diagram of axis on the micro:bit) +(see what would need to be done to use DST)
- [ ] annotate accelorometer graph(walking one)(see example in imgs)



### Day 3 - 16/7 
- made graphs from data sets(csv converted to excel) produced when the micro:bit was shaken, stationary and walking(swinging while held)
- test of axis' to see which ones showed the movement the best(shown in graphs)  - program to visualize z and x axis changes
- functional requirements of minimumparallel.py
- read papers on accelerometer graphs 

> With this type of step counter, the number of zero crossings or peaks of the vertical acceleration of the body versus time curve is used to determine the number of steps. 

- [ ] set a minimum, and then have a step be counted every time that minimum is **crossed** (<mark style = "background-color :  lightblue;">minus minimum from all other data to find relatives</mark>)(with walking graphs average peaks can be found much easier, so this will work better)

### Day 2 - 15/7


- got the micro:bit to make a file
- wrote positions into the file **must be strs**
- exported file to new program and printed as a mu graph
- made program to find min and max of each axis from the data file, find the midpoint and then count every time the midpoint was met
- converted csv files with the data to excel spreadsheet 
- increased range of data being taken in, and tested for error caused by this

### Day 1 - 14/7

- familiarization with software being used
  (Mu, Git, Typora)
- writing basic micro:bit programs for testing and refamiliarization 
- writing basic micro:bit programs involving accelerometer
- attempted setting up the micro:bit for remote use
- wrote basic program to turn a small array into a graph
- got data for multiple loops
- put info into arrays and print arrays
- got info in all three axis

