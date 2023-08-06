# Problem 80: Square Root Digital Expansion
# Solved: 02/08/23
# Runtime: 00:00.005

import decimal
decimal.getcontext().prec = 200

n = 100

squares = []

for i in range(1,n):
    sq = i**2
    if sq > n:
        break
    else:
        squares.append(sq)

digital_sum = 0
for i in range(1,n+1):
    if i in squares:
        continue
    sqrt = decimal.Decimal(i).sqrt()
    sqrt = str(sqrt)
    sqrt = sqrt.replace('.', '')
    sqrt = sqrt[:100]
    for digit in sqrt:
        digital_sum += int(digit)

print(digital_sum)