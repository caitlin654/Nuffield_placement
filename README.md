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

- [ ] put data into files and bring into other program
- [ ] make graph from accelerometer data(excel or mu?)
- [ ] figure out how to have it function not connected to computer
- [ ] how to write stuff into files?
- [ ] check how accelerometer works

- got the micro:bit to make a file

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

