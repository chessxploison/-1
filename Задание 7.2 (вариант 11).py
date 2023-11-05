def max_ev(a):
    lst2 = []
    for el in lst1:
        if el % 2 ==0 and el < 10:
            lst2.append(el)
    if len(lst2) == 0:
        print('Нет таких чисел')
 
    print(sorted(lst2, reverse=False))

lst1 = []
n = int(input('Число элементов в списке: '))
for i in range(0, n):
    x = int(input())
    lst1.append(x)

max_ev(lst1)
