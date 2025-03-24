# from math import sqrt, pi
#
#
# def square(fig):
#     if fig == 1:
#         a = int(input('Введите сторону a = '))
#         b = int(input('Введите сторону b = '))
#         c = int(input('Введите сторону c = '))
#         p = (a + b + c) / 2
#         print(round(sqrt(p * (p - a) * (p - b) * (p - c)), 2))
#     elif fig == 2:
#         a = int(input('Введите сторону a = '))
#         b = int(input('Введите сторону b = '))
#         print(a * b)
#     elif fig == 3:
#         a = int(input('Введите радиус = '))
#         print(round(pi * a ** 2, 2))
#
#
# fig = int(input('Выбор фигуры:\n 1 - треугольник\n 2 - квадрат\n 3 - круг\n : '))
# square(fig)


n = int(input())
cnt = 0
for i in range(1, n+1):
    cnt += ((-1) ** i + 1) * n
print(cnt)
