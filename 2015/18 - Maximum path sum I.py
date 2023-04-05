import time
now=time.clock()
triangle=[[75],
          [95,64],
          [17,47,82],
          [18,35,87,10],
          [20,4,82,47,65],
          [19,1,23,75,3,34],
          [88,2,77,73,7,63,67],
          [99,65,4,28,6,16,70,92],
          [41,41,26,56,83,40,80,70,33],
          [41,48,72,33,47,32,37,16,94,29],
          [53,71,44,65,25,43,91,52,97,51,14],
          [70,11,33,28,77,73,17,78,39,68,17,57],
          [91,71,52,38,17,14,91,43,58,50,27,29,48],
          [63,66,4,68,89,53,67,30,73,16,69,87,40,31],
          [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]
def getlims(lastrow,lastrowpos):
    if lastrowpos==0:
        return (0,1)
    elif lastrowpos==lastrow-1:
        return (lastrowpos-1,lastrowpos)
    else:
        return (lastrowpos-1,lastrowpos+1)
mx=0
for row15 in range(15):
    r14=getlims(15,row15)
    for row14 in range(r14[0],r14[1]):
        r13=getlims(14,row14)
        for row13 in range(r13[0],r13[1]):
            r12=getlims(13,row13)
            for row12 in range(r12[0],r12[1]):
                r11=getlims(12,row12)
                for row11 in range(r11[0],r11[1]):
                    r10=getlims(11,row11)
                    for row10 in range(r10[0],r10[1]):
                        r9=getlims(10,row10)
                        for row9 in range(r9[0],r9[1]):
                            r8=getlims(9,row9)
                            for row8 in range(r8[0],r8[1]):
                                r7=getlims(8,row8)
                                for row7 in range(r7[0],r7[1]):
                                    r6=getlims(7,row7)
                                    for row6 in range(r6[0],r6[1]):
                                        r5=getlims(6,row6)
                                        for row5 in range(r5[0],r5[1]):
                                            r4=getlims(5,row5)
                                            for row4 in range(r4[0],r4[1]):
                                                r3=getlims(4,row4)
                                                for row3 in range(r3[0],r3[1]):
                                                    r2=getlims(3,row3)
                                                    for row2 in range(r2[0],r2[1]):
                                                        route=triangle[14][row15]+triangle[13][row14]+triangle[12][row13]+triangle[11][row12]+triangle[10][row11]+triangle[9][row10]+triangle[8][row9]+triangle[7][row8]+triangle[6][row7]+triangle[5][row6]+triangle[4][row5]+triangle[3][row4]+triangle[2][row3]+triangle[1][row2]+75
                                                        if route>mx:
                                                            mx=route
                                                            #print(mx,[row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,row13,row14,row15])
print(time.clock()-now)
            
        
