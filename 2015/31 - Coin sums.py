import math
ways=1
check=0             
for c1 in range(201):
    for c2 in range(math.ceil(101-(c1/2))):
        for c5 in range(math.ceil(41-c1/5-c2/2.5)):
            for c10 in range(math.ceil(21-c1/10-c2/5-c5/2)):
                for c20 in range(math.ceil(11-c1/20-c2/10-c5/4-c10/2)):
                    for c50 in range(math.ceil(5-c1/50-c2/25-c5/10-c10/5)):
                        for c100 in range(math.ceil(3-c1/100-c2/50-c5/20-c10/10)):
                            if c1!=check:
                                print(c1,ways)
                                check=c1
                            if c1+c2*2+c5*5+c10*10+c20*20+c50*50+c100*100==200:
                                ways+=1
                        
print(ways)
