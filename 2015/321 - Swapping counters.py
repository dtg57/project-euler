xresults = {1:1, 2:3, 3:10, 4:22, 5:63}
yresults = {1:2, 2:5, 3:10, 4:32, 5:90}

p = 3
q = 2
k = 3
r = 4
s = 3
l = 5

x = 3
y = 5
it = 3

for i in range(20):
    print(it, x, y)
    x = p * xresults[it - 2] + (q * yresults[it - 2]) + k
    y = r * xresults[it - 2] + (s * yresults[it - 2]) + l
    xresults[it] = x
    yresults[it] = y
    it += 2

it = 4
x = 10
y = 10

for i in range(20):
    print(it, x, y)
    x = p * xresults[it - 2] + (q * yresults[it - 2]) + k
    y = r * xresults[it - 2] + (s * yresults[it - 2]) + l
    xresults[it] = x
    yresults[it] = y
    it += 2

s = 0
for i in xresults:
    if i <= 40:
        s += xresults[i]
print(s)
