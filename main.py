# name = 'admin'
# print('Hello', name)
# age = 20.2
# print(age)
#
#
# print(type(name))
#
# print(type(age))
#
# print(id(name))
# print(id(age))
# from itertools import count
# from subprocess import check_output


# a = b = c = 10
# a, b, c = 5, 'Hello', 7.2
# print(a)
# print(b)
# print(c)

# name = 'admin'
# print(name)

# import keyword
# print(keyword.kwlist)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 5
# print(a)
# a = 'Hello'
# print(a)
# a = 1.2
# print(1.2)

# a = 5
# b = 20
# print('a:', a)
# print('b:', b)
#
# c = a  # 1
# a = b  # 2
# b = c  # 1
#
# print('a:', a)
# print('b:', b)

# print('строка \
#       символов')
# print("\tстр\nка \n\tсимв   олов")

# print('Документ \'file.txt\' находится по пути: \rD:\\folder\\file.txt')


# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"  # конкатенация
# print(s3)
# s4 = s3 * 5
# print(s4)

# print(6 + 2)
# print(6.2 + 2.4)
# print(6 - 2)
# print(6 * 2)
# print(7 / 2)
# print(6 / 2)
#
#
# print(7 // 2)
# print(6 // 2)
#
# print(6 ** 2)
#
# print(7 % 2)

# a = 5
# b = 7
# c = 3
# d = a + b + c
# print('Сумма чисел равна:', d)
# f = a * b * c
# print(f)
# g = d/3
# print(g)

# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# a = 5
#
# a += 3  # a = a + 3
# print(a)  # 8
#
# a -= 3  # a = a - 3, где a теперь 8
# print(a)  # 5
#
# a *= 4  # a = a * 4, a теперь 5
# print(a)  #20


# num = 9753
# print('Исходное число:', num)
# a = num % 10
# print('a:', a)
# num = num // 10
# # print(num)
# b = num % 10
# print('b:', b)
# num = num // 10
# print(num)
# c = num % 10
# print('c:', c)
# num = num // 10
# # print(num)
# d = num % 10
# print('d:',d)
# print('Обратное число:', a * 1000 + b * 100 + c * 10 + d)
#
# num = 4321
# print('Исходное число:', num)
# res = num % 10
# # res = num % 10 * 1000  #1000
# # num //= 10
# # res += num % 10 * 100  #200   res = res + num % 10 * 100
# # num //= 10
# # res += num % 10 * 10
# # num //= 10
# # res += num % 10
# print('Обратное число:', res)

# num1 = '2'
# num2 = 3
# # res = int(num1) + num2   # преобразовали строку в число командой int
# res = num1 + str(num2)  # преобразовали число 3 в строку командой str, получилась конкатенация
# print(res)

# print(int(3.981))
# print(type(round(3.581)))
# print(round(3.599, 2))

# num1 = "2.5"
# num2 = 10
# res = float(num1) + num2  # 2,5 + 10
# print(res)

# name = 'Виктор'
# age = 20
# print('Меня зовут', name, '. Мне', age, 'лет.')
# print('Меня зовут ' + name + '. Мне ' + str(age) + ' лет.')
# print('Меня зовут ', name, '. Мне ', age, ' лет.', sep='', end=' ')
# print('Hello Python')

# name = input('Введите имя: ')
# print('Hello,', name)


# num = int(input('Введите число: '))
# power = int(input('Введите степень: '))
# res = num ** power  # 5**2
# print('Число', num, 'в степени', power, 'равно: ', res)


# num1 = int(input('Введите число 1:'))
# num2 = int(input('Введите число 2:'))
# num3 = int(input('Введите число 3:'))
# num4 = int(input('Введите число 4:'))
# res1 = num1 + num2
# res2 = num3 + num4
# res3 = res1 / res2
# print(round(res3, 2))


# b1 = True
# b2 = False
#
# print(int(b1))  # 1
# print(int(b2))  # 0
# print(b1 + 5)  # 1 + 5 = 6
# print(b2 + 5)  # 0 + 5 = 5

# print(bool('Python'))
# print(bool(0))
# print(bool(''))
# print(bool(True))
# print(bool(False))
# print(bool(None))


# test = None
# print(test)
# print(type(test))
# test = 5
# print(test)

# print(5 == 5)
# print(5 == 3)
# print(2 + 5 == 3 + 4)  # 2 + 5 == 3 + 4  7 == 7
# print(2 + 5 != 3 + 4)  # 2 + 5 == 3 + 4  7 == 7
# print(8 > 5)
# print(8 >= 8)
# print(5 < 10)
# print(5 <= 5)
# print('hello' > 'Hello')  # 104 > 72 по коду символа сравниваются строки

# print(2 < 4 < 9)  # True (2<4)  :  True (4<9) => True
# print(2 > 4 < 9)  # False (2>4)  :  True (4<9) => False
#
# print(2 * 5 > 7 >= 4 + 3)  # 10 > 7 >= 7  True : true => True
# print(3 * 3 <= 7 >= 2)  # 9 <= 7 >= 2  False  : True  => False

# print(5 - 3 == 2 and 1 + 3 == 4) # 5 - 3 == 2 and 1 + 3 == 4 => True True сначала арифметические действия
# print(5 - 3 == 2 and 1 + 3 < 4) #  True n False
# print(5 - 3 > 2 and 1 + 3 == 4) #  False n True
# print(5 - 3 > 2 and 1 + 3 < 4) #  False n False

# print(5 - 3 == 2 or 1 + 3 == 4) # 5 - 3 == 2 and 1 + 3 == 4 => True True сначала арифметические действия
# print(5 - 3 == 2 or 1 + 3 < 4) #  True n False
# print(5 - 3 > 2 or 1 + 3 == 4) #  False n True
# print(5 - 3 > 2 or 1 + 3 < 4) #  False n False

# print(not 9 - 5)  # not 4(True) => False not меняет на противопложный
# print(not 7 - 7)  # not False => True

# a = 15
# b = 10
# if a > b:
#     print( a, '>', b)

# a = 10
# b = 10
# if a > b:
#     print(a, '>', b)
# if b > a:
#     print(b, '>', a)
# if b == a:
#     print(b, '==', a)

# cnt = 5
# if cnt < 10:
#     cnt += 1
# print(cnt)

# cnt = 5
# if cnt < 10:
#     cnt += 1
# else:
#     cnt -= 1
# print(cnt)

# a = 40
# b = 40
# if a > b:
#     print(a, '>', b)
# elif b == a:  # else if
#     print(b, '==', a)
# else:
#     print(b, '>', a)

# age = int(input('Введите свой возраст:'))
# if age >= 18:
#     print('Доступ разрешен')
#     print('Приятного просмотра')  # если больше одной строки, то разное кол-во строк будет ошибкой
# else:
#     print('Доступ запрещен!')

# a = input('Введите первую сторону: ')
# b = input('Введите вторую сторону: ')
# c = input('Введите третью сторону: ')
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a == b or a == c or b == c:
#     print('Треугольник равнобедренний')
# else:
#     print('Треугольник разносторонний')

# day = int(input(' ВВедите день недели (цифрой):'))
# if 1 <= day <= 5: #(day >= 1) and (day <=5):
#     print('Рабочий день - ', end='')
#     if day == 1:
#         print('понедельник')
#     if day == 2:
#         print('вторник')
#     if day == 3:
#         print('среда')
#     if day == 4:
#         print('четверг')
#     if day == 5:
#         print('пятница')
# elif day == 6 or day == 7:
#     print('Выходной день - ', end='')
#     if day == 6:
#         print('суббота')
#     if day == 7:
#         print('воскресенье')
# else:
#     print('Такого дня недели не существует!')

# month = int(input('Введите номер месяца:'))
# if  (month == 12) or (1 <= month <=2):
#     print('Зима')
# elif 3 <= month <=5:
#     print('Весна')
# elif 6 <= month <= 8:
#     print('Лето')
# elif 9 <= month <= 11:
#     print('Осень')
# else:
#     print('Ошибка ввода данных')

# 1) от 0 до 9
# 2) 1 - ворона, 2 - вороны, 3 вороны, 4 - вороны, 5 - ворон, 6 - ворон, 7 - ворон, 8 - ворон, 9 - ворон, 0 - ворон

# n = int(input('Введите количество ворон:'))
# if 0<= n <= 9:
#     print('На ветке ', end='')
#     if n == 1:
#         print(n, 'ворона')
#     if 2 <= n <= 4:
#         print(n, 'вороны')
#     if 5 <= n <= 9 or n == 0:
#         print(n, 'ворон')
# else:
#     print('Ошибка ввода данных')

