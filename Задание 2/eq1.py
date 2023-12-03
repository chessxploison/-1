import math
s = 0.749155
x = 14.26
z = 3.5*10**(-2)
y = -1.22
ans = (2*math.cos(x-0.6666666666666666)/(0.5 + math.sin(y)**2))*(1+(z**2/(3-(z**2/5))))
print(s == round(ans, 6))
