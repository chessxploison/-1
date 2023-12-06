name=str(input('Укажите свое имя'))
while name != ('Иван'):
    age=int(input('Укажите свой возраст'))
    if age >= 16 and age < 75:
        print('Поздравляем, вы поступили в ВГУИТ')

    elif age < 16 and age > 0:
        print('Сначала нужно окончить школу!')

    if age < 16:
        print('Вам осталось проучиться ещё:',16-age )
