# делаю по записи лекции
# задачи в уроке 25
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @staticmethod
#     def __check_value(s):
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     def __set_coord_x(self, x):
#         print("Вызов __set_coord_x")
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Не верный формат данных")
#
#     def __get_coord_x(self):
#         print("Вызов __get_coord_x")
#         return self.__x
#
#     def __del_coord_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#
#     coordX = property(__get_coord_x, __set_coord_x, __del_coord_x)
#
#
# p1 = Point(5, 10)
# # print(p1.__set_coord_x(50))
# p1.coordX = "abc"
# print(p1.coordX)
# del p1.coordX
# print(p1.__dict__)


# 2-й вариант задачи с декаратором @property - сначала getter потом setter
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(s):
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Не верный формат данных")
#
#     @x.deleter
#     def x(self):
#         del self.__x
#
#     # x = property(__get_coord_x, __set_coord_x, __del_coord_x)
#
#
# p1 = Point(5, 10)
# p1.x = 50
# print(p1.x)
# del p1.x
# print(p1.__dict__)


# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.__old = old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Igor"
# print(p1.name)
# p1.old = 31
# print(p1.old)
# print(p1.__dict__)
# del p1.name
# print(p1.__dict__)


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# p4 = Point()
#
#
# print(Point.get_count())
# print(p1.get_count())


# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# print(inc(10), dec(10))
#
#
# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# ch = Change()
# print(ch.inc(10), Change.dec(10))


# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         mx = a
#         if b > mx:
#             mx = b
#         if c > mx:
#             mx = c
#         if d > mx:
#             mx = d
#         return mx
#
#     @staticmethod
#     def min(*args):
#         mn = args[0]
#         for i in args:
#             if i < mn:
#                 mn = i
#         return mn
#
#     @staticmethod
#     def average(*args):
#         return sum(args) / len(args)
#
#     @staticmethod
#     def factorial(n):
#         fact = 1
#         for i in range(1, n + 1):
#             print(i, end="")
#             fact *= i
#         return fact
#
#
# print("Максимальное число: ", Numbers.max(3, 5, 7, 9))
# print("Минимальное число: ", Numbers.min(3, 5, 7, 9))
# print("Среднее арифметическое: ", Numbers.average(3, 5, 7, 9))
# print(" Факториал: ", Numbers.factorial(5))


# делаю по записи лекции
# задачи в уроке 26


# делаю по записи лекции
# задачи в уроке 29

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"{self.name}"
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)
# print(cat.__dict__)

# import math
#
#
# class Point:
#     __slots__ = ("x", "y", "__length")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(10, 20)
# # p1.z = 30
# # print(p1.__dict__)
# print(p1.length)
# p1.length = 10
# print(p1.length)
# # print(p1.__slots__)


# множественное наследование_урок_29

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# dog = Dog('Buddy')
# dog.bark()
# dog.sleep()
# dog.play()


# class A:
#     def __init__(self):
#         print("Инициализатор класса А")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#
# class C(A):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Инициализатор класса D")
#
#
# d = D()
# print(D.mro())
# print(D.__mro__)


# class A:
#     def __init__(self):
#         print("Инициализатор класса А")
#
#
# class AA:
#     def __init__(self):
#         print("Инициализатор класса AA")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#
# class C(AA):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Инициализатор класса D")
#
#
# d = D()
# print(D.mro())


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор класса Styles")
#         self.color = color
#         self.width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инициализатор класса Pos")
#         self.sp = sp
#         self.ep = ep
#         # Styles.__init__(self, *args)
#         super().__init__(*args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self.sp}, {self.ep},{self.color}, {self.width} ")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()

# миксины

# class Goods:
#     def __init__(self, name, weight, price):
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#         super().__init__()
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 17:15")
#
#
# class Notebook(Goods, MixinLog):
#     pass
#
#
# n = Notebook("HP", 1.5, 35000)
# n2 = Notebook("HP", 1.9, 10000)
# n.print_info()
# n.save_sell_log()
# n2.print_info()
# n2.save_sell_log()

# перегрузка операторов (инф: словари и множества не работают с оператором +)
# число секунд в одном дне: 24 * 60 min * 60sec = 86400

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом int")
#         self.sec = sec
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec % other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return self.sec == other.sec
#
#     def __gt__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return self.sec > other.sec
#
#     def __ge__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return self.sec >= other.sec
#
#     def __lt__(self, other):
#         return not self.__gt__(other)
#
#     def __le__(self, other):
#         return not self.__ge__(other)
#
# # c1 = Clock(100)
# # c2 = Clock(200)
# # print(c1.get_format_time())
# # print(c2.get_format_time())
# # c1 += c2
# # print(c1.get_format_time())
#
#
# c1 = Clock(600)
# print("c1:", c1.get_format_time())
# c2 = Clock(200)
# # print("c2:", c2.get_format_time())
# c3 = c1 - c2
# print("c1 - c2:", c3.get_format_time())
# c3 = c1 * c2
# print("c1 * c2:", c3.get_format_time())
# c3 = c1 // c2
# print("c1 // c2:", c3.get_format_time())
# c3 = c1 % c2
# print("c1 % c2:", c3.get_format_time())
# c1 -= c2
# print("c1 -= c2:", c1.get_format_time())
# c1 *= c2
# print("c1 *= c2:", c1.get_format_time())
# c1 //= c2
# print("c1 //= c2:", c1.get_format_time())
# c1 %= c2
# print("c1 %= c2:", c1.get_format_time())
#
# # операторы сравнений перегрузка
# c1 = Clock(100)
# c2 = Clock(100)
# print("c1:", c1.get_format_time())
# print("c2:", c2.get_format_time())
# if c1 == c2:
#     print("Время равно")
# else:
#     print("Время разное")
# print("c1:", c1.get_format_time())
# print("c2:", c2.get_format_time())
# print("*" * 20)
# c1 = Clock(100)
# c2 = Clock(100)
# c3 = c1 + c2
# print("c1:", c1.get_format_time())
# print("c2:", c2.get_format_time())
# print("c3:", c3.get_format_time())
# print("c3 > c1:", c3.get_format_time() > c1.get_format_time())
# print("c3 >= c1:", c3.get_format_time() >= c1.get_format_time())
# print("c3 < c1:", c3.get_format_time() < c1.get_format_time())
# print("c3 <= c1:", c3.get_format_time() <= c1.get_format_time())


# урок 33

# import csv

# with open("data.csv") as f:
#     file_reader = csv.reader(f, delimiter=",")
#
#     for row in file_reader:
#         print(row)

# with open("host.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(['hostname', 'vendor', 'model', 'location'])
#     writer.writerow(['cw1', 'Cisco', '3750', 'London'])
#     writer.writerow(['cw2', 'Cisco', '3850', 'Liverpool'])
#     writer.writerow(['cw3', 'Cisco', '3650', 'Liverpool'])
#     writer.writerow(['cw4', 'Cisco', '3650', 'London'])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['cw1', 'Cisco', '3750', 'London'],
#         ['cw2', 'Cisco', '3850', 'Liverpool'],
#         ['cw3', 'Cisco', '3650', 'Liverpool'],
#         ['cw4', 'Cisco', '3650', 'London']]
#
# with open("sw_data.csv", "w") as f:
#     writer = csv.writer()









