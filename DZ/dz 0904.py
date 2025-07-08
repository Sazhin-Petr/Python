from math import sqrt


class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def sum(self):
        print(f'Сумма: {self.a + self.b}')

    def composition(self):
        print(f'Произведение: {self.a * self.b}')


class Right_Triangle(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)

    def hypotenuse(self):
        hyp = round(sqrt(self.a ** 2 + self.b ** 2), 2)
        print(f'Гипотенуза ABC {hyp}')
        return hyp

    def square(self):
        print(f'Площадь треугольника ABC {(self.a * self.b) / 2}')


Triangle = Right_Triangle(5, 8)
hyp = Triangle.hypotenuse()
print(f'Прямоугольный треугольник ABC ({Triangle.get_a()}, {Triangle.get_b()}, {hyp})')
Triangle.square()
print()
Triangle.sum()
Triangle.composition()
print()
Triangle.a = 10
Triangle.b = 20
Triangle.hypotenuse()
Triangle.sum()
Triangle.composition()
Triangle.square()