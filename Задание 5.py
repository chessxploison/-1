def task_1(n):
    ans=[]
    sqr=1
    for i in range(1, 100):
        while sqr<n:
            sqr=i**2
            ans.append(sqr)
    print(ans)
task_1(int(input()))

def task_2(n):
    i = 2
    while n % i != 0:
        i += 1
    print(i)

task_2(int(input()))

def task_3(n):
    n = int(input())
    twopow = 2
    powr = 1
    while twopow <= n:
        twopow *= 2
        powr += 1
    print(powr - 1, twopow // 2)

task_3(int(input()))

def task_4(x,y):
    i = 1
    while x < y:
        x *= 1.1
        i += 1
    print(i)
task_4(int(input()),int(input()))

def task_5(a):
    n = 0
    while True:
        if a == 0:
            break
        n += 1
    print(n)

a = int(input())
task_5(a)

def task_6(n):
    sum = 0
    len = 0
    while n != 0:
        sum += n
        len += 1
        n = int(input())
    print(sum / len)

n = int(input())
task_6(n)

task_7(x,y):
    k = 0
    while x != 0:
        if y != 0 and x < y:
            k += 1
        x = y
    print(k)
    
x = int(input())
y = int(input())
task_7(x,y)

def task_8(cur):
    n = 1
    n_max = 0
    cur = -1
    prev = -1
    while True:
        if cur == 0:
            break
        if prev != -1:
            if cur == prev:
                n += 1
            else:
                if n_max < n:
                    n_max = n
                n = 1
        prev = cur

    if n > n_max:
        n_max = n

    print(n_max)

cur = int(input())
task_8(cur)