# n = int(input('Введите количество ворон:'))
# if 0 <= n <= 9:
#     print('На ветке ', end='')
#     if n == 1:
#         print(n, 'ворона')
#     elif 2 <= n <= 4:
#         print(n, 'вороны')
#     else:
#         print(n, 'ворон')
# else:
#     print('Ошибка ввода данных')

# match выражение:
#     case шаблон_1:
#         действие_1
#     case шаблон 2:
#         действие_2
#         действие по умолчанию

# password = 'qwerty'
#
# match password:
#     case 'admin':
#         print('Администратор')
#     case 'user':
#         print('Пользователь')
#     case _:
#         print('Пароль не верен')

# day = 'вторник'
# time = 10
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 12 or 14 <= time <= 17:
#         print('Рабочий день')
#     case 'суббота' | 'воскресенье':
#         print('Выходной день')
#     case _:
#         print('Такого дня недели не существует или не рабочее время')

# a, b = 30, 20
#
# print(a if a < b else b )

# a, b = 20, 20
# print('a == b' if a == b else 'a > b' if a > b else 'b > a')

# a = int(input('Введите число: '))
# kop = a   # 55
# if 11 <= kop <= 14:
#     print(a, 'копеек')
# elif 1 <= kop <= 99:
#     kop = kop % 10
#     if kop == 1:
#         print(a, 'копейка')
#     elif 2 <= kop <= 4:
#         print(a, 'копейки')
#     else:
#         print(a, 'копеек')
# else:
#     print('недопустимое значение')


# a = 5
# b = 0
# print(a / b)

# try:   #попытаться
#     n = int(input('Ввeдите целое число: '))
#     print(n * 2)
# except ValueError:
#     print('Что-то пошло не так')

# try:
#     n = int(input('Введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except ValueError:
#     print('Нельзя вводить строки!')
# except ZeroDivisionError:
#     print('Нельзя делить на ноль!')


# try:
#     n = int(input('Введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print('Нельзя вводить строки или Нельзя делить на ноль! ')
# else:   # когда в блоке Try не возникло исключение
#     print('Все нормально. Вы ввели числа', n, 'и', m)
# finally:  # выполнится в любом случае
#     print('Конец программы')


# n = input('Введите первое число: ')   # '10'
# m = input('Введите второе число: ')   # qqq
# try:
#     n = int(n)   # 10
#     m = int(m)   #
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

# Циклы

# while условие:
#     блок_инструкций

# i = 0  # счетчик
# while i < 5:  # условие
#     print('i = ', i)
#     i += 1  # изменение счетчика

# итерация - один шаг цикла

# i = 10
# while i > 0:
#     print('i = ', i)
#     i -= 1
#
# i = 2
# while i <= 20:
#     if i % 2:   # i % 2 == 0 -четные числа     i % 2 != 0; i % 2 == 1; i % 2 - нечетные числа
#         print(i, end=' ')
#     i += 1

# i = 2
# while i <= 20:
#     print(i, end=' ')
#     i += 2

# n = int(input('Количество символов: '))
# print('*' * n)
# i = 0
# while i < n:
#     print('*', end='')
#     i += 1

# +-+-+-+

# n = int(input('Количество символов: '))
# i = 0
# while i < n:
#     if i % 2 == 0:
#         print('+', end='')
#     else:
#         print('-', end='')
#     i += 1

# n = int(input('Количество символов: '))
# while n > 0:
#     print('*', end='')
#     n -= 1

# a = int(input('Введите начало диапазона: '))
# b = int(input('Введите конец диапазона: '))
# res = 0
# while a <= b:
#     if a % 2:
#         print(a, end=' ')
#         res = res + a
#     a += 1
# print('\nСумма:', res)


# n = input('Введите целое число: ')
#
# while type(n) is not int:  # !=  это is not
#     try:
#         n = int(n)
#     except ValueError:
#         print('Число не целое!')
#         n = input('Введите целое число: ')
# if n % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print('\nЦикл завершен')


# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input('Введите положительное число: '))
#     if n < 0:
#         break

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print('Цикл окончен, i=', i)

# i = 1
# while i < 5:
#     print('Внешний цикл: i =', i)
#     j = 1
#     while j < 4:
#         print('\tВнутренний цикл: j =', j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, '*', j, '=', i * j, end='\t\t')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print('^', end='')
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1
#
# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1


# for element in collection:
#    print(element)

# for i in 'Hello!', 'World':
#     print(i)

#  range(start, stop, step = 1 по умолчанию)

# a = 10
# for i in range(0, 10, 1):  # i = 0, i < 10, i += 1
#     print(i, end=' ')
#
# print()
#
# i = 1
# while i < 10:
#     print(i, end=' ')
#     i *= 2


# a = int(input('Введите целое число: '))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=' ')


# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")
#
# print()
#
# for i in range(11, 100, 11):
#     print(i, end=" ")
#
#
# print()
#
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")


# for i in  range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('Цикл закончен')


# for i in range(3):
#     print('+++')
#     for j in range(2):
#         print('-----')


# w = 12
# h = 4
#
# for i in range(h):
#     for j in range(w):
#         print('*', end='')
#     print()


# w = int(input('Введите ширину прямоугольника: '))
# h = int(input('Введите высоту прямоугольника: '))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()


# letter = [i * 2 for i in 'Hello']
# print(letter)
#
# for i in 'Hello':
#     print(i * 2)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)
#
# for i in range(30):
#     if i % 2 == 0:
#         print(i)


#  Список (list)
# nums = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# print(nums)
# print(type(nums))
# print(nums[0])
# print(nums[1])
# print(nums[10])
# print(nums[-1])
# print('Кол-во чисел в списке:', len(nums))
# nums[1] = 256
# nums[3] += 100
# print(nums)

# s = []
# print(s)
# print(type(s))
#
# t = list()
# print(t)
# print(type(t))
#
# print(range(1, 18, 2))
# print(list(range(1, 18, 2)))

# a = [1, 3, 5, 7, 9]
# b = [11, 13, 15, 17]
# print(a + b)
# print(a * 3)


# a = [1, 3, 5, 7, 9]
#
# for i in a:
#     print(i)

# a = [0 for i in range(5)]
# print(a)

# a = [i for i in range(5)]
# print(a)

# n = 15
# a = [i ** 2 for i in range(2, n)]
# print(a)

# a = [0] * int(input('Введите кол-во элементов списка:'))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input('=>'))
# print(a)

# a = [input('->') for i in range(int(input('n= ')))]
# print((a))

# lst = [9, 6, 3, 5]
#
# for i in range(len(lst)):  # 0 1 2 3  - индекс
#     print(lst[i], end=' ')
#
# print()
#
# for v in lst:  #  9 6 3 5
#     print(v)


# n = list(range(21, 41))
# print(n)
# count = 0
# sum_ = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         count += 1
#     else:
#         sum_ += n[i]
# print('Количество четных элементов: ', count)
# print('Сумма: ', sum_)

# a = [int(input('->')) for i in range(int(input('n= ')))]
# print(a)
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=' ')
# print()
#
# for i in range(0, len(a), 2):
#         print(a[i], end=' ')

# a = [int(input('->')) for i in range(int(input('n= ')))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a [i -1]:
#         print(a[i], end=" ")

# a = [9, 7, 8, 4, 2]
# print(a)
# a[0], a[1] = a[1], a[0]
# print(a)

#  Cрез

# cписок[start: stop: step]

# a = [9, 7, 8, 4, 2, 1, 3]
# print(a)
# print(a[1:4])
# print(a[:])
# print(a[5:])
# print(a[1:4:2])
# print(a[::2])
# print(a[::-2])
# print(a[5:2:-1])
# print(a[-1:0:-1])
# print(a[10:20])

# lst = list(range(1, 8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[-1:])
# print(lst[3:4])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])


# a = [1, 2, 3, 4, 5, 6, 7]
# print(a)
# a[1:3] = [0, 0, 0, 0]
# print(a)
# a[1:2] = [20]
# print(a)
# # a[2] = [120]
# # print(a)
#
# a[100:111] = [100]
# print(a)
# print(a[9])
# print(len(a))


# Методы списков
# print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# s = [9, 7, 8, 4, 2, 1, 3]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([11, 12, 13])  # добавляет список элементов в конец списка
# print(s)
# s.insert(2, 100)  # добавляет элемент по заданному индексу
# print(s)
#
# s.insert(-1, 5)
# print(s)
# s.insert(20, 5)
# print(s)

