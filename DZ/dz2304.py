from abc import ABC, abstractmethod
from math import sqrt


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    def square(self):
        pass

    def paint(self):
        pass

    def print_info(self):
        pass


class Square(Shape):
    def __init__(self, a, color):
        self.a = a
        self.color = color

    def perimeter(self):
        super().perimeter()
        return self.a * 4

    def square(self):
        super().square()
        return self.a ** 2

    def paint(self):
        super().paint()
        fig = []
        for _ in range(self.a):
            fig.append('*' * self.a)
        return '\n'.join(fig)

    def print_info(self):
        super().print_info()
        return f'===Квадрат===\nСторона: {self.a}\nЦвет: {self.color}\nПлощадь: {Square.square(self)}\nПериметр: {Square.perimeter(self)}\n{Square.paint(self)}'


class Rectangle(Shape):
    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        self.color = color

    def perimeter(self):
        super().perimeter()
        return (self.a + self.b) * 2

    def square(self):
        super().square()
        return self.a * self.b

    def paint(self):
        super().paint()
        fig = []
        for _ in range(self.a):
            fig.append('*' * self.b)
        return '\n'.join(fig)

    def print_info(self):
        super().print_info()
        return (f'===Прямоугольник===\nДлина: {self.a}\nШирина: {self.b}\nЦвет: {self.color}\nПлощадь: {Rectangle.square(self)}\nПериметр: '
                f'{Rectangle.perimeter(self)}\n{Rectangle.paint(self)} ')

class Treangle(Shape):
    def __init__(self, a, b, color):
        self.a = a
        self.b = b
        self.color = color

    def perimeter(self):
        super().perimeter()
        return self.a * 2 + self.b

    def square(self):
        super().square()
        return round(self.a / 4 * sqrt(4 * self.b ** 2 - self.a ** 2), 2)

    def paint(self):
        super().paint()
        fig = []
        for i in range(self.b):
            stars = 2 * i + 1
            if stars > self.a:
                stars = self.a
            space = (self.a - stars) // 2
            paint = ' ' * space + '*' * stars + ' ' * space
            fig.append(paint)
        return '\n'.join(fig)

    def print_info(self):
        super().print_info()
        return (f'===Треугольник===\nСторона 1: {self.a}\nСторона 2: {self.b}\nСторона 2: {self.b}\nЦвет: {self.color}\nПлощадь: '
                f'{Treangle.square(self)}\nПериметр: {Treangle.perimeter(self)}\n{Treangle.paint(self)} ')


fig1 = Square(3, 'red')
# print(figure1.print_info())
print()
fig2 = Rectangle(3, 7, 'green')
# print(figure2.print_info())
print()
fig3 = Treangle(11, 6, 'yellow')
# print(figure3.print_info())

for shape in fig1, fig2, fig3:
    print(shape.print_info(), end='\n\n\n')