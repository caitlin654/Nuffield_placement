# Project Notes

[toc]

## Steps
- [ ] get position from accelerometer every time period  **Ensure they're not just random numbers**


- [ ] append position to array
  ```python
  def getdata():
      positionsx = []
      loops = 0
  
      while loops>20:
          positionx = accelerometer.get_x()
          positionsx.append(positionx)
          loops = loops + 1
  ```

- [ ] print new position to file

- [ ] read positions from file to python and change to graph



## Project log

### Day 2 - 15/7

- [ ] figure out how to have it function not connected to computer
- [ ] do i need all 3 axis?  
> With this type of step counter, the number of zero crossings or peaks of the vertical acceleration of the body versus time curve is used to determine the number of steps. 
- [ ] set a minimum, and then have a step be counted every time that minimum is crossed (minus minimum from all other data to find reletives)
- [ ] how do i change the mu save location? or a solution to the having to copy it across every time.
- [ ] get the graph to look normal
- got the micro:bit to make a file
- wrote positions into the file **must be strs**
- exported file to new programme and printed as a mu graph

### Day 1 - 14/7

- familiarization with software being used
  (Mu, Git, Typora)
- writing basic micro:bit programs for testing and refamiliarization 
- writing basic micro:bit programs involving accelerometer
- attempted setting up the micro:bit for remote use
- wrote basic program to turn a small array into a graph
- got data for multiple loops
- put info into arrays and print arrays
- got info in all three dimensions