# s = []
# n = int(input('кол-во элементов в списке: '))
# for num in range(n):
#     x = int(input('Введите число: '))
#     # s.append(x)
#     s.insert(0, x)  # [7, 8, 9]
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []  # [2, 1, 4, 3]
#
# for i in a:  # 5; 9; 2
#     for j in b:  # 4, 2, 1, 3, 7; 4, 2, 1, 3, 7;
#         if i in c:
#             continue
#         if i == j:  # 5!=4, 5!=2, 5!= 1, 5!= 3, 5!=7; 9!=4, ...
#             c.append(i)
#             break
# print(c)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7, 2]
# c = []
#
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c= []
#
# for i in range(len(a)):  # 0, 1, 2
#     c.append(a[i])
#     c.append(b[i])
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 4, 2]
# c = []
#
# for i in range(len(a)):  # 0, 1, 2, 3 ,4
#     c.append(a[i])
#     c.append(b[i])
# # for i in range(len(a), len(b)):
# #     c.append(b[i])
# print(c)

# a = [1, 2, 3, 4, 2]
# b = [11, 22, 33]
# c = []
# if len(b) > len(a):
#     for i in range(len(a)):  # 0, 1, 2, 3 ,4
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):  # 0, 1, 2, 3 ,4
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# a = [1, 2, 3, 4, 2]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     a,b = b,a
#
# for i in range(len(a)):  # 0, 1, 2, 3 ,4
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
#
# print(c)
#
# s = [9, 7, 8, 4, 2, 8, 1, 3]
# print(s)
# # s.remove(8)  # удаляет первое вхождение элемента по значению
# # print(s)
# # s.remove(18)  # ERROR
# # # print(s)
# #
# # item = 1
# # if item in s:
# #     s.remove(item)
# # print(s)
#
# # last = s.pop()  # удаляет последний элем из списка
# # print(last)
# # print(s)
# #
# # second = s.pop(1) # удаляет элемент по заданному индексу
# # print(second)
# # print(s)
# #
# # second = s.pop(10)  # ERROR
# # print(second)
# # print(s)
#
# try:
#     second = s.pop(1)
# except IndexError:
#     second = 'Такого индекса нет'
# print(second)
# print(s)

# s = [9, 7, 8, 4, 2, 8, 1, 3]
# # s.clear()  # удаляет элементы из списка
# print(s)
#
# # s[5:] = []
# # print(s)
#
# del s[0:3]
# print(s)

# s = [9, 7, 8, 4, 2, 8, 1, 3, 8]
# print(s)
#
# # num = s.count(9)  #  считает количество вхождений заданного элемента
# # print(num)
#
# ind = s.index(8, 3, 7)  #  ищет первое вхождение заданного элемента, возвращает индекс на котором
# # нашелся элемент, можно задать диапазон поиска
# print(ind)


# a = [1, 2, 3]
# b = a.copy()  # создает копию с отличным адресом  и меняются по разному
# print('a =', a, id(a))
# print('b =', b, id(b))
# b.append(20)
# print('a =', a, id(a))
# print('b =', b, id(b))
# a.append(100)
# print('a =', a)
# print('b =', b)

# m = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# m.reverse()  # разворачивает список
# print(m)

# m = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# m.sort()
# print(m)
# m = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# m.sort(reverse=True)
# print(m)

# s = ['Виталий', 'Сергей', 'Александр', 'Анна']
# s.sort(key=len, reverse=True)  # сортировка по длине
# print(s)

# m = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# m.sort()
# print(m)
#
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# lst = sorted(s)
# print(s)
# print('lst', lst)
#
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# lst = sorted(s, reverse=True)
# print(s)
# print('lst', lst)

# import random

# print(random.random())
# print(random.randint(5, 10))  # включает последнее значение, выбирает любое число из данных
# print(random.randrange(5, 10, 2))  # не включает посл значение
# print(round(random.uniform(10.5, 25.5), 2))  # не целое число

# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# print(random.choice(city_list))
# print(random.choice(s))
# print(random.choices(city_list, k=3))
# print(random.choices(s, k=3))
# random.shuffle(city_list)
# print(city_list)
# random.shuffle(s)
# print(s)

# import random
#
# mas = [random.randint(50, 100) for i in range(5)]
# print(mas)
# print(len(mas))
# print(max(mas))
# print(min(mas))
# print(sum(mas))  # считает сумму чисел в списке

# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# n = max(mas)
# print('Max:', max(mas))
# mas.remove(n)
# mas.insert(0, n)
# print(mas)

# import random
#
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# min_ = min(mas)
# print('Min', min_)
# ind = mas.index((min_))
# print('Index', ind)
# del mas[:ind]
# print(mas)

# import random

# m = [
#     [1, 2, 3, 4],  #  0 индекс
#     [5, 6, 7, 8],  # 1 индекс
#     [9, 10, 11, 12]  # 2 индекс
# ]
# print(m)
# print(len(m))
# print(m[1][2])
# print(m[2][1])
#
# print('Вариант 1')
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t')
#     print()
# print('Вариант 2')
# for row in m:
#     for x in row:
#         print(x, end='\t')
#     print()

# m = ['Hello', 'World', [44, [1, 2, 3], 55, ['Python']]]
# print(m)
# print(m[1][2])
# print(m[2][1][1])
# print(m[2][3][0][3])


# import math
#
# print(math.sqrt(4))
# print(math.ceil(3.2))
# print(math.floor(3.8))


# import math as m
#
# print(m.sqrt(4))
# print(m.ceil(3.2))
# print(m.floor(3.8))

# from math import *
#
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.8))


# from math import sqrt, ceil, floor
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.8))

# import math
# print(dir(math))

# from math import pi
#
# # print(pi)
# radius = int(input('Введите радиус окружности: '))
# print("Длина окружности:", round(2 * radius * pi, 2))

# import time
# import locale


# print(time.time())
# print(time.ctime(123))
# res = time.localtime()
# print(res)
# print(res.tm_year, "-", res.tm_mon, "-", res.tm_mday, sep='')
# print(time.strftime('Today is %B %d, %Y'))
# # print(time.strftime('%m/%d/%Y, %H:%M:%S', time.localtime(66666666)))
# locale.setlocale(locale.LC_ALL, 'ru')
# print(time.strftime('Сегодня: %B %d, %Y'))
#
# a = 1000000
# print(a)  #  1'000'000, 1,000,000

# start = time.time()
# print('Запуск программы')
# time.sleep(5)
# res = time.time() - start
# print('Программа выполнилась за', res, 'секунд')


# Функции

# def hello(name, age):  #  аргументы
#     print('Меня зовут:', name, 'Мой возраст:', age)
#
#
# hello('Irina', 28)  #  параметры
# hello('Ivan', 25)


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum('as', 'gfd')


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#     print()
#
#
# symbol(9, '+', '-')
# symbol(7, 'x', '0')


# def get_sum(a, b):
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)   #  return возвращает функцию в место вызова функции  = 7
# print(res)


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 5))
# print(maximum(5, 15))


# def res(a, b):
#     if a > b:
#         return a - b
#     elif a < b:
#         return a + b
#
#
# x = int(input('a ='))
# y = int(input('b ='))
# print(res(x, y))


# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, 'в кубе =', cube(i))


# def change(lst):
#     end = lst.pop()   #  удален последний элемент
#     start = lst.pop(0)  #  удален первый элемент
#     lst.append(start)
#     lst.insert(0, end)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['c', 'л', 'o', 'н']))

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['c', 'л', 'o', 'н']))


# def one_big(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# if one_big(a, b):
#     print('Первое число больше второго')
# else:
#     print("Втрое число больше первого")
# print(one_big(10, 5))
# print(one_big(5, 10))

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         if 'a' <= ch <= 'z':
#             has_lower = True
#         if '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) > 8 and has_upper and has_lower:
#         return True
#     return False
#
#
# p = input('Введите пароль: ')
# if check_password(p):
#     print('Надежный пароль')
# else:
#     print('Ненадежный пароль')


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2, c=5))
# print(get_sum('С', 'л', d='н', c='о'))


# def set_param(count=20, symbol='-'):
#     print(symbol * count)
#
#
# set_param(10, '+')
# set_param(5, '*')
# set_param(15, '#')
# set_param(7)
# set_param()

