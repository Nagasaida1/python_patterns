# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 3 4 5
# 4 3 2 3 4 5 6
# 4 3 3 4 5 6 7
# 4 3 4 5 6 7 8
# 4 4 5 6 7 8 9

n=int(input("Enter a number:"))

size =2 * n-1
for i in range(size):
    for j in range(size):
        top=i
        bottom =size - 1 - i
        left=j
        right=size - i - j
        val=n-min(top,bottom,left,right)
        print(val,end=" ")
    print()