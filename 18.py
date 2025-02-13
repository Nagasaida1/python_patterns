# 1 2 3 4  17 18 19 20
#   5 6 7  14 15 16
#     8 9  12 13
#       10  11



n = int(input("Enter a number:"))
res = []
l = []
i = 1
r = 0
while r < n:
    l = []
    for k in range(n - r):
        l.append(i)
        i += 1
    l.append('')
    res.append(l)
    r += 1
r -= 1
for j in range(1, n + 1):
    for k in range(n - r):
        res[-j].append(i)
        i += 1
    r -= 1
for l in res:
    x = res.index(l)
    if x > 0:
        print(' ' * (2 * x - 1), end=' ')
    for e in l:
        print(e, end=' ')
    print()