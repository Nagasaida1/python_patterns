# *    
# **   
# ***  
# **** 
# *****
# **** 
# ***  
# **


n= int(input("enter a number:"))

for i in range(n):
    print(('*')*(i+1))
for i in range(n-1):
    print(('*')*(n-i-1))


for i in range(n):
    print((str(i+1)+'')*(i+1))
for i in range(n-1):
    print((str(n-i-1)+'')*(n-i-1))


for i in range(n):
    print((chr(65+i)+'')*(i+1))
for i in range(n-1):
    print((chr(63+n-i)+'')*(n-i-1))