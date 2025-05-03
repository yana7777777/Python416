
from abc import ABC, abstractmethod
import math


class Shape:
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Square(Shape):
    def __init__(self, side, color):
        super().__init__(color)
        self.side = side

    def get_perimeter(self):
        return self.side * 4

    def get_area(self):
        return self.side * self.side

    def draw(self):
        return ("*  " * self.side + "\n") * self.side

    def info(self):
        print(f"=== Квадрат ===\nСторона: {self.side}\nЦвет: {self.color}"
              f"\nПлощадь: {self.get_area()}\nПериметр: {self.get_perimeter()}\n{self.draw()}\n")


class Rectangle(Shape):
    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width

    def get_perimeter(self):
        return (self.length + self.width) * 2

    def get_area(self):
        return self.length * self.width

    def draw(self):
        return ("*  " * self.width + "\n") * self.length

    def info(self):
        print(f"=== Прямоугольник ===\nДлина: {self.length}\nШирина: {self.width}\nЦвет: {self.color}"
              f"\nПлощадь: {self.get_area()}\nПериметр: {self.get_perimeter()}\n{self.draw()}\n")


class Triangle(Shape):
    def __init__(self, side_1, side_2, side_3, color):
        super().__init__(color)
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def get_perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def get_area(self):
        p = self.get_perimeter() / 2
        return round(math.sqrt(p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3)), 2)

    def draw(self):
        rows = []
        for n in range(self.side_2):  # 6, n = 2
            rows.append(" " * n + "*" * (self.side_1 - 2 * n))  # ['***********', ' *********', '  *******']
        rows.reverse()
        return "\n".join(rows)

    def info(self):
        print(f"=== Треугольник ===\nСторона 1: {self.side_1}\nСторона 2: {self.side_2}\nСторона 3: {self.side_3}"
              f"\nЦвет: {self.color}\nПлощадь: {self.get_area()}\nПериметр: {self.get_perimeter()}\n{self.draw()}\n")


fig = [Square(3, "red"), Rectangle(3, 7, "green"), Triangle(11, 6, 6, "yellow")]

for g in fig:
    g.info()

