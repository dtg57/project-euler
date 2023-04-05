import random
import time
import datetime

colours=['r','o','y','g','b','i','v']
balls=[]
for a in range(10):
    for b in range(7):
        balls.append(colours[b])
print(balls)
average=0
count=0
for i in range(1,10000000):
    balls2=balls
    selection=[]
    now=datetime.datetime.now()
    for b in range(20):
        num=random.randint(0,len(balls2)-1)
        selection.append(balls2[num])
        del balls2[num]
    count+=len(set(selection))
    average=(average*(i-1)+count)/i
    if i%500==0:
        print(average)
print(average)
