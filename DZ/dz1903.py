pos1 = int(input())
pos2 = int(input())
text = """Замена строки в текстовом файле;
изменить строку в списке;
записать список в файл;"""
with open('DZ.txt', 'w') as f:
    f.write(text)
with open('DZ.txt', 'r') as f:
    lst = f.readlines()
    if pos1 <= len(lst) and pos2 <= len(lst):
        lst[pos1], lst[pos2] = lst[pos2] + '\n', lst[pos1] + '\n'
        with open('DZ.txt', 'w') as f:
            f.writelines(lst)
    else:
        print('Число строк документа меньше введенных значений!')


