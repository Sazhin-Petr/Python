# n = int(input('Количество студентов: '))
# name = []
# mark = []
# for i in range(1, n):
#     print(i, end='')
#     name1 = input(' - й , студент: ')
#     name.append(name1)
#     mark1 = int(input('Балл: '))
#     mark.append(mark1)
# sr = round(sum(mark) / len(mark))
# print('Средний балл: ', sr, '. Студенты с баллом выше среднего:')
# group = dict(zip(name, mark))
# for keys, valius in group.items():
#     if valius > sr:
#         print(keys)

#  2 тип решения

# c = int(input('введите колво списка'))
# a = {input('введите имя'): int(input('введите балл') for i in range(c))}
# sr_bal = round(sum(a.values()) / c)
# print('средний балл ', sr_bal, '\nстуденты с был выше')
# # for i in a:
# #     if a[i] > sr_bal:
# #         print(i)
# for k, v in a.items():
#     if v > sr_bal:
#         print(k)


#  решил преподаватель
student = {}
c = int(input('введите колво списка'))
for i in range(c):
    name = input(str(i + 1) + '-й студент')
    point = int(input('балл'))
    student[name] = point  #  создание словаря
sr_bal = round(sum(student.values()) / c)
print('средний балл ', sr_bal, '\nстуденты с был выше')
for k, v in student.items():
    if v > sr_bal:
        print(k)

 c = int(input('введите колво списка'))
a = {input(str(i) + 'введите имя'): int(input('введите балл') for i, j in enumerate(range(c), 1)}