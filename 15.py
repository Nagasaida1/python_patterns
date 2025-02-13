# 0
# 1 0
# 0 1 0
# 1 0 1 0
# 0 1 0 1 0

n= int(input("enter a number:"))

for i in range(n):
    for j in range(i+1):
        print((i+j)%2,end=' ')
    print()