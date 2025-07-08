class Human:
    def __init__(self, fio, age):
        self.fio = fio
        self.age = age


class Student(Human):

    def __init__(self, fio, age, direct, group, mark):
        super().__init__(fio, age)
        self.direct = direct
        self.group = group
        self.mark = mark

    def print_info(self):
        return f'{self. fio} {self.age} {self.direct}  {self.group} {self.mark}'


class Teacher(Human):

    def __init__(self, fio, age, object, mark):
        super().__init__(fio, age)
        self.object = object
        self.mark = mark

    def print_info(self):
        return f'{self. fio} {self.age} {self.object}  {self.mark}'


class Graduate(Student):
    def __init__(self, fio, age, direct, group, mark, theme):
        super().__init__(fio, age, direct, group, mark)
        self.theme = theme

    def print_info(self):
        return f'{self. fio} {self.age} {self.direct}  {self.group} {self.mark} {self.theme}'


h1 = Student('Батодалаев Даши', 16, 'ГК', 'Web_011', 5)
h2 = Student('Загидуллин Линар', 32, 'РПО', 'PD_011', 5)
h3 = Graduate('Шугани Сергей', 15, 'РПО', 'PD_011', 5, 'Защита персональных данных')
h4 = Teacher('Даньшин Андрей', 38, 'Астрофизика', 110)
h5 = Student('Маркин Даниил', 17, 'ГК', 'Python_011', 5)
h6 = Teacher('Башкиров Адексей', 45, 'Разработка приложений', 20)

Human_list = [h1.print_info(), h2.print_info(), h3.print_info(), h4.print_info(), h5.print_info(), h6.print_info()]

for info in Human_list:
    print(info)