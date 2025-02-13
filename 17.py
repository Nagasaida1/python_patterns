#    ****
#   *  *
#  *  *
# ****
n = int(input("Enter a number:"))
print(' ' * (n - 1) + '*' * n)
for i in range(1, n - 1):
    for j in range(2 * n - 2):
        if i + j == n - 1 or i + j == 2 * n - 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print('*' * n)
