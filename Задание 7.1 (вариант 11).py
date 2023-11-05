def biggest_even(a):
    ev=[]
    for i in range(len(a)):
        if a[i]%2 == 0:
            ev.append(a[i])
    print(max(ev))

ans=[]
n = int(input('Число элементов в списке: '))
for i in range(0, n):
    x = int(input())
    ans.append(x)

biggest_even(ans)
            
