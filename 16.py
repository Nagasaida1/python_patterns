#   *   *
#  * * * *
# *   *   *

n = int(input("Enter a number:"))
for i in range(n):
    for j in range(3 * n):
        if i % 2 == j % 2:
            if (i + j) % 2 == 0:
                if i % 2 != 0:
                    print('*', end='')
                elif (j + i) % 4 != 0:
                    print('*', end='')
                else:
                    print(' ', end='')
            else:
                print(' ', end='')
        else:
            print(' ', end='')
    print()
