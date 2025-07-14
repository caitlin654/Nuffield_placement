from microbit import *

#accelerometer.get_values()  #gives coord
#accelerometer.current_gesture() == "face up" #returns booloean depending on if the face of the microbit is facing up

while True: # shows sad if upside down
    gesture = accelerometer.current_gesture()
    if gesture =="face up":
        display.show(Image.HAPPY)
    else:
        display.show(Image.ANGRY)

#while True:
 #   display.show(Image.DIAMOND)
  #  if accelerometer.was_gesture("shake"):
   #     display.clear()
    #    sleep(1000)
     #   display.show(Image.YES)
      #  sleep(100
