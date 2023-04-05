with open('p059_cipher.txt') as f:
    content=f.readlines()
    content=[x.strip('\n') for x in content]
    content=content[0]
with open('words.txt') as g:
    words=g.readlines()
    words=[x.strip('\n') for x in words]
    
def getnums(string):
    nums=[]
    pos=0
    nums.append(int(string[:string.find(',')]))
    pos+=len(str(nums[-1]))
    while pos<len(string)-3:
        start=string.find(',',pos)
        end=string.find(',',start+1)
        nums.append(int(string[start+1:end]))
        pos=end
    nums.append(int(string[-2:]))
    return nums

encrypted=getnums(content)

codes=[]
lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for a in range(26):
    for b in range(26):
        for c in range(26):
            codes.append(lower[a]+lower[b]+lower[c])
def encrypt(code,start):
    end=[]
    start=list(start)
    codepos=0
    for i in start:
        end.append(chr(ord(i)^ord(code[codepos])))
        codepos+=1
        if codepos==3:
            codepos=0
    return end
def decipher(code,target):
    end=[]
    codepos=0
    for i in target:
        end.append(chr(i^ord(code[codepos])))
        codepos+=1
        if codepos==3:
            codepos=0
    return ''.join(end)

def checkenglish(string):
    splitted=string.split()
    for i in splitted:
        if i in words:
            return True
    return False
def sumascii(string):
    lis=list(string)
    s=0
    for i in lis:
        s+=ord(i)
    return s
#ones=[]
#print(decipher('aaa',encrypted))
#num=0
#for i in codes:
#    d=decipher(i,encrypted)
#    if d.count(' ')>100:
#        ones.append(num)
#    if num%100==0:print(num)
#    num+=1
#print(decipher(codes[367],encrypted))
#for i in ones:
#    print(i,decipher(codes[i],encrypted))
print(sumascii(decipher(codes[4423],encrypted)))
