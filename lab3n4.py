import random

z=0
while z<3:
    x = random.randint(1,10)
    y = random.randint(1,10)
    print(x, '+', y, '=')
    otvet = int(input('введите ответ '))
    if x + y != otvet:
        z = z + 1
if z == 3:
    print('игра окончена')

