from fractions import Fraction
c=0
start='1+1/'
def findnumden(fraction):
    pos=fraction.find('/')
    if len(fraction[:pos])>len(fraction[pos+1:]):
        return True
for i in range(999):
    start+='(2+1/'
    s=start+'2'
    for b in range(s.count('(')):
        s+=')'
    e=eval(s)
    #print(s)
    #print(e)
    frac=str(Fraction(e).limit_denominator(10000000000000))
    print(frac)
    if findnumden(frac):
        c+=1
print(c)
