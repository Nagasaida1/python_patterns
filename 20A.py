# E
# D E
# C D E
# B C D E
# A B C D E

n=int(input("Enter a number:"))

for i in range(1,n+1):
    for j in range(1,n+1):
        if(j<=i):
            print(chr(69-i+j),end=' ')
    print()