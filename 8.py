#1
from math import sqrt
 
def checkifprime(x):
    return all(x % i != 0 for i in range(2, int(sqrt(x)+1)))
 
def checkiftwin(x):
    return checkifprime(x) and (checkifprime(x-2) or checkifprime(x+2))
 
n = int(input())
print(*filter(checkiftwin, [x for x in range(n, 2*n+1)]))

#2
from random import randint as rd
def arrmax(arr) :
    amax = arr[0][0]
    n = len(arr)
    for i in range(n) :
        if max(arr[i]) > amax :
            amax = max(arr[i])
    return amax
    
def arrprint(a, b) :
    for i in a :
        print(*i)
    print()
    for i in b :
        print(*i)
    print()
 
na = int(input('Кол-во строк в первой матрице'))
ma = int(input('Кол-во элементов в строке'))
nb = int(input('Кол-во строк в первой матрице'))
mb = int(input('Кол-во элементов в строке'))
 
a = [[rd(1,50) for i in range(ma)] for j in range(na)]
b = [[rd(51,100) for i in range(mb)] for j in range(nb)]
 
arrprint(a,b)
 
amax = arrmax(a)
bmax = arrmax(b)
 
for i in range(len(a)) :
    for j in range(len(a[i])) :
        a[i][j] = bmax if a[i][j] == amax else a[i][j]
for i in range(len(b)) :
    for j in range(len(b[i])) :
        b[i][j] = amax if b[i][j] == bmax else b[i][j]
    
arrprint(a,b)
