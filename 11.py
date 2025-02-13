
n = int(input("Enter the number: "))

for i in range(n):
    print(" " * (n - i - 1), end="")
    value = 1
    for j in range(i + 1):
        print(f"{value} ", end="")
        value = value * (i - j) // (j + 1)
    print()
