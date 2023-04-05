def triangulars(startat,stopat):
    i=startat
    triangulars=[]
    while i<stopat:
        triangulars.append((i*(i+1))/2)
        i=i+1
    return triangulars
def pentagonals(startat,stopat):
    i=startat
    pentagonals=[]
    while i<stopat:
        pentagonals.append((i*(3*i-1))/2)
        i=i+1
    return pentagonals
def hexagonals(startat,stopat):
    i=startat
    hexagonals=[]
    while i<stopat:
        hexagonals.append(i*(2*i-1))
        i=i+1
    return hexagonals


def testforall(tri,pent,hexa):
    test=0
    n=0
    for num in tri:
        if num>test+500000:
            print (num)
            test=num
        if num in pent and num in hexa:
            print ("I've found it!!",num)
            n=num
            break
    return n

def carryon(start):
    t=start
    p=start*0.9
    h=start*0.8
    stop=start+100000
    num=0
    while num==0:
        num=testforall(triangulars(t,stop),pentagonals(p,stop),hexagonals(h,stop))
        stop=stop+100000
    return num
print (carryon(50000))

    
        
