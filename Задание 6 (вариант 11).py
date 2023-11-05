def max_count(s, key):
    c = m = 0
    for i in range(len(s)):
        if s[i]==key:
            c+=1
            m = max(m,c)
        else:
            c=0
    print(m)
s = str(input())
s1=s.replace('!','.')
max_count(s, 'н')
print(s1)
