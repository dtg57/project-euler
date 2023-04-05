def getpowers(lowera,uppera,lowerb,upperb):
    powers=[]
    for a in range(lowera,uppera+1):
        for b in range(lowerb,upperb+1):
            powers.append(a**b)
    return sorted(set(powers))
print (len(getpowers(2,100,2,100)))























