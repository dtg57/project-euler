# Problem 610: Roman numerals II
# Solved: 18/12/2020
# Runtime: hours - I solved this by generating many (up to 10^8) roman numerals and taking the average, inefficient

import math
from random import random

validfollowers = {
    'III' : [],
    'II' : ['I'],
    'VI' : ['I'],
    'XI' : ['V', 'I', 'X'],
    'IV' : [],
    'IX' : [],
    'I' : ['X', 'V', 'I'],
    'V' : ['I'],
    'X' : ['X', 'I', 'V', 'L', 'C'],
    
    'XXX' : ['I', 'V'],
    'XX' : ['X', 'I', 'V'],
    'LX' : ['X', 'I', 'V'],
    'CX' : ['V', 'I', 'X', 'L', 'C'],
    'XL' : ['I', 'V'],
    'XC' : ['I', 'V'],
    'L' : ['X', 'V', 'I'],
    'C' : ['I', 'V', 'L', 'C', 'X', 'M', 'D'],

    'CCC' : ['I', 'V', 'X', 'L'],
    'CC' : ['X', 'I', 'V', 'C', 'L'],
    'DC' : ['X', 'I', 'V', 'C', 'L'],
    'MC' : ['V', 'I', 'X', 'L', 'C', 'M', 'D'],
    'CD' : ['I', 'V', 'X', 'L'],
    'CM' : ['I', 'V', 'X', 'L'],
    'D' : ['X', 'V', 'I', 'C', 'L'],
    'M' : ['I', 'V', 'L', 'C', 'X', 'M', 'D'],
}

def checkValid(numeralstring):
    global validfollowers
    length = len(numeralstring)
    if length == 1:
        return True
    for i in range(0, length - 1):
        num = numeralstring[i]
        if i == 0:
            if numeralstring[i + 1] not in validfollowers[num]:
                return False
        elif i == 1:
            if numeralstring[i - 1:i + 1] in validfollowers:
                if numeralstring[i + 1] not in validfollowers[numeralstring[i - 1:i + 1]]:
                    return False
            else:
                if numeralstring[i + 1] not in validfollowers[num]:
                    return False
        else:
            if numeralstring[i - 2:i + 1] in validfollowers:
                if numeralstring[i + 1] not in validfollowers[numeralstring[i - 2:i + 1]]:
                    return False
            elif numeralstring[i - 1:i + 1] in validfollowers:
                if numeralstring[i + 1] not in validfollowers[numeralstring[i - 1:i + 1]]:
                    return False
            else:
                if numeralstring[i + 1] not in validfollowers[num]:
                    return False

    return True

def checkValidNew(newDigit, currentNumeral):
    global validfollowers
    length = len(currentNumeral)
    if length == 0:
        return True
    if length == 1:
        return newDigit in validfollowers[currentNumeral]
    if length == 2:
        if currentNumeral in validfollowers:
            return newDigit in validfollowers[currentNumeral]
        else:
            return newDigit in validfollowers[currentNumeral[-1]]
    if currentNumeral[-3:] in validfollowers:
        return newDigit in validfollowers[currentNumeral[-3:]]
    if currentNumeral[-2:] in validfollowers:
        return newDigit in validfollowers[currentNumeral[-2:]]
    return newDigit in validfollowers[currentNumeral[-1]]


values = {
    'M' : 1000,
    'D' : 500,
    'C' : 100,
    'L' : 50,
    'X' : 10,
    'V' : 5,
    'I' : 1,
    'CM' : 900,
    'CD' : 400,
    'XC' : 90,
    'XL' : 40,
    'IX' : 9,
    'IV' : 4,
}

def value(numeral):
    global values
    if len(numeral) == 0:
        return 0
    s = 0
    i = 0
    length = len(numeral)
    while i < length:
        if i < length - 1 and numeral[i:i + 2] in values:
            s += values[numeral[i:i + 2]]
            i += 2
        else:
            s += values[numeral[i]]
            i += 1
    return s

def randToDigit(n):
    x = n / 0.14
    if x < 1: return 'M'
    if x < 2: return 'D'
    if x < 3: return 'C'
    if x < 4: return 'L'
    if x < 5: return 'X'
    if x < 6: return 'V'
    if x < 7: return 'I'
    return False

def getValidNext(currentNumeral):
    global validfollowers
    length = len(currentNumeral)
    if length == 0:
        return ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    if length == 1:
        return validfollowers[currentNumeral]
    if length == 2:
        if currentNumeral in validfollowers:
            return validfollowers[currentNumeral]
        else:
            return validfollowers[currentNumeral[-1]]
    if currentNumeral[-3:] in validfollowers:
        return validfollowers[currentNumeral[-3:]]
    if currentNumeral[-2:] in validfollowers:
        return validfollowers[currentNumeral[-2:]]
    return validfollowers[currentNumeral[-1]]

def cumulate(prob, numeral):
    global expected, probs, p, p0
    val = value(numeral)
    if val % 1000 == 0:
        print(numeral, ' ', val, ' ', prob)
    followers = getValidNext(numeral)
    if len(followers) == 0 or val * prob <= 0.000000000000001:
        #
        # if no possible followers then must stay on this numeral
        #
        expected[val] = prob
        return
    #
    # adding on probability of stopping on this numeral
    #
    newprob = prob * probs[len(followers)]
    expected[val] = newprob * p0
    for follower in followers:
        #
        # prob of reaching next number is prob * p / (1 - (7 - p*len(followers))) = newprob * p
        #
        cumulate(newprob * p, numeral + follower)
        
p = 0.14
p0 = 0.02
expected = {}

probs = {
    1 : 1 / (1 - 6*p),
    2 : 1 / (1 - 5*p),
    3 : 1 / (1 - 4*p),
    4 : 1 / (1 - 3*p),
    5 : 1 / (1 - 2*p),
    6 : 1 / (1 - 1*p),
    7 : 1,
}

#cumulate(1, 'I')


def generateNumeral(currentNumeral):
    if len(currentNumeral) > 1:
        if currentNumeral[-2:] in ['IV', 'IX']:
            return currentNumeral
        if len(currentNumeral) > 2 and currentNumeral[-3:] == 'III':
            return currentNumeral
    n = random()
    newDigit = randToDigit(n)
    if not newDigit:
        return currentNumeral
    else:
        if checkValidNew(newDigit, currentNumeral):
            return generateNumeral(currentNumeral + newDigit)
        else:
            return generateNumeral(currentNumeral)

def expectedValue(expected):
    s = 0
    for val in expected:
        s += val * expected[val]
    return s

denoms = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
expecteds = {}

for denom in denoms:
    expected = {}
    cumulate(1, denom)
    expecteds[denom] = expectedValue(expected)



total = 0
vals = {}


for i in range(1, 10**8 + 1):
    numeral = generateNumeral('')
    if not checkValid(numeral):
        print(numeral)
        raise NameError('Invalid Roman Numeral')
    val = value(numeral)
    total += value(numeral)
    if val in vals:
        vals[val] += 1
    else:
        vals[val] = 1
    if i%10000==0:
        print(numeral, ' ', total / i)

#for val in vals:
#    print(val, ' ', vals[val] / 10**6)


