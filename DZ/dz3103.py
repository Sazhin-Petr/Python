class CAR:

    def __init__(self, model, year, maker, power, color, price):
        self.model = model
        self.year = year
        self.maker = maker
        self.power = power
        self.color = color
        self.price = price

    def print_info(self):
        print('Название модели: ', self.model)
        print('Год выпуска: ', self.year)
        print('Производитель: : ', self.maker)
        print('Мощность двигателя: ', self.power, 'л.с.')
        print('Цвет машины: ', self.color)
        print('Цена: ', self.price)

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_maker(self, maker):
        self.maker = maker

    def get_maker(self):
        return self.maker

    def set_power(self, power):
        self.power = power

    def get_power(self):
        return self.power

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


car1 = CAR('X7 M50i', 2021, 'BMW', '530', 'white', 10790000)
car1.print_info()
car1.set_model('RX7')
car1.set_year('2023')
car1.set_maker('Audi')
car1.set_power('650')
car1.set_color('Black')
car1.set_price('1000000')
car1.print_info()