#
# def display_info(name, age):
#     print('Name:', name, '\nAge:', age)
#
#
# display_info('Irina', 23)ay
# def display_info(name, age):
#     print('Hello,', name)
#
#
# display_info('Irina', 23)
# display_info(23, 'Irina')
# display_info(age=23, name='Irina')
# display_info('Igor', age=23, name='Irina')


# lt1 = 'Hello'
# lt2 = 'Hello'
# print(lt1, id(lt1))
# print(lt2, id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)
# print(lst1 is lst2)

# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))
# lst1.pop(1)
# print(lst1, id(lst1))

# lt1 = 'Hello'
# print(lt1, id(lt1))
# lt1 = lt1[5:10]
# print(lt1, id(lt1))
# lt1 = lt1 + '!'
# print(lt1, id(lt1))

# a = 5
# print(a, id(a))
# a =7
# print(a, id(a))


# Кортеж (turple)


# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
# lst[1] = 100
# print(lst)
# tpl[1] = 100  #  кортэж не изменяем
# print(tpl)

# a = ()
# print(a, type(a))
# b = tuple()
# print(b, type(b))

# a = 1, 2, 3  #  без скобок также кортеж
# print(a, type(a))
#
# b = tuple('Hello')
# print(b, type(b))

# b = tuple('Hello')
# print(b)
#
# print(b[1])
# print(b[1:3])

# s1 = tuple(input('->') for i in range(5))
# print(s1)

# from random import randint
# s1 = tuple(randint(50, 100) for i in range(5))
# print(s1)


# t1 = tuple('hello')
# t2 = tuple('world')
# # # print(t1)
# # # print(t2)
# t3 = t1 + t2
# # print(t3)
# print(t3.)
# # print(t3 * 2)

# print((t3.count('a')))
# print(t3.index('l', 4, -2))
# print(dir(list))
# print(dir(tuple))

# v = 'l'
# if v in t3:
#     print(t3.index(v))
# else:
#     print('Такого индекса нет')


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) == 1:
#             return tpl[tpl.index(el):]  #  [2:]
#         else:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print((slicer((1, 2, 8, 5, 1, 2, 9), 8)))

# t = (10, 'Python', True, [1, 2, 3], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# print(t, id(t))
# print(len(t))
# t[4].append('hi')
# print(t, id(t))

#  распаковка кортежа

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# # x, y, z = 1, 2, 3
# print(x, y, z)

#  только кортеж возвращает несколько значений
# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
# # user = get_user()
# # print(user)
# # first_name, year, married = user
#
# first_name, year, married = get_user()
# print(first_name, year, married)
# print(year)

# lst = [1, 2, 3, 4, 5, 6]
# print(lst, type(lst))
# tpl = tuple(lst)
# print(tpl, type(tpl))
# lst2 = list(tpl)
# print(lst2, type(lst2))

# countries = (
#     ('Германия', 80.2, (('Берлин', 3.326), ('Гамбург', 1.718))),
#     ('Франция', 66, (('париж', 2.2), ('Марсель', 1.6)))
# )
# print(countries, end='\n\n')
#
# for county in countries:
#     county_name, county_population, cities = county
#     print('\nСтрана: ', county_name, ', население = ', county_population, cities, sep='')
#     for city in cities:
#         city_name, city_population = city
#         print('\tГород ', city_name, ', население ', city_population, sep='')

# tpl = tuple(input('Введите строку: '))
# print(tpl)
#
# lst = []
#
# for i in range(len(tpl)):
#     if tpl[i] not in lst:
#         lst.append(tpl[i])
#
# for i in range(len(lst)):
#     print('Количество: ', lst[i], '=', tpl.count(lst[i]))
#
# print(lst)


# Множество  (set)

# s = {'red', 'yellow', 'green', 'yellow', 'green'}
# print(s, type(s))
# print(len(s))

# a = set('helo')
# print(a, type(a))

# s = {x * x for x in range(10)}
# print(s)

# lst = [1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6]
# lst = ['red', 'yellow', 'green', 'yellow', 'green']
# print(lst)
# num = set(lst)
# print(num)
# lst2 = list(num)
# print(lst2)
#
# t = {'yellow', 'red', 'green'}
# print('red' in t)
# print('blue' in t)
# for i in t:
#     print(i)

# lst = ['ab_1', 'ac_1', 'bc_1', 'bc_2']
# print([i for i in lst if 'a' in i])
# print(['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst])
# print(tuple('A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c'))

# print(dir(set))

# a = {'red', 'yellow', 'green'}
# print(a)
# a.add('blue')
# print(a)
# # a.remove('yellow')
# # a.remove('black')  # KeyError
# color = 'black'
# # if color in a:
# #     a.remove(color)  #  удаление элемента, если нет выдаст ошибку
# # a.discard(color)  #  удаление элемента, если нет не выдаст ошибку
# # a.pop()  #  удаление первого элемента (то есть любой)
# a.clear()  # очистка полностью
# print(a)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)  # объединение множеств
# # c = a | b
# # print(c)
# a |= b  # создается объединение множеств и перезапись переменной a
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a & b  #  пересечение множеств
# print(c)
# a &= b
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a - b  #  0  вычитает повторяющиеся
# print(c)
# a -= b
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a ^ b
# print(c)
# a ^= b
# print(a)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}  # b подмножество а
# c = a >= b
# print(c)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = {6, 2}
# e = {8, 2}
# # d = a ^ b ^ c ^ e  #
# d = a.symmetric_difference(b).symmetric_difference(c).symmetric_difference(e)
# print(d)

# a = {1, 2}
# b = {3}
# c = {4, 5}
# d = {3, 2, 6}
# e = {6}
# f = {7, 8}
# g = {9, 8}
# h = a | b | c | d | e | f | g
# print(h)
# print('Unic elems count: ', (len(h)))
# print('Min elem: ', min(h))
# print('Max elem: ', max(h))


# a = 'Hello'
# b = 'How are you'
# c = set(a) & set(b)
# # print(c)
# for i in c:
#     print(i, end=' ')

# s = frozenset([1, 2, 3, 4, 5, 6])
# print(s)
# s1 = frozenset('hello')
# print(s1)

#  Cловарь (dict)

# lst = ['one', 'two']
# d = {'first': 'one', 'second': 'two'}  #  первое значение ключ второе его значение
# print(lst[1])
# print(d['second'])

# d = {0: 'text', 'one': 45, (1, 2): 'Кортеж', True: [5, 9, 8, 6], False: 'один', 1: 'spisok'}  # при повторных ключах
# # берется первый из них и перезаписывает второе значение
# print(d)


# Создание словаря
# d = {1: 'one', 'second': 'two'}  #  ключ любой неизменные данные
# print(d)
# print(type(d))
#
# d1 = dict(first='one', second='two')  #  ключ только строка
# print(d1)
# print(type(d1))

# lst = [
#     ['one', 1],
#     ['two', 2],
#     ['three', 3]
# ]
#
# print(lst)
# d = dict(lst)
# print(d)

# d = {i: i ** 2 for i in range(1, 7)}
# print(d)
#
# for i in d:
#     print('key =', i, 'value = ', d[i])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res *= d[key]
# print(res)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(d)
# del d['x2']
# print(d)

# d = dict()
# d[1] = input('-> ')
# d[2] = input('-> ')
# d[3] = input('-> ')
# d[4] = input('-> ')
# print(d)

# d = {i: input('-> ') for i in range(1, 5)}
# print(d)
# dislike = int(input('Что исключить: '))
# del d[dislike]
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400]
# }
#
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], 'шт. по ', goods[i][2], 'руб', sep='')
#
# while True:
#     n = input('# : ')
#     if n == '0':
#         break
#     else:
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input('Количество: '))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print('Значение некорректно, введите число')
#         else:
#             print('Такого ключа нет')
# #
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ', goods[i][1], 'шт. по ', goods[i][2], 'руб', sep='')

# print(dir(dict))

# d = {1: 'one', 2: 'two', 3: 'three'}
# print(d.keys())
# print(d.values())
# print(d.items())
# for i in d:
# for i, j in d.items():
#     print(i, ':', j)

# d = {1: 'one', 2: 'two', 3: 'three'}
# d2 = d.copy()
# print('D =', d)
# print('D2 =', d2)
#
# d2[2] = 'four'
# print('D =', d)
# print('D2 =', d2)

