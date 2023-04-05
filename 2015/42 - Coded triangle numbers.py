import math
f=open("p042_words.txt","r")
words1=str(f.read())

def gettriangles(length):
    triangles=[]
    for i in range(1,length+1):
        triangles.append(0.5*i*(i+1))
    return triangles

def getnexttarget(string,startpos):
    start=string.find('"',startpos)
    end=string.find('"',startpos+1)
    return string[start+1:end],end+2

def getwords(string):
    names2=[]
    startpos=0
    for i in range(int(string.count('"')/2)):
        name,a=getnexttarget(string,startpos)
        startpos=a
        names2.append(name)
    return names2

words=sorted(getwords(words1))

upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getscore(string):
    score=0
    for letter in string:
        score=score+upper.find(letter)+1
    return score

triangles=gettriangles(100)

amount=0

for word in words:
    if getscore(word) in triangles: amount=amount+1

print (amount)
