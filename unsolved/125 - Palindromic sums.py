def ispalindrome(num):
    return num == int(str(num)[::-1])
palins = []
for i in range(1, 10 ** 8):
    if i % 100000 == 0:
        print(i)
    if ispalindrome(i):
        palins.append(i)
