n = int(input("Enter a number:"))
for i in range(n):
    for j in range(n - i):
        print(chr(69 - j-i), end=' ')
    print()