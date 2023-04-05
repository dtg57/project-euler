import time
now=time.clock()
with open('p067_triangle.txt') as file:
    content=file.readlines()
    content=[x.strip('\n') for x in content]
data=[]
def getnums(row):
    end=[]
    row=row.split()
    for i in row:
        if i[0]=='0':
            end.append(int(i[1]))
        else:
            end.append(int(i))
    return end
for i in content:
    data.append(getnums(i))
for row in range(98,-1,-1):
    for el in range(0,row+1):
        if data[row+1][el]>data[row+1][el+1]:
            data[row][el]+=data[row+1][el]
        else:
            data[row][el]+=data[row+1][el+1]
print(data[0])

print(time.clock()-now)
