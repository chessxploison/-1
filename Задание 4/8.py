def Task8(n):
    while 1 <= n <= 9:
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end="")
            print()  

n = int(input())

print(Task8(n))
