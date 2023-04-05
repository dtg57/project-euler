with open('p054_poker.txt') as file:
    lines = [x.strip('\n') for x in file.readlines()]
hands = []

def correctvalue(cardvalue):
    if cardvalue == 'T':
        return 10
    if cardvalue == 'J':
        return 11
    if cardvalue == 'Q':
        return 12
    if cardvalue == 'K':
        return 13
    if cardvalue == 'A':
        return 14
    return int(cardvalue)

for i in lines:
    hands.append([])
    cards = i.split()
    person1 = cards[:5]
    person2 = cards[5:]
    cards1 = []
    cards2 = []
    for a in person1:
        cards1.append((correctvalue(a[0]), a[1]))
    for b in person2:
        cards2.append((correctvalue(b[0]), b[1]))
    hands[-1].append(cards1)
    hands[-1].append(cards2)
    
def getvalues(hand):
        values = []
        for i in hand:
            values.append(i[0])
        return values
    
def getsuits(hand):
    suits = []
    for i in hand:
        suits.append(i[1])
    return suits

def checkstraight(values):
    for i in range(1,5):
        if values[0] + i != values[i]:
            return False, 0
    return True, values[-1]
        
def getsuitachs(hand):
    def checkflush(hand):
        return len(set(getsuits(hand))) == 1, getbestcard(hand)
    def checkstraightflush(hand):
        return len(set(getsuits(hand))) == 1 and checkstraight(getvalues(hand)), getbestcard(hand)
    def checkroyalflush(hand):
        if not checkflush(hand):
            return False, 0
        values = getvalues(hand)
        for i in range(10,15):
            if i not in values:
                return False, 0
        return True, getbestcard(hand)
    RF = checkroyalflush(hand)
    if RF[0]:
        return 'RF', RF[1]
    SF = checkstraightflush(hand)
    if SF[0]:
        return 'SF', SF[1]
    FL = checkflush(hand)
    if FL[0]:
        return 'FL', Fl[1]
    return 'JK', 0

def getvalueachs(hand):
    def checkFH(counts):
        checks = [False, False]
        for i in counts:
            if i[1] == 3:
                checks[0] = True
            if i[1] == 2:
                checks[1] = True
        if False not in checks:
            for i in counts:
                if i[1] == 3:
                    return True, i[0]
        return False, 0
    def checkFK(counts):
        for i in counts:
            if i[1] == 4:
                return True, i[0]
        return False, 0
    def checkTK(counts):
        for i in counts:
            if i[1] == 3:
                return True, i[0]
        return False, 0
    def checkTP(counts):
        total = [0,0]
        for i in counts:
            if i[1] == 2:
                total[0] += 1
                if i[0] > total[1]:
                    total[1] = i[0]
        if total[0] == 2:
            return True, total[1]
        return False, 0
    def checkOP(counts):
        for i in counts:
            if i[1] == 2:
                return True, i[0]
        return False, 0
    values = getvalues(hand)
    repets = []
    for i in values:
        count = values.count(i)
        if count > 1:
            repets.append((i, count))
    counts = list(set(repets))
    ST = checkstraight(sorted(values))
    if ST[0]:
        return 'ST', ST[1]
    FH = checkFH(counts)
    if FH[0]:
        return 'FH', FH[1]
    FK = checkFK(counts)
    if FK[0]:
        return 'FK', FK[1]
    TK = checkTK(counts)
    if TK[0]:
        return 'TK', TK[1]
    TP = checkTP(counts)
    if TP[0]:
        return 'TP', TP[1]
    OP = checkOP(counts)
    if OP[0]:
        return 'OP', OP[1]
    return 'JK',0

def checkhand(hand):
    achs = ['JK','OP','TP','TK','ST','FL','FH','FK','SF','RF']
    valueAch = getvalueachs(hand)
    suitAch = getsuitachs(hand)
    valueindex = achs.index(valueAch[0])
    suitindex = achs.index(suitAch[0])
    if valueindex > suitindex:
        return valueAch
    else:
        return suitAch
    
def getbestcard(hand):
    return max(getvalues(hand))

def getbetter(hand1, hand2):
    achs = ['JK','OP','TP','TK','ST','FL','FH','FK','SF','RF']
    hand1ach = checkhand(hand1)
    hand2ach = checkhand(hand2)
    index1 = achs.index(hand1ach[0])
    index2 = achs.index(hand2ach[0])
    best1 = getbestcard(hand1)
    best2 = getbestcard(hand2)
    
    if index1 > index2:
        return 1
    if index2 > index1:
        return 2
    if index2 == index1:
        if index1 == 0 and index2 == 0:
            if best1 > best2:
                return 1
            if best2 > best1:
                return 2
            print(hand1, hand2)
        if hand1ach[1] > hand2ach[1]:
            return 1
        if hand2ach[1] > hand1ach[1]:
            return 2
        if hand1ach[1] == hand2ach[1]:
            print(hand1, hand2)
    
    

pos = 0
winsfor1 = 0
for i in hands:
    print(pos)
    if getbetter(i[0], i[1])==1:
        winsfor1 += 1
    pos += 1
print(winsfor1)
    
        
            
            