# d = {1: 'one', 2: 'two', 3: 'three'}
# print(d)
# # d.clear()
# # item = d.pop(2)
# # item = d.pop(4, 'Такого ключа не существует')
# # item = d.pop(2, 'Элемент')
# item = d.popitem()
# print(d)
# print(item)

# d = {1: 'one', 2: 'two', 3: 'three'}
# # # value = d[2]
# # value = d.get(2, 'Такого ключа не существует')
# # # value = d.get(6, 0)
# # print(value)
# # item = d.setdefault(4)
# # item = d.setdefault(4, 'four')  # добавляет значение
# item = d.setdefault(2, 'four')  #  не добавляет значение если ключ есть
# print(d)
# print(item)

# d = {1: 'one', 2: 'two', 3: 'three'}
# # a = {10: 'A', 20: 'B', 2: 'C'}
# a = [(10, 'A'), (20, 'B'), (2, 'C')]
# # c = d + a  #  ошибка
# # c = d | a  #  складывает словари
# # print(c)
# c = d.update(a)
# print(d)

# d = {'name': 'Kelly', 'age': '25', 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# # new_d['name'] = d.pop('name')
# # new_d['salary'] = d.pop('salary')
# new_d['name'], new_d['salary'] = d.pop('name'), d.pop('salary')
# print(d)
# print(new_d)

# d = {'name': 'Kelly', 'age': '25', 'salary': 8000, 'city': 'New York'}
# d['location'] = d.pop('city')
# print(d)

# d = {
#     'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
# }
# for x, y in d.items():
#     print(x)
#     for i, j in d[x].items():
#         print('\t', i, ':', j)

#  генераторы словарей

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# # new_d = {key: value for key, value in d.items()}
# new_d = {value: key for key, value in d.items()}
# print(d)
# print(new_d)

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# new_d = {key: value for key, value in d.items() if value <= 2}
# print(new_d)

# d = {i: i * 5 for i in [10, 20, 30, 40, 50]}
# print(d)
#
# s = 'Hello'
# d1 = {key: key * 3 for key in s}
# print(d1)

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
#
# print(list(d.values()))
# print(list(d.keys()))
# print(list(d.items()))

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = dict()  #  {'one': [1,2,3], 'two': [], 'three': [], 'four': []}
# s = None
#
# for i in a:
#     if type(i) is str:
#         d[i] = []
#         s = i  #  'one'
#     else:
#         d[s].append(i)
# print(d)

#  zip

# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# d = list(zip([1, 2, 3], ['one', 'two', 'three'], [33, 44, 55]))
# print(d)
# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# a = {1, 2, 3}
# b = {'one', 'two', 'three'}
# a = [1, 2, 3, 4]
# b = ['one', 'two', 'three']
# d = {k: v for k, v in zip(a, b)}
# print(d)

# one = {'name': 'Igor', 'surname': 'Pavlov', 'job': 'Consol'}
# two = {'name': 'Irina', 'surname': 'Vetrova', 'job': 'Manager'}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# s = [(1, 'a'), (2, 'b'), (3, 'c')]
# a, b = zip(*s)  # * распаковка кортежей
# print(a)
# print(b)

# letters = ['b', 'd', 'a', 'c']
# numbers = [4, 1, 3, 2]
# d = dict(zip(letters, numbers))
# print(d)
# #
# data1 = list(zip(letters, numbers))
# print(data1)
# data1.sort()
# print(data1)
# d2 = dict(data1)
# print(d2)
#
# data2 = list(zip(numbers, letters))
# print(data2)
# data2.sort()
# print(data2)
# d3 = {v: k for k, v in data2}
# print(d3)

# letters = ['b', 'd', 'a', 'c']
# numbers = [4, 1, 3, 2]
#
# data = sorted(zip(letters, numbers))
# print(dict(data))

# one = {'один': 1, 'два': 2}
# two = {'три': 3, 'четыре': 4}
# print({**one, **two})  #  объединяет словари  ** распаковка словаря
# print(one | two)
#
# for k, v in {**one, **two}.items():
#     print(k, '->', v)

# colors = ['red', 'green', 'blue']
# ind = 1
# # for color in colors:
# #     print(str(ind) + '-й цвет: ' + color)
# #     ind += 1
# #
# for index, color in enumerate(colors, 1):
#     print(str(index) + '-й цвет: ' + color)

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
#
# for i, (k, v) in enumerate(d.items(), 1):
#     print(i, ') ', k, ': ', v, sep='')

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):  #  различное количество параметров
#     return args
#
#
# print(func(5))
# print(func(1, 2, 3, 'abc'))
# print(func())

# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(7, 8, 9))

# def to_dict(*args):
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('grey', (2, 17), 3.11, -4))

# def average(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#     res = []
#     for num in args:
#         if num < sr:
#             res.append(num)
#     return res
#
#
# print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(average(3, 6, 1, 9, 5))

# def func(a, b, *args):
#     return a, args
#
#
# print(func(5, 2))
# print(func(1, 2, 3, 4, 5))

# def scores(student, *score):
#     print('Student name: ', student)
#     for i in score:
#         print(i)
#
#
# scores('Igor', 100, 95, 88, 92, 99)
# scores('IVan', 77, 32, 88)

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=1, c=3))
# print(func())
# print(func(name='Irina'))

# def info(**data):
#     for k, v in data.items():
#         print(k, ':', v)
#     print()
#
#
# info(name='Irina', surname='Vetrova', age=22)
# info(name='Igor', phone='99825', email='igor@mail.ru', age=22)


# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='bob', age=31, weighy=61, eyes_color='grey')
# print(my_dict)

# def func(a, *args, b=100, **kwargs):
#     return a, b, args, kwargs
#
#
# print(func(1, 2, 3, 4, 5, 6, c=55,  d=66,  b=20, e=77))


# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
#
# func1(1, 2, 3, 4, 5)
# func2(one=123, two=456)


#  Области видимости (scope)

# name = 'Tom'  #  глобальная область видимости
#
#
# def hi():
#     global name, surname
#     name = 'Sam'  #  локальная область видимости
#     surname = 'Jonson'
#     print('Hello', name, surname)
#
#
# def bye():
#     print('Good bye', name)
#
#
# # print(name)
# hi()
# bye()
# print(name)
# print(surname)


# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()
# print(i)


# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)


# max = 5
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
# print(max(lst))


# def add_two(a):
#     x = 2  #  вторая строка, которая будет отрабатываться по очереди
#
#     def add_some():
#         x = 3
#         print('x =', x)  #  четвертая строка, отрабатываемая по очереди
#         return a + x  #  пятая по порядку
#     print('х в наружной функции =', x)
#     return add_some()  #  третья строка, которая отрабатывается  также и шестая очередь
#
#
# print(add_two(3))  #  первая по очереди строка, которая отрабатывается то есть вызов функции,
# # затем она седьмая выводит печать

#  вложенные функции

# def outer(who):
#     def inner():
#         print('Hello,', who)
#
#     inner()
#
# outer('World')


# def outer():
#     a = 6
#
#     def inner(b):
#         a = 4
#         print('Сумма: ', a + b)
#     print('a =', a)
#     inner(5)
#
#
# outer()


# x = 25
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print('a =', a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)


# def fn1():
#     x = 25
#
#     def fn2():
#         # x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#         fn3()
#         print('fn2.x=', x)
#
#     fn2()
#     print('fn1.x=', x)  #
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         print(a, b)
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))


# def rect_peral(a, b, c):
#     def inner(i, j):
#         return i * j
#
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(rect_peral(2, 4, 6))
# print(rect_peral(5, 8, 2))
# print(rect_peral(1, 6, 8))


#  Замыкания

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# a = outer(5)
# print(a(10))
#
# b = outer(6)
# print(b(10))
#
# print(outer(5)(10))

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a
#         nonlocal b
#         c.append(4)
#         a = a + 1
#         b = b + '!'
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res1()


# Анонимные функции (lambda)

# def func(x, y):
#     res = x + y
#     return res
#
#
# print(func(1, 2))
#
# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
#
# func1 = lambda x, y: x + y
#
# print(func1(1, 2))
# print(func1(5, 2))


# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())

# print((lambda *args: sum(args))(1, 2, 3, 4, 5, 6, 7))
# print((lambda *args: sum(args))(6, 7))

# print((lambda **kwargs: kwargs)(a=1, b=2, c=3))
# print((lambda **kwargs: sum(kwargs.values()))(a=1, b=2, c=3))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
# for t in c:
#     print(t('abc__'))

