number = num = int(input('Введите пятизначное число: '))
a = num % 10
num //= 10
b = num % 10
num //= 10
c = num % 10
num //= 10
d = num % 10
num //= 10
e = num % 10
res1 = a * b * c * d * e
print('Произведение цифр числа ', number, ': ', res1, sep='')
res2 = (a + b + c + d + e) / 5
print('Среднее арифметическое:', res2)
