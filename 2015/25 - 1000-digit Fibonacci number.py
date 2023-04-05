import math
sequence=[1,1]
digits=1
while len(str(sequence[-1]))<1000:
    sequence.append(sequence[-1]+sequence[-2])
    if len(str(sequence[-1]))!=digits:
        print (len(str(sequence[-1])))
        digits=len(str(sequence[-1]))
print (len(sequence))
