# n = input('Введите число: ')
# res = 1
# while type(n) is not int:
#     try:
#         n = int(n)
#     except (ValueError, TypeError):
#         print('Введено не целое число!')
#         n = input('Введите число: ')
# while n != 0:
#     res *= n
#     n = int(input('Введите число: '))
# print('Результат: ', res)

# 2 решение

# res = 1
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     res *= n
# print('Результат:', res)