from math import sqrt


class Area:
    __count = 0

    @staticmethod
    def triangle_square(a, b, c):
        p = (a + b + c) / 2
        Area.__count += 1
        return sqrt(p * (p - a) * (p - b) * (p - c))

    @staticmethod
    def triangle_height(a, h):
        s = (a * h) / 2
        Area.__count += 1
        return s

    @staticmethod
    def square_box(a):
        s = a ** 2
        Area.__count += 1
        return s

    @staticmethod
    def square_rectangle(a, b):
        s = a * b
        Area.__count += 1
        return s

    @staticmethod
    def get_count():
        return Area.__count


print("Площадь треугольника по формуле Герона (3, 4, 5): ", Area.triangle_square(3, 4, 5))
print("Площадь треугольника через основание и высоту (6, 7): ", Area.triangle_height(6, 7))
print("Площадь квадрата (7): ", Area.square_box(7))
print("Площадь прямоугольника (2, 6): ", Area.square_rectangle(2, 6))
print("Количество подсчетов площади: ", Area.get_count())






