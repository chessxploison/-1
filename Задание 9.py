#1
import random  
def createArr():
    r = 0
    x = int(input())
    y = int(input())
    arr = []
    for i in range(x):
        arr.append([])
        for j in range(y):
            arr[i].append(random.randint(0,100))
            r += 1  
    return arr

lenm, numlines, l = int(input('Длина строки')), int(input('Кол-во строк')), []
m=arr()
for i in m:
    l+=[min(i)]
print(m)
print(sum(m[l.index(min(l))]))

#2
from random import randint
from operator import mul
from functools import reduce
 
 
def mprint(matrix):
    for row in matrix:
        for item in row:
            print()
        print()
 
 
n = int(input())
 
matrix = [[randint(-10, 10) for _ in range(n)] for _ in range(n)]
mprint(matrix)
print()
 
tmatrix = list(zip(*matrix))
ps = [reduce(mul, row) for row in tmatrix]
min_p = min(ps)
idx = ps.index(min_p)
 
if idx < n - 1:
    tmatrix[idx], tmatrix[idx + 1] = tmatrix[idx + 1], tmatrix[idx]
else:
    tmatrix[idx], tmatrix[idx - 1] = tmatrix[idx - 1], tmatrix[idx]
 
matrix = list(zip(*tmatrix))
mprint(matrix)
