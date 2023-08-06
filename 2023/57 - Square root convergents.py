# Problem 57: Square root convergents
# Solved: 5/4/2023
# Runtime: 00:01
#

num = 3
denom = 2
count = 0

for i in range(1000):
    # x[i+1] = 1 + 1/(x[i] + 1)
    denom, num = num + denom, denom*2 + num
    # Apparently we don't even need to simplify the fraction. Either we got lucky, or there must be a theorem that ensures a+2b and a+b are relatively prime if a and b are relatively prime
    if len(str(num)) > len(str(denom)):
        count += 1

print(count)