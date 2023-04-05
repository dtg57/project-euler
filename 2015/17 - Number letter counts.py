import math

def xor(boola,boolb):
    if boola==True and boolb==True:
        return False
    if boola==True and boolb==False:
        return True
    if boola==False and boolb==True:
        return True
    if boola==False and boolb==False:
        return False

def writtenforms(number):
    num=str(number)
    onedigit=['','one','two','three','four','five','six','seven','eight','nine']
    teens=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens=['','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    units=onedigit[int(num[-1])]
    if len(num)==1:
        written=onedigit[int(num)]
    if len(num)==2 and int(num[0])==1:
        written=teens[int(num[1])]
    if len(num)==2 and int(num[0])!=1:
        written=tens[int(num[0])-1]+onedigit[int(num[1])]
    return written
    
def writtenformc(number):
    num=str(number)
    onedigit=['','one','two','three','four','five','six','seven','eight','nine']
    teens=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens=['','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    units=onedigit[int(num[-1])]
    if len(num)<3:
        written=writtenforms(number)
    if len(num)>2:
        tensunits=writtenforms(int(num[-2:]))
        hundreds=onedigit[int(num[-3])]
        if len(num)>3:
            thousands=onedigit[int(num[-4])]
    if len(num)==3 and int(num[-1])==0 and int(num[-2])==0:
        written=hundreds+'hundred'
    if len(num)==3 and not((int(num[-1])==0)and(int(num[-2])==0)):
        written=hundreds+'hundredand'+tensunits
    if len(num)==4:
        thousands=onedigit[int(num[0])]
        if int(num[-1])==0 and int(num[-2])==0 and int(num[-3])==0:
            written=thousands+'thousand'
    return written

all=''
for i in range(1,1001):
    all=all+writtenformc(i)
    print (str(i) + ' ' + str(len(writtenformc(i))))
print (all, len(all))

    
    

