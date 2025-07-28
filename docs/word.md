``` python
def distance(accy, accx):
    dist = 0
    velx = 0
    vely = 0
    for loops in range(0, len(accy)):
        time = 0.1 
        changex = (velx * time) + (0.5 * accx *(time)**2)
        changey = (vely * time) + (0.5 * accy *(time)**2)
        changedist = ((changex)**2 + (changey)**2)**0.5
        dist = dist + changedist
        velx = (accx)*time
        vely = (accy)*time
    dist = round(dist, 2)
    return dist

def distance(steps, stride):
      distance = stride*steps
     return distance
       
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
```

