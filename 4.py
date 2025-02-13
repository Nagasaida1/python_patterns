# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = int(input("enter a  number: "))

for i in range(n):
    for j in range(i+1):
        print(j+1, end=' ')
    print()

for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=' ')
    print()

