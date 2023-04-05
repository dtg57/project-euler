evens = ['2', '4', '6', '8', '0']
done = {}

def reverse(n):
    return int(n[::-1])
def reversible(n):
    global reverse
    global done
    if n in done:
        return done[n]
    s = str(n)
    r = reverse(s)
    if n % 2 == r % 2:
        done[n] = False
        done[r] = False
        return False
    if s[-1] == '0':
        done[n] = False
        done[r] = False
        return False
    reverse = str(n + r)
    for i in evens:
        if i in reverse:
            done[n] = False
            done[r] = False
            return False
    done[n] = True
    done[r] = True
    return True

c = 0
for i in range(1, 10 ** 3):
    if i%2 == int(str(i)[::-1]) % 2:
        continue
    if reversible(i):
        c += 1
print(c)
    
    