#
# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(42)
# print(f(3))
#
#
# def outer(n):
#     return lambda x: x + n
#
#
# f = outer(42)
# print(f(3))
#
#
# outer = lambda n: lambda x: x + n
# f = outer(42)
# print(f(3))
#
# f = (lambda n: lambda x: x + n)(42)
# print(f(3))
#
#
# res = (lambda n: lambda x: ' x > n' if x > n else 'x < n')(42)(3)
# print(res)

# res = (lambda x: lambda y: lambda z: x + y + z)(2)(4)(6)
# print(res)


# def func(i):
#     return i[1]
#
#
# d = {'b': 10, 'a': 15, 'c': 4}
# lst = list(d.items())
# print(lst)
# lst.sort(key=func)
# print(lst)
# d2 = dict(lst)
# print(d2)

# d = {'b': 10, 'a': 15, 'c': 4}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# d2 = dict(lst)
# print(d2)


# players = [{'name': 'Антон', 'lastname': 'Бирюков', 'raiting': 9},
#            {'name': 'Алексей', 'lastname': 'Бодня', 'raiting': 10},
#            {'name': 'Федор', 'lastname': 'Сидоров', 'raiting': 4},
#            {'name': 'Михаил', 'lastname': 'Семенов', 'raiting': 6},
# ]
#
# res1 = sorted(players, key=lambda item: item['lastname'])
# print(res1)
#
# res2 = sorted(players, key=lambda item: item['raiting'], reverse=True)
# print(res2)
#
# res3 = sorted(players, key=lambda item: item['raiting'])
# print(res3)


# lst = [
#     lambda x, y: x + y,
#     lambda x, y: x - y,
#     lambda x, y: x * y,
#     lambda x, y: x / y,
# ]
# print(lst[0](12, 2))


# d = {
#     1: lambda: print('Январь'),
#     2: lambda: print('Февраль'),
#     3: lambda: print('Март'),
#     4: lambda: print('Апрель'),
#     5: lambda: print('Май'),
#     6: lambda: print('Июнь'),
#     7: lambda: print('Июль'),
#     8: lambda: print('Август'),
#     9: lambda: print('Сентябрь'),
#     10: lambda: print('Октябрь'),
#     11: lambda: print('Ноябрь'),
#     12: lambda: print('Декабрь'),
# }
#
# d[3]()


#  map()  цикл

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
# print(list(map(mult, lst)))
#
# print(list(map(lambda t: t * 2, lst)))
#
# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))
#
# print(set(map(lambda t: t * 2, [2, 8, 12, -5, -10])))
#
# lst1 = [2, 8, 12, -5, -10]
# lst2 = [8, -10, 12, 2, -5]
#
# print(dict(map(lambda x, y: (x, y), [2, 8, 12, -5, -10], [8, -10, 12, 2, -5])))
# print(dict(map(lambda x, y: (x, y), lst1, lst2)))
# print(list(map(lambda x, y: (x, y), lst1, lst2)))


# t = (2.88, -1.78, 100.55)
#
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))

# areas = [3.564789, 5.789456, 4.012456, 56.451266, 9.4567891, 32.45678912]
# print(list(map(round, areas, range(1, 7))))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda x, y: x + y, l1, l2)))


#  filter()  цикл

# t = ('abcd', 'qwe', 'zxcvb', 'def', 'hjk')

# print(tuple(filter(lambda s: len(s) == 3, t)))


# lst = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# print(list(filter(lambda s: s > 75, lst)))


# import random
#
# lst = [random.randint(0, 40) for i in range(10)]
# print(lst)
# print(list(filter(lambda s: 10 <= s <= 20, lst)))
# print(list(filter(lambda s: s in range(10, 21), lst)))

# lst = [45, 55, 60, 37, 100, 105, 220]
# print(list(filter(lambda x: x % 15 == 0, lst)))
# print(list(filter(lambda x: not x % 15, lst)))

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10)))))
# print(list(filter(lambda x: x % 2, range(10))))
#
# print([x ** 2 for x in range(10) if x % 2])


#   Декораторы

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# text = hello
# print(text())


# def my_decorator(func):
#     def inner():
#         print('До кода')
#         func()
#         print('После кода')
#
#     return inner
#
#
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def inner():
#         print('-' * 30)
#         func()
#         print('*' * 30)
#
#     return inner
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('Hello, I am func "func_test"')
#
#
# @my_decorator
# def test():
#     print('Hello, I am func "test"')


# func_test()
# test()

# def circle(fn):
#     def wranp():
#         return '(' + fn() + ')'
#
#     return wranp
#
#
# def angle(fn):
#     def wranp():
#         return '<' + fn() + '>'
#
#     return wranp
#
#
# @angle
# @circle
# def expression():
#     return '5 + 2'


# print(expression())


# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print('Вызов функции: ', count)
#
#     return wrap
#
# @cnt
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()

# def outter(fn):
#     def inner(arg1, arg2):
#         print('Данные :', arg1, arg2)
#         fn(arg1, arg2)
#
#     return inner
#
#
# @outter
# def print_full_name(first, last):
#     print('Меня зовут', first, last)
#
#
# print_full_name('Ирина', 'Ветрова')

#
# def outer(fn):
#     def inner(*args, **kwargs):
#         print('args', args)
#         print('kwargs', kwargs)
#         fn(*args, **kwargs)
#
#     return inner
#
#
# @outer
# def print_data(a, b, c, study='Python'):
#     print(a, b, c, 'изучают', study, end='\n\n')
#
#
# print_data('Борис', 'Елизавета', 'Светлана', study='Javascript')
# print_data('Вова', 'Катя', 'Витя')


# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '=', end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor('Сумма:', '+')
# def summa(a, b):
#     print((a + b))
#
#
# @decor('Разность:', '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def multiply(arg):
#     def inner(fn):
#         def inner2(*args, **kwargs):
#             return fn(*args, **kwargs) * arg
#
#         return inner2
#     return inner
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))

#
# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) is not args[i]:
#                     raise TypeError('Неверный тип данных')
#             for k in kwargs:
#                 if type(f_kwargs[k]) is not kwargs[k]:
#                     raise TypeError('Неверный тип данных')
#                     # return 'Неверный тип данных'
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, 'Hello'))
# print(typed_fn2('Hello', 'World', '!'))
# # print(typed_fn2(1, 2, 3))
# print(typed_fn3('Hello', 'World', z=5))
# print(typed_fn3('Hello', 'World', z='!'))


#  Строки

# print(bin(18))  # 0b10010  двоичная система счисления
# print(oct(18))  # 0o22  восьмеричная система счисления
# print(hex(18))  # 0x12  шестнадцатеричная система счисления
#
# print(0b10010)
# print(0o22)
# print(0x12)
# print(0x12 + 0b10010 + 4)

# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# print(e * 3)
# print('y' in e)
# print('a' in e)
# print(e[1])
# print(e[1:3])
# print(e[::-1])


# def change_char_to_str(s, old, new):
#     s2 = ''
#     i = 0
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#
#         i += 1
#
#     return s2
#
#
# str1 = 'Я изучаю Nyton. Мне нравится Nyton. Nyton очень интересный язык программирования'
# str2 = change_char_to_str(str1, 'N', 'P')
# print(str1)
# print(str2)

# print(u'Привет')
# print('Привет')


# print('c:\\file.txt')
# print(r'c:\file.txt\\'[:-1])
# print(r'c:\file.txt' + '\\')
# print('c:\\file.txt\\')

# print(b'1ab2c3')


# name = 'Дмтирий'
# age = 25
# print(f'Меня зовут {name}. Мне {age} лет')

# x = 10
# y = 5
# print(f'{x=}, {y=}')
# print('x=', x, 'y=', y, sep=' ')
# print(f'{round(10/7, 2)}')
# print(f'{10/7:.2f}')
# num = 74
# print(f'{{{num}}}')


# dir_name = 'folder'
# file_name = 'file.txt'
# print(fr'home\{dir_name}\{file_name}')
# print('home\\' + dir_name + '\\' + file_name)


# s = '''Многострочный
# текст
# '''
# print(s)
# st = ('многострочный '
#       'текст')
# print(st)

# def square(n):
#     '''Принимает число n, возвращает квадрат числа n'''
#     res = n ** 2
#     return res
#
#
# print(square(5))
# print(square.__doc__)
# print(sum.__doc__)
# print(min.__doc__)

# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания.
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)


# print(ord('a'))
# print(ord('а'))
# print(ord('б'))

# while True:
#     n = input('-> ')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break


