# *                     
# **
# ***
# ****
# *****

x =int(input("enter a number:"))

for i in range(x):
    for j in range(i+1):
        print("*",end="")
    print()
#------or-------------------------------
for i in range(x):
    print((str(i+1)+'')*(i+1))

for i in range(x):
    for j in range(i+1):
        print(i+1,end='')
    print()

for i in range(x):
    print((chr(65+i)+'')*(i+1))

