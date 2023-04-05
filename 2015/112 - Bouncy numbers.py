def checkbouncy(num):
    num = str(num)
    def checkincreasing(num):
        for i in range(0,len(num)-1):
            if num[i] > num[i+1]:
                return False
        return True
    def checkdecreasing(num):
        for i in range(0,len(num)-1):
            if num[i] < num[i+1]:
                return False
        return True
    return not (checkdecreasing(num) or checkincreasing(num))
count = 0
proportion = 0
test = 99
while proportion < 0.99:
    if test % 10000 == 0:
        print(test, proportion)
    test += 1
    if checkbouncy(test):
        count += 1
    proportion = count/test
print(test)