# st = "Test string for me "
# arr = [ord(x) for x in st]
# print("ASCII коды", arr)
# arr = [round(sum(arr) / len(arr))] + arr
# print("Среднее арфиметическое: ", arr)
# arr += [ord(x) for x in input('->')[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))

# a = 97
# b = 122
#
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")

#
# print('apple' == 'Apple')
# print(ord('a'))
# print(ord('A'))

# from random import randint
#
# SHORT = 8
# LONG = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
#
# def random_password():
#     rand_len = randint(SHORT, LONG)
#     result = ""
#     for i in range(rand_len):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
#
# print("Случайный пароль: ", random_password())


# print(dir(str))

# s = "hello, WORLD! I am leaning Python."
# # print(s.capitalize())  #  Первый символ в строке в верхнем регистре, остальные в нижнем
# # print(s.lower())  #  все символы в нижнем регистре
# # print(s.upper())  #  все символы в верхнем регистре
# # print(s.swapcase())  #  инвертирование регистра символов
# # print(s.title())  #  первая буква каждого слова в верхнем регистре
#
# # print(s.count("h", 1, -4))
# # print(s.lower().count("i"))
#
# print(s.find("Python"))  #  возвращает первый индекс подстроки
# print(s.find("h", 1, - 4))  #  если вхождение не найдено то возвращается "- 1"
#
#
# print(s.index("Python"))
# print(s.index("h", 1, - 4))  #  если вхождение не найдено то возвращается ValueError

# st = "один два"
# one = st[:st.find(" ")]
# two = st[st.find(" ") + 1:]
# print(two + " " + one)


# s = "hello, WORLD! I am leaning Python."
# print(s.rfind("h", 1, - 4))  #  возвращает последний индекс подстроки, если вхождения не найдено озвращается "-1"
# print(s.rindex("h", 1, - 4))  #  возвращает последний индекс подстроки, если вхождения не найдено озвращается "ValueError"


# st = "I am learning Python. hello, WORLD"
# print(st[:st.find("h")] + st[st.rfind("h") + 1:])
#
# s = "hello, WORLD! I am leaning Python."
# print(s.startswith("he"))  #  возвращает True если строка начинается с заданной подстроки
# print(s.startswith("I am", 14))
# print(s.find("I am"))
#
# print(s.endswith("Python"))  #  возвращается True если строка заканчивается заданнйо подстрокой
#
# print("abc123".isalnum())  #  определяет состоит ли строка из строк и цифр
# print("abc;123".isalnum())
# print("".isalnum())
#
# print("ABCsvb".isalpha())  #  определяет состоит ли строка из букв
# print("234235".isdigit())  #  определяет состоит ли строка из цифр


# print("abc".islower())  #  определяет состоит ли строка из букв в нижнем регистре, допскает наличие других символов
# print("Abc".islower())
# print("%^&abc123412".islower())

# print("Abc".isupper())  #определяет состоит ли строка из букв в верхнем регистре, допскает наличие других символов
# print("ABC".isupper())

# print("py".center(10))  #  выравниваем строку по центру
# print("py".center(10, "-"))
# print("py".center(1))

# print("       py".lstrip())  #  удалит пробелы с левой стороны
# print("py          ".rstrip())  #  удалит пробелы с правой стороны
# print("       py        ".strip())  #  удалит пробелы слева и справа


# print("https://.python.org".lstrip("htps:/"))
# print("https://.python.org".rstrip("org."))
# print("https://.python.org".strip("htps:/."))
#
# print("https://.python.org".lstrip("htps:/").rstrip("org."))

# str1 = 'Я изучаю Nyton. Мне нравится Nyton. Nyton очень интересный язык программирования'
# print(str1.replace("N", "P"))
# print(str1.replace("Nyton", "Pyton", 2))  #  поиск и замена

# st = "-"
# seq = ('a', 'b', 'c')
# print(st.join(seq))  #  объединяет итерируемую последовательность в строку
#
# print("..".join(['1', '99']))
# print(":".join('abc'))
# print(":".join('a'))

# print('Строка разделенная пробелами'.split())  #  строку преобразует в список по символу разделителю
# print('www.python.org'.split("."))
# print('www.python.org.ru'.split(".", 2))

# print('www.python.org'.rsplit("."))
# print('www.python.org.ru'.rsplit(".", 2))

# # st = "Никонов Валерий Анатольевич"
# st = input("ВВедите ФИО: ").split()
# # st = st.split()
# print(st)
# print(f"{st[0]} {st[1][0]}. {st[2][0]}.")

# num = input("Введите числа через пробел: ").split()
# print(num)
# num = list(map(int, num))
# print(num)
# print(sum(num))


# Регулярные выражения
import re
from itertools import count
from os import write

# s = 'Я ищу совпадения в 2025 году. И я их найду в 2 счёта.'
# # reg = 'совпадения'
# # print(re.findall(reg, s))  #  возвращает список содержащий все совпадения
# # print(re.search(reg, s))  #  место расположения первого объекта
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).group())
# # reg = 'Я ищу'
# # print(re.match(reg, s))  #  поиск совпадения только с начала строки
# # reg = r'\.'
# # reg = r'а'
# reg = r'[ан]'
# # print(re.split(reg, s))  #  список, в котором строка разбита по заданному шаблону
# reg = r'\.'
# print(re.sub(reg, '!', s))  #  поиск и замена

# print(dir(re))

# s = 'Я ищу совпадения в 2025 году. И я их найду в 2 счёта.6789 [Hel-lo] Wor_ld'
# # reg = r'[0-9]'
# # reg = r'[6-9]'
# reg = r'[12][0-9][0-9][0-9]'
# reg = r'[А-Яа-яЁё]'
# reg = r'[А-яЁё]'
# reg = r'[A-z]'
# reg = r'[A-Za-z\[\]-]'
# reg = r'[^0-9]'
# print(re.findall(reg, s))
#
# st = 'Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты в диапозоне от 00 до 59. 2021-06-15T01:09'
# reg = '[0-2][0-9]:[0-5][0-9]'
# print(re.findall(reg, st))

# s = 'Я ищу совпадения в 2025 году. И я их найду в 2 счёта.6789 [Hel-lo] Wor_ld'
# # reg = r'\d'   #  все цифры
# # reg = r'\D'  #  все кроме цифр
# # reg = r'\s'  #  все пробелы
# # reg = r'\S'  #  все кроме пробелов
# # reg = r'\w'  #  все цифры и буквы всех алфавитов
# # reg = r'\W'
# # reg = r'\AЯ ищу'
# reg = r'Wor_ld\Z'
# print(re.findall(reg, s))

#  Кол-во повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ?  - от 0 до 1 повторения

# s = 'Я ищу совпадения в 2025 году. И я их найду в 2 счёта.6789 [Hel-lo] Wor_ld 2000000000'
# # reg = r'\w+'
# # reg = r'\d+'
# reg = r'20*'
# print(re.findall(reg, s))

# d = 'Цифры: 7, +17, -24, 0013, 0.3'
# reg = r'[+-]?[\d.]+'
# print(re.findall(reg, d))

# d = '05-03-1987  #  Дата рождения'
#
# print('Дата рождения:', re.sub(r'\s\s#.+','', d))
# print('Дата рождения:', re.sub(r'-','.', d))
# print('Дата рождения:', re.sub(r'\s\s#.+','', re.sub(r'-','.', d)))

# st = 'author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831'
# # reg = r'\w+\s*=\s*\w*\s*\w*\.?\w?\.?'
# # reg = r'\w+\s*=\s*[\w\s\.]*'
# reg = r'\w+\s*=\s*[^;]+'  #  возвращает все символы кроме ;
# print(re.findall(reg, st))
#
# reg1 = r'; '
# print(re.split(reg1, st))

# st = '12 сентября 2025 года'
# reg = r'\d{4}'
# reg = r'\d{2,4}'
# reg = r'\d{,4}'
# print(re.findall(reg, st))

# s = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# reg = r'\+?7\d{10}'
# print(re.findall(reg, s))

# s = 'Я ищу совпадения в 2025 году. И я их найду в 2 счёта.6789 [Hel-lo] Wor_ld 2000000000'
# # reg = r'^\w+\s\w+'
# reg = r'\w+\s\w+$'
# print(re.findall(reg,s))

# def validate_login(login):
#     return re.findall(r'^[A-za-z0-9_-]{3,16}$', login)
#
#
# print(validate_login('Python_master'))
# print(validate_login('Pyt00'))

