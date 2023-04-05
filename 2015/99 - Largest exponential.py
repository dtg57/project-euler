import math
with open('p099_base_exp.txt') as file:
    lines = file.readlines()
pairs = []
for pair in lines:
    comma = pair.find(',')
    pairs.append([int(pair[:comma]), int(pair[comma + 1:].strip('\n'))])

answers = {}
for i in range(1000):
    pair = pairs[i]
    answers[pair[1] * math.log(pair[0])] = i
print(answers[max(answers)] + 1)
