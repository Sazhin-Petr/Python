import json


class World:

    def __init__(self, country, city):
        self.country = country
        self.city = city

    @staticmethod
    def add(new_base):
        try:
            with open('dict_world.json', 'r', encoding='utf-8') as f:
                base = json.load(f)
        except FileNotFoundError:
            base = {}

        base.update(new_base)
        with open('dict_world.json', 'w', encoding='utf-8') as f:
            json.dump(base, f, indent=2, ensure_ascii=False)
        print('Файл сохранен')

    @staticmethod
    def remove_country(del_country):

        with open('dict_world.json', 'r', encoding='utf-8') as f:
            base = json.load(f)

        if del_country in base:
            base.pop(del_country)
            with open('dict_world.json', 'w', encoding='utf-8') as f:
                json.dump(base, f, indent=2, ensure_ascii=False)
            print('Страна удалена')
        else:
            print('Такой страны нет в базе')

    @staticmethod
    def find_country(country):
        with open('dict_world.json', 'r', encoding='utf-8') as f:
            base = json.load(f)

        if country in base:
            print(f'Данная страна находится в базе её столица {base[country]} ')
        else:
            print('Такой страны нет в базе, попробуйте её добавить!')

    @staticmethod
    def change_city(change_country, change_city):
        with open('dict_world.json', 'r', encoding='utf-8') as f:
            base = json.load(f)
        if change_country in base:
            base[change_country] = change_city
            with open('dict_world.json', 'w', encoding='utf-8') as f:
                json.dump(base, f, indent=2, ensure_ascii=False)
            print('Редактирование завершено')
        else:
            print('Такой страны нет в базе')

    def __str__(self):
        with open('dict_world.json', 'r', encoding='utf-8') as f:
            base = json.load(f)

        return base

    @staticmethod
    def print_info():
        with open('dict_world.json', 'r', encoding='utf-8') as f:
            base = json.load(f)

        return base


while True:
    print(f'{'*' * 30}\nВыбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n4 - редактирование данных'
          f'\n5 - просмотр данных\n6 - завершение работы')
    pos = int(input('Ввод: '))
    if pos == 1:
        country = input('Введите название страны: ')
        city = input('Введите название столицы страны: ')
        dict_world = {country: city}
        World.add(dict_world)

    elif pos == 2:
        del_country = input('Введите страну, которую желаете удалить: ')
        World.remove_country(del_country)

    elif pos == 3:
        country = input('Введите название страны которую хотите найти: ')
        World.find_country(country)

    elif pos == 4:
        change_country = input('Введите страну, в которой необходимо изменить столицу: ')
        change_city = input('Введите новую столицу: ')
        World.change_city(change_country, change_city)

    elif pos == 5:
        print(World.print_info())

    elif pos == 6:
        print('Работа завершена')
        break

    else:
        print('Введен некорректный номер')


# Нужно было до цикла создать файл и в каждой цифре вызывать только лишь фунцию и в нее вкладывать файл
# World.change_city(file)