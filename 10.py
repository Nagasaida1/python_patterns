    #     *
    #    * *
    #   *   *
    #  *     *
    # *       *
    #  *     *
    #   *   *
    #    * *
    #     *

n=int(input("Enter a Number:"))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        if k == 0 or k == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        if k == 0 or k == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

