# n = int(input('Введите число от 1 до 99: '))
# if 1 <= n <= 99:
#     print(n, end='')
#     if (n % 10 == 1) and n != 11:
#         print(' копейка')
#     elif (n % 10 == 2) and (n != 12) or (n % 10 == 3) and (n != 13) or (n % 10 == 4) and (n != 14):
#         print(' копейки')
#     else:
#         print(' копеек')
# else:
#     print('Введено не верное число!')
#

# age = int(input('Введите свой возраст: '))
# if age >= 16:
#     print('Вы можете получить права!')
# else:
#     print('Права вам не доступны')

# age = int(input('Введите свой возраст '))
# if age < 5:
#     print('Вход бесплатный!')
# elif 5 <= age <= 17:
#     print('Вход стоит 10 баксов!')
# else:
#     print('Вход стоит 20 баксов!')


# cost = int(input('ВВедите стоимость покупки: '))
# age = int(input('Введите возраст: '))
# if cost > 100 and age <= 65:
#         print('Скидка 10%')
# elif cost > 100 and age > 65:
#         print('Скидка 15%')
# else:
#     print('Скидки нет!')

a = int(input('Введите число: '))
kop = a   # 55
if 11 <= kop <= 14:
    print(a, 'копеек')
elif 1 <= kop <= 99:
    kop = kop % 10
    if kop == 1:
        print(a, 'копейка')
    elif 2 <= kop <= 4:
        print(a, 'копейки')
    else:
        print(a, 'копеек')
else:
    print('недопустимое значение')