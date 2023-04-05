import math
f=open("p022_names.txt","r")
names1=str(f.read())

def getnexttarget(string,startpos):
    start=string.find('"',startpos)
    end=string.find('"',startpos+1)
    return string[start+1:end],end+2

def getnames(string):
    names2=[]
    startpos=0
    for i in range(int(string.count('"')/2)):
        name,a=getnexttarget(string,startpos)
        startpos=a
        names2.append(name)
    return names2

names=sorted(getnames(names1))
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getscore(string):
    score=0
    for letter in string:
        score=score+upper.find(letter)+1
    return score

allscores=[]
for name in names:
    allscores.append(getscore(name)*(names.index(name)+1))

overall=0
for score in allscores:
    overall=overall+score
print (overall)
    
