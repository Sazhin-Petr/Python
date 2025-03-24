from math import pi

figure = int(input('Введите номер фигуры:\n 1. Окружность \n 2. Прямоугольник \n 3. Трапеция\n : '))
if figure == 1:
    r = int(input('Введите радиус: '))
    print('Площадь окружности радиуса', r, ': ', end='')
    print((lambda R: pi * R ** 2)(r))
elif figure == 2:
    a = int(input('Введите длину: '))
    b = int(input('Введите ширину: '))
    print('Площадь прямоугольника размером', a, '*', b, ': ', end='')
    print((lambda A, B: A * B)(a, b))
elif figure == 3:
    a = int(input('Введите длину: '))
    b = int(input('Введите ширину: '))
    h = int(input('Введите высоту: '))
    print('Площадь трапеции для', 'a', '=', a, 'b', '=', b, 'h', '=', h, ': ', end='')
    print((lambda A, B, H: (A + B) * H / 2)(a, b, h))