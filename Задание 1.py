#2
print('Курс Основы программирования начался')
#3
a=16823
b=12302
c=a*b
v=3092
k=c%v
print('k =',k)
#4
name=str(input('Укажите свое имя'))
while name != ('Иван'):
    age=int(input('Укажите свой возраст'))
    if age >= 16 and age < 75:
        print('Поздравляем, вы поступили в ВГУИТ')

    elif age < 16 and age > 0:
        print('Сначала нужно окончить школу!')

    if age < 16:
        print('Вам осталось учиться в школе:',16-age )

#5
seconds = int(input('Колличество секунд'))
days = seconds // 86400 
hours = (seconds % 86400) // 3600 
minutes = (seconds % 3600) // 60 
sec = seconds % 60 
print(days, hours, minutes, sec)

#6
n=int(input('Введите число'))
b=n + n**2 + n**3 + n**4 + n**5
print(b)

#7
a=int(input('Введите значение a'))
b=int(input('Введите значение b'))
c=a
a=b
b=c
print('a=',a)
print('b=',b)

#8
a=int(input('Введите a:'))
if a%2 == 0:
    print ('Четное число')
else:
    print('Нечетное число')
