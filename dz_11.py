import math
from math import sqrt, pi

n = int(input("выберите фигуру:\n1-треугольник\n2-прямоугольник\n3-круг\nВведите номер фигуры: "))

s = None

if n == 1:
    print("Вы выбрали треугольник \n")
    a = int(input("Введите сторону а: "))
    b = int(input("Введите сторону b: "))
    c = int(input("Введите сторону c: "))
    p = a + b + c / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print("Площадь треугольника = ", round(s, 2))
elif n == 2:
    print("Вы выбрали прямоугольник \n")
    a = int(input("Введите сторону а: "))
    b = int(input("Введите сторону b: "))
    s = a * b
    print("Площадь прямоугольника = ", round(s, 2))
elif n == 3:
    print("Вы выбрали круг \n")
    r = int(input("Введите радиус r: "))
    s = pi * r ** 2
    print("Площадь круга = ", round(s, 2))
else:
    print("Что-то пошло не так. Попробуйте еще раз.")


