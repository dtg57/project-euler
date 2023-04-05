def countdigs(num):
    string=str(num)
    digs=[0,0,0,0,0,0,0,0,0,0]
    for dig in string:
        digs[int(dig)]=digs[int(dig)]+1
    return digs
        
def checkdigs(num,num2):
    if len(str(num))!=len(str(num2)) or countdigs(num)!=countdigs(num2): return False
    else: return True
    
def checkalldigs(num):
    if checkdigs(num,2*num) and checkdigs(num,3*num) and checkdigs(num,4*num) and checkdigs(num,5*num) and checkdigs(num,6*num):
        return True
    else: return False

test=1
n=0
while n==0:
    if checkalldigs(test):
        n=test
        print('Here!',n)
    test=test+1
