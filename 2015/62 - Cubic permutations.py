def checkpermut(num1,num2):
    num1=list(str(num1))
    num2=list(str(num2))
    if len(num1)!= len(num2):
        return False
    for i in num1:
        if i not in num2:
            return False
    for i in num2:
        if i not in num1:
            return False
    for i in range(10):
        if num1.count(str(i))!=num2.count(str(i)):
            return False
    return True
def checkcubes(below,length):
    cubes=[]
    for i in range(1,below):
        cubes.append(i**3)
    for a in cubes:
        print(int(a**(1/3)))
        permuts=[a]
        for b in cubes:
            if len(permuts)==length:
                return permuts
            if checkpermut(a,b) and a!=b:
                permuts.append(b)              
print(checkcubes(10000,5))
