# d = {
#     'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
# }
# for name in d:
#     print(name)
#     for region, volume in d[name].items():
#         print(region, ':', volume)
# name = input('Имя: ')
# if name in d:
#     region = input('Регион: ')
#     if region in d[name]:
#         print(d[name][region])
#         d[name][region] = input('Введите новое значение: ')
#         print(d[name])
# else:
#     print('Такого имени нет!')

#  второй вариант
# for name in d:
#     print(name)
#     for region in d[name]:
#         print(region, ':', d[name][region])
# person = input('Имя: ')
# region = input('Регион: ')
# print(d[person][region])
# new = int(input('Новое знач: '))
# d[person][region] = new
# print(d[person])