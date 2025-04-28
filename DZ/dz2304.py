from abc import ABC, abstractmethod


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
        return f'\nСторона: {self.a}\nЦвет: {self.color}\nПлощадь: {Square.square(self)}\nПериметр: {Square.perimeter(self)}\n{Square.paint(self)}'


figure1 = Square(3, 'red')
print('===Квадрат===', figure1.print_info())


