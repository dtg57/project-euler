# Problem 79: Passcode derivation
# Solved: 02/08/23
# Runtime 00:00.59

from itertools import permutations

# returns array of indices of character ch within string s
def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

# returns dictionary of arrays giving indices of occurences of all the digits 0-9 within strings
def occurencesDict(s):
    d = {}
    for i in range(10):
        d[str(i)] = findOccurrences(s, str(i))
    return d

with open('p079_keylog.txt') as file:
    attempts = [x.strip ('\n') for x in file.readlines()]

counts = {i:0 for i in range(10)}

for triple in attempts:
    for i in range(10):
        str_i = str(i)
        count = triple.count(str_i)
        if count > counts[i]:
            counts[i] = count

min_len = sum(counts.values())

base_perm = ''
for i in counts:
    for j in range(counts[i]):
        base_perm += str(i)

perms = [''.join(p) for p in permutations(base_perm)]
works = []

for perm in perms:
    occurences = occurencesDict(perm)
    bool_works = True
    for attempt in attempts:
        best_first = min(occurences[attempt[0]])
        best_last = max(occurences[attempt[2]])
        if best_first > best_last:
            bool_works = False
            break
        else:
            for occurence in occurences[attempt[1]]:
                if not best_first < occurence < best_last:
                    bool_works = False
                    break
            if not bool_works:
                break
    if bool_works:
        works.append(perm)

print(works)