# text = '<body>Примет жадного совпадения соответствия регулярных выражений</body>'
# print(re.findall('<.*?>', text))

# st = 'Петр, Ольга и Виталий отлично учатся!'
# reg = r'Петр|Ольга|Виталий|Наталья'
# print(re.findall(reg,st))

# st = 'int = 4, float = 4/0f, double = 8.0, int'
# # reg = r'\w+\s*=\s*\d[/\w+]*'
# # reg = r'int\s*=\d[.\w+]*|float\s*=\s*\d[.\w+]*'
# reg = r'((int|float)\s*=\s*(\d[.\w+]*))'  #  выводят информацию, которая была в скобках
# print(re.findall(reg, st))

# d = 'Word2016, PS6, AI5'
# reg = r'([A-Za-z]+)\d+'
# reg = r'[A-Za-z]+(\d+)'
# print(re.findall(reg, d))
# print(re.search(reg, d))

# st = '5 + 7*2 - 4'
# # reg = r'\s*([+*-])\s*'
# reg = r'\s*[+*-]\s*'
# print(re.split(reg, st))


# s = 'Я ищу совпадения в 2025 году. И я их найду в 2 счёта.'
# # reg = r'[0-9]+\s\D+'
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# print(re.search(reg, s).group(0))
# print(re.search(reg, s).group(1))
# print(re.search(reg, s).group(2))
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])

# s = 'Самолет прилетает 10/23/2025. Будем рады вас видеть после 10/24/2025'
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))

# s = 'yandex.com and yandex.ru'
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s))

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# text = 'hello world'
# print(re.findall(r'\w\+', text))
# print(re.findall(r'\w\+', text, re.DEBUG))

# text = 'helLo worLd'
# reg = r'l'
# print(re.findall(reg, text))
# print(re.findall(reg, text, re.IGNORECASE))

# text = """
# one
# two
# """

# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))

# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, re.MULTILINE))

# print(re.findall("""
# [a-z.-]+         #  part 1
# @               #  @
# [a-z.]+          #  part 2
# """, 'test@mail.ru', re.VERBOSE))

# text = '''Python,
# python
# PYTHON'''
# reg = '(?im)^python'
# print(re.findall(reg, text))

#  Рекурсия

# def elevator(n):  #  5
#     if n == 0:    #  базовый случай
#         print('Вы в подвале')
#         return
#     print("=>", n)
#     elevator(n - 1)  #  5  4 3 2 1
#     print(n, end=' ')
#
#
# n1 = int(input('На каком этаже вы находитесь'))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res

# def sum_list(lst):  #  [1, 3, 5, 7, 9]
#     if len(lst) == 1:
#         print(lst, '=> lst[0]:', lst[0])
#         return lst[0]  #  9
#     else:
#         print(lst, '=> lst[0]:', lst[0])
#         return lst[0] + sum_list(lst[1:])  #  1 + 3 + 5 + 7 + 9
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):  #  254, 16
#     convert = '0123456789ABCDEF'
#     if n < base:
#         return convert[n]  # 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base]  #   to_str(n // base, base) + 'E'
#
#
# print(to_str(254, 16))


# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Berb'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))

# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Berb'], 'Alex', ['Bea', 'Bill'], 'Ann']
#
#
# def count_items(item_list):
#     count = 0  #  7
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))
#

#  Файлы

# f = open('text.txt', 'r')
# f = open(r'D:\Python\text.txt', 'r')
# print(f)
# print(*f)
# f.close()  #  закрывает и сохраняет файл
# print(f.closed)
# print(f.name)
# print(f.encoding)

# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('xyz.txt', 'w')
# f.write('This is line1.\nThis is line2.\nThis is line3.\n')
# f.close()

# f = open('xyz.txt')
# print(f.read())
#
# # print(f.readline())
# # print(f.readline(8))
# # print(f.readline())
# # print(f.readline())
# # f.close()
#
# print(f.readlines(16))
# print(f.readlines())
# f.close()

# count = 0
#
# f = open('xyz.txt')
# for line in f:
#     print(line)
#     count += 1
# f.close()
#
# print(count)

# f = open('xyz.txt')
# print(len(f.readlines()))
# f.close()


# f = open('test.txt', 'w')
# f.write('Hello\nWorld\n')
# f.close()

# lines = ['This is line1.', 'This is line2.', 'This is line3.']
# f = open('test1.txt', 'a')  #  'a' дозаписывает данные в конец файла или создает если файла нет
# # f.write('New text')
# f.writelines(lines)
# f.close()

# file = 'text2.txt'
# f = open(file, 'w')
# f.write('Замена строки в текстовом файле;\n'
#         'изменить строку в списке;\n'
#         'записать список в файл;\n')
# f.close()
# f = open(file, 'r')
# data = f.readlines()
# print(data)
# data[1] = 'Hello World!\n'
# print(data)
# f.close()
#
# f = open(file, 'w')
# f.writelines(data)
# f.close()


# f = open('text3.txt', 'w')
# lst = [str(i) for i in range(1, 100, 5)]
# print(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()

# f = open('text.txt')
# print(f.read(3))
# print(f.tell())  #  возвращает текущую позицию курсора в файле
# print(f.seek(1))  #  перемещает курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open('text.txt', 'r+')
# print(f.write('I am learning Python'))
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
# f.close()
#
# f = open('text.txt', 'a+')
# print(f.read())
# f.close()

# with open('text.txt', 'w' ) as f :
#     print(f.write('0123456789'))
# print(f.closed)
#
# with open('text.txt') as f:
#     print(f.read())

# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 5.47]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)
#
#
# with open('res.txt', 'w') as f:
#     f.write(get_line(lst))
#
# print('Файл записан')

# with open("res.txt") as f:
#     nums = f.read()
#
# print(nums)
#
# lst = list(map(float, nums.split()))
# print(lst)
# print(sum(lst))

# file_name = 'long.txt'
# with open(file_name, 'w') as f:
#     f.write('Файл — именованная область данных на носителе информации, используемая как базовый объект'
#              ' взаимодействия с данными в операционных системах.')
#
#
# def longest_world(file):
#     with open(file) as text:
#         lst = text.read().split()
#         print(lst)
#         max_lenght = len(max(lst, key=len))
#         print(max_lenght)
#         res = [word for word in lst if len(word) == max_lenght]
#
#         return res[0] if len(res) == 1 else res


# print(longest_world(file_name))


# text = 'Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n'
# with open('one.txt', 'w') as f:
#     f.write(text)
#
# with open('one.txt') as fr, open('two.txt', 'w') as fw:
#     for line in fr:
#         line = line.replace('Строка', 'Линия -')
#         fw.write(line)



#  Модули OS и OS.PATH

# import os

# print(os.getcwd())  #  путь к текущей директорией
# print(os.listdir())  #  список директорий и файлов
# print(os.listdir('.venv'))

# os.mkdir('folder')  #  создали папку
# os.rmdir('folder')  #  удалили папку

# os.makedirs('nest1/nest2/nest3')  #  создается папка с промежуточными директориями
# os.remove('xyz.txt')  #  удаление файла
# os.rename('one.txt', 'file_name.txt')
# os.rename('file_name.txt', 'nest1/file_name.txt') #  переименовыват файл,
# может его перемещать в существующую директорию
# os.renames("two.txt", "test/two.txt")  #  переименовыват файл,
#  может создавать директории, которых не существует при перемещении

# for root, dirs, files in os.walk('nest1', topdown=True):
# # for root, dirs, files in os.walk('nest1', topdown=False):
#     print('Root', root)
#     print('\tDirs', dirs)
#     print('\t\tFiles', files)

# def remove_empty_dirs(root_tree):
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директория {root} удалена')
#
#
# remove_empty_dirs('nest1')


# import os
# # import os.path
#
# print(os.path.split(r'D:\Python\nest1\nest2\nest3\text3.txt'))
# print(os.path.join(r'D:\Python', 'nest1', 'nest2', 'nest3', 'text3.txt'))
# print(os.path.exists(r'D:\Python\nest1\nest2\nest3\text3.txt'))
# print(os.path.exists(r'D:\Python\nest2\nest3\text3.txt'))
# print(os.path.isfile(r'D:\Python\nest1\nest2\nest3\text3.txt'))
# print(os.path.isfile(r'D:\Python\nest1\nest2\nest3'))
# print(os.path.isdir(r'D:\Python\nest1\nest2\nest3\text3.txt'))
# print(os.path.isdir(r'D:\Python\nest1\nest2\nest3'))



