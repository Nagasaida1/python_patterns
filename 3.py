# *****
# ****
# ***
# **
# *

n =int(input("enter a number:"))

for i in range(n):
        print("*"*(n-i))

for i in range(n):
    print((str(i+1)+'')*(n-i))

for i in range(n):
        print((chr(65+i)+'')*(n-i))
