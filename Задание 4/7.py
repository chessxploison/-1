def Task7a(n):
    x = 1
    for i in range(2, n + 1):
        x *= i
    return x

def Task7b(n):
    y = 0
    for i in range(1, n + 1):
        y += Task7a(i)
    return y

n = int(input())
x = Task7b(n)
print(x) 
