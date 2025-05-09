# name = "admin"  # переменная
# # print("Hello, " + name + "!")
# age = 20
# # print(name + str(age))
# print(age)
# age = 15.5
# print(age)
# print(type(name))
# print(type(age))

# a = 4
# b = 5
# print(id(a))
# print(id(b))
# a = b  # 5
# print(a)
# print(b)
# print(id(a))
# print(id(b))

# a = b = c = 1
# print(a)
# print(b)
# print(c)

# a, b, c = 5, "Hello", 9.2
#
# print(a)
# print(b)
# print(c)

# _first_name = "admin"
# print(_first_name)

# PI = 3.14
# print(PI)

# name = "Никита"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.")


# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# # первый способ
# # c = a  # 1
# # a = b  # 2
# # b = c  # 1
# # второй способ
# # a, b = b, a
# # третий способ
# a = a + b  # 1 + 2 = 3
# b = a - b  # 3 - 2 = 1
# a = a - b  # 3 - 1 = 2
# print("a:", a)
# print("b:", b)

# print("строка \
# символов")
# print('строка \nсимволов')
# print("\tДокумент \"file.txt\"      находится     по пути: \rD\\folder\\file.txt")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + "___"
# print(s3 * 3)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(7 / 2)
# print(7 // 2)
# print(7 ** 2)
# print(7 % 2)

# a = 5
# b = 7
# c = 3
# res = a + b + c
# print("Сумма:", res)
# print("Произведение:", a * b * c)
# print("Среднее арифметическое:", res / 3)

# print(6 / 4 * 5 ** 2 + 7)  # 113
# print((6 + 4) * (5 ** 2 + 7))  # 320

# num = 10
# num += 5  # num = num + 5 = 15
# print(num)
#
# num -= 3  #  num = num - 3 = 12
# print(num)
#
# num **= 2  # num = num ** 2  144
# print(num)

# num = 4321
# print("Исходное число:", num)
# a = num % 10
# print("a:", a)
# num = num // 10
# # print(num)
# b = num % 10
# print("b:", b)
# num = num // 10
# # print(num)
# c = num % 10
# print("c:", c)
# num = num // 10
# # print(num)
# d = num % 10
# print("d:", d)
# print("Обратное число:", a * 1000 + b * 100 + c * 10 + d)


# num = 9753
# print("Исходное число:", num)
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print("Обратное число:", res)

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# # res = num1 + str(num2)
# print(res)

# print(int(3.8))
# print(round(3.8))
# print(type(round(3.8)))
# print(round(3.895, 2))
# print(type(round(3.899, 2)))

# a = '5.2'
# b = 10
# c = float(a) + b
# print(c)

# name = "Виктор"
# age = 28
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="", end=" ")
# print("Новая строка")

# name = input("Введите имя: ")
# print("Ваше имя:", name)

# num = input("Введите число: ")
# power = input("Введите степень: ")
# num = int(num)
# power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# num1 = int(input("Введите число 1: "))
# num2 = int(input("Введите число 2: "))
# num3 = int(input("Введите число 3: "))
# num4 = int(input("Введите число 4: "))
# sum1 = num1 + num2
# sum2 = num3 + num4
# res = sum1 / sum2
# print(round(res, 2))

# b1 = True
# b2 = False
# print(type(b1))
# print(b1 + 5)
# print(b2 + 5)

# print(bool("python"))
# print(bool(""))
# print(bool(" "))
# print(bool(5))
# print(bool(0))
# print(bool(0.1))
# print(bool(0.0))
# print(bool(False))
# print(bool(None))
#
# a = None
# print(a)
# print(type(a))

# print(7 == 7)
# print(2 + 5 == 7 / 3)
# print(2 + 5 != 7 / 3)
# print(8 > 5)
# print(8 > 8)
# print(8 >= 8)
# print(9 > 9)
# print(9 >= 9)
# print("python" > "Python")  # 112 > 80

# print(2 < 4 < 9)  # True && True => True
# print(2 * 5 > 7 >= 4 + 3)  # 10 > 7 >= 7  True && True => True
# print(3 * 3 <= 7 >= 2)  # 9 <= 7 >= 2  False && True =>
#
# a = "10"
# b = 10
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)  # True and True => True
# print(5 - 3 == 2 and 1 + 3 < 4)  # True and False => False
#
# print(5 - 3 == 2 or 1 + 3 == 4)  # True or True => True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True or False => True
#
# print(not 9 - 5)
# print(not 7 - 7)
#
# adfsdf = 5
# print("a:", adfsdf)

# print("строка текста строка текста строка текста строка текста строка текста строка текста строка текста строка
# текста "
#       "строка текста строка текста строка текста строка текста строка текста ")

# cnt = 5
# if cnt < 10:
#     # cnt = cnt + 1
#     cnt += 1
#     print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 15
# b = 25
# if a > b:
#     print("a > b")
# elif a == b:
#     print("a == b")
# else:
#     print("b > a")

# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
# c = input("Введите третью строку: ")
#
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or b == c or a == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")


# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")


# a = int(input("Введите номер месяца:"))
# if a == 12 or a == 1 or a == 2:
#     print("Зима")
# elif a == 3 or a == 4 or a == 5:
#     print("Весна")
# elif a == 6 or a == 7 or a == 8:
#     print("Лето")
# elif a == 9 or a == 10 or a == 11:
#     print("Ocень")
# else:
#     print("Нету таких месяцев")

# month = int(input("Введите номер месяца цифрой: "))
# if 1 <= month <= 2 or month == 12:
#     print("Время года - Зима")
# elif 3 <= month <= 5:
#     print("Время года - Весна")
# elif 6 <= month <= 8:
#     print("Время года - Лето")
# elif 9 <= month <= 11:
#     print("Время года - Осень")
# else:
#     print("Некорректное значение")

# season = int(input("Введите номер месяца: "))
# if 1 <= season <= 12:
#     print("Время года: ", end="")
#     if 1 <= season <= 2 or season == 12:
#         print("Зима")
#     if 3 <= season <= 5:
#         print("Весна")
#     if 6 <= season <= 8:
#         print("Лето")
#     if 9 <= season <= 11:
#         print("Осень")
# else:
#     print("Такого месяца нет")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ", end="")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if 5 <= n <= 9 or n == 0:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ворон", end="")
#     if n == 1:
#         print("а", n)
#     elif 2 <= n <= 4:
#         print("ы", n)
#     else:
#         print("", n)
# else:
#     print("Ошибка ввода")


# match выражение:
#     case шаблон_1:
#         действие_1
#     case шаблон_2:
#         действие_2
#     case _:
#         значение_по_умолчанию

# password = "user"
#
# match password:
#     case "admin":
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#     case _:
#         print("Пароль неверен")

# day = 'понедельник'
# time = 15
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 12 or 14 <= time <= 17:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")

# Тернарное выражение

# a, b = 30, 20
# print(a if a < b else b)

# a, b = 30, 20
# print("На 0 делить нельзя" if b == 0 else a / b)


# a = int(input("Введите число от 1 до 99: "))
# kop = a
# if 11 <= kop <= 14:
#     print(a, "копеек")
# elif 1 <= a <= 10 or 15 <= a <= 99:
#     kop = kop % 10
#     if kop == 1:
#         print(a, "копейка")
#     elif 2 <= kop <= 4:
#         print(a, "копейки")
#     else:
#         print(a, "копеек")
# else:
#     print("Значения должны быть от 1 по 99")

# a = int(input("Введите число от 1 до 99: "))  # 53
# kop = a
# if 11 <= kop <= 14:
#     print(a, "копеек")
# elif 1 <= a <= 99:
#     kop = kop % 10
#     if kop == 1:
#         print(a, "копейка")
#     elif 2 <= kop <= 4:
#         print(a, "копейки")
#     else:
#         print(a, "копеек")
# else:
#     print("Значения должны быть от 1 по 99")

# Исключения

# a = 5
# b = 0
# print(a / b)

# try:  # попытаться
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")
#
# print("Код далее")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на 0")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или нельзя делить на 0")
# else:  # когда в блоку try не возникло исключение
#     print("Все нормально. Вы ввели", n, "и", m)
# finally:  # выполнится в любом случае
#     print("Конец программы")

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(str(n) + " " + str(m))

# Циклы

# while уловие:
#     блок_кода

# итерация - один шаг цикла

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1
#
# print()
#
# j = 2
# while j <= 20:
#     print(j, end=" ")
#     j += 2

# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Укажите количество символов: "))
# # print("*" * n)
# while n > 0:
#     print("*", end="")
#     n -= 1

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     if a % 2:  # 1 3 5
#         print(a)
#         res += a
#     a += 1
# print("Сумма нечетных чисел:", res)

# n = input("Введите целое число: ")
#
# while type(n) is not int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# res = 1
# while True:
#     n = int(input("введите  число: "))
#     if n == 0:
#         break
#     res *= n
# print(res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# print("Цикл окончен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# n = int(input("Количество символов: "))
# symbol = input("Тип символа: ")
# orient = int(input("0 - горизонтальная\n1 - вертикальная\nориентация линии: "))
#
# # while orient != "0" and orient != "1":
# #     orient = input("Укажите Ваш выбор числом 0 или 1: ")
# i = 0
# while i < n:
#     if orient == 1:
#         print(symbol)
#     else:
#         print(symbol, end=" ")
#     i += 1


# for element in collection:
#     print(element)

# for i in "Hello":
#     print(i)
#
# for i in "Hello", "World":
#     print(i)

# range(start=0, stop, step=1)

# for i in range(10):  # i = 0, i < 10; i += 1
#     print(i, end=" ")
#
# print()
# j = 10
# while j > 0:
#     print(j, end=" ")
#     j -= 2


# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(11, 100, 11):
#     print(i, end=" ")
#
# print()
#
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     # if i == 1:
#     #     break
# else:
#     print("Конец цикла")


# for i in range(3):  # for(let i = 0; i < 3; i++)  # i = 3
#     print("+++")
#     for j in range(2):  # for(let j = 0; j < 2; j++) # j = 2
#         print("-----")


# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):  # 3
#     for j in range(w):  # 1
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

# string = [letter * 2 for letter in "Python"]
# print(string)
#
# for letter in "Python":
#     print(letter * 2, end="\t")

# num = [i for i in range(30) if i % 2 == 0]
# print(num)
#
# for i in range(30):
#     if i % 2 == 0:
#         print(i, end="\t")


# Список (list)
# nums = [8, 3, 9, 4, 1]
# print(nums)
# print(type(nums))
#
# num1 = list()
# print(num1)
# print(type(num1))

# nums = [8, 3, 9, 4, 1, "one", True]
# print(nums)
# print(nums[0])
# print(nums[-5])
# print(nums[4])
# print(nums[-1])
# print(nums[-2])

# nums = [8, 3, 9, 4, 1]
# print(nums)
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)

# nums = [8, 3, 9, 4, 1]
# print(nums, id(nums))
# print(nums[0], id(nums[0]))
# print(nums[1], id(nums[1]))
# nums[1] = 256
# print(nums[1], id(nums[1]))
# print(nums, id(nums))
# print("Длина списка:", len(nums))

# nums = [8, 3, 9, 4, 1]
# nums2 = [11, 12, 13]
# n = nums + nums2
# print(n)
# print(n * 3)

# print(list("Hello"))
#
# print(range(10))
# print(list(range(10)))
# print(list(range(2, 10)))
# print(list(range(10, 2, -2)))

# [выражение for переменная in последовательность]

# a = [0 for i in range(1, 5)]  # 0 1 2
# print(a)  # [0, 0, 0, 0, 0]

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)  # [1, 4, 9, 16]


# a = [0] * int(input("Введите количество элементов списка: "))  # 5 => [0,0,0,0,0]
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]  # range(0, -1)
# print(a)

# a = list(range(10, 100, 10))
# print(a)
#
# for i in range(len(a)):  # 0 1 2 3 4 5 6 7 8
#     print(a[i] + 2, end=" ")
# print()
#
# for i in a:
#     print(i + 2, end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print("Сумма отрицательных элементов:", s)

# for i in a:
#     if i < 0:
#         s += i
# print("Сумма отрицательных элементов:", s)


# i = 0
# while i < len(a):
#     if a[i] < 0:
#         s += a[i]
#     i += 1
# print("Сумма отрицательных элементов:", s)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
#
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")
# print()
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# n = list(range(21, 26))
# print(n)
# k = s = 0
# # for i in range(len(n)):
# # if n[i] % 2 == 0:
# #     k += 1
# # else:
# #     s += n[i]
#
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
#
# print("Количество четных элементов:", k)
# print("Сумма нечетных элементов:", s)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# sum1 = kol = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         kol += 1
#         sum1 += a[i]
# print("среднее арифметическое", sum1 / kol)

# lst = [7, 9, 2, 1, 17]
# print(lst)
# lst[0], lst[1] = lst[1], lst[0]
# print(lst)

# Срез
# список[start:stop:step]

# s = [9, 7, 2, 1, 17, 8]
# print(s)
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[::2])
# print(s[:])
# print(s[0:-1])
# print(s[-1:0:-1])
# print(s[10:20])

# lst = list(range(1, 8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[::-7])
# print(lst[-1:])
# print(lst[3:4])
# print(lst[4:7])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])

# st = "123456"
# print(st[1:3])
# num = st[::-1]
# print(num)
# print(type(num))
# num = int(num)
# print(num)
# print(type(num))

# lst = list(range(1, 8))
# print(lst)
# lst[1:3] = [0, 0, 0, 0]
# print(lst)
# lst[1:2] = [20]
# lst[3] = [40, 50]
# print(lst)
# lst[15:16] = [100]
# print(lst)

# print(len(lst))

# Методы списков

# lst = list(range(1, 8))
# print(lst)
# lst.append(99)  # добавляет один элемент в конец списка
# print(lst)
# lst.extend([1, 2, 3])   # добавляет список элемент в конец списка
# print(lst)
# lst.insert(1, 100)  # добавляет элемент (второй параметр) по заданному индексу (первый параметр)
# print(lst)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)  # [5,6,7,8,9]
# print(s)

# a = [5, 9, 2, 1, 4, 3, 4, 2]
# b = [4, 2, 1, 3, 7, 2]
# c = []  # [2]

# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:  # 1 == 1
#             c.append(i)
#             break

# for element in a:
#     if element in b and element not in c:  # [2, 1, 4, 3, 4, 2]
#         c.append(element)
#
# print(c)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# b = []
#
# for i in range(len(a)):
#     if a[i] not in b:
#         b.append(a[i])  # [1, 3, 5, 6, 2, 4, 7]
# print(b)

# lst = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# new_lst = []
# i = 0
# for element in lst:
#     k = element   # 5
#     for j in lst:  # 5
#         if k == j:  # 5 == 5
#             i += 1  # i = 1
#     if i == 1:
#         # print(k, end=" ")
#         new_lst.append(k)  # [3, 5]
#     i = 0
#
# print(new_lst)


# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# b = []

# for i in range(len(a)):
#     if a.count(a[i]) == 1:
#         # b.append(a[i])  # [3, 5, 4, 7]
#         print(a[i], end=" ")
# print(b)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7, 6]
# num = a.count(6)
# print(num)


# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(a)
# for i in a:  # 7
#     if a.count(i) == 1:  # 1 == 1
#         print(i, end=" ")  # 3 5 4 7


# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# # a = ["red", "yellow", "green"]
# print(a)
# for i in a:  # 1 3 5 6 2 4 6 1 2 7
#     # print(i, end=" ")
#     if a.count(i) == 1:  # 1 == 1
#         print(i, end=" ")  # 3 5 4 7
#
# print()
# for i in range(len(a)):  # 0 1 2 3 4 5 6 7 8 9
#     # print(a[i], end=" ")
#     if a.count(a[i]) == 1:
#         print(a[i], end=" ")

# a = [1, 2, 3, 55, 66]
# b = [11, 22, 33]
# c = []
#
# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):  # 0 1 2
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):  # range(3, 5):
#     c.append(b[i])


# if len(b) > len(a):
#     for i in range(len(a)):  # 0 1 2
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # range(3, 5):
#         c.append(b[i])
# else:
#     for i in range(len(b)):  # 0 1 2
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):  # range(3, 5):
#         c.append(a[i])

# print(c)  # [1, 11, 2, 22, 3, 33, 4, 2]

# lst = [11, 1, 22, 2, 33, 3, 55, 66]

# lst[:] = []
# del lst[2:7]

# lst.remove(22)  # удаляет элемент из списка по значению (первое вхождение)
# print(lst)
#
# last = lst.pop()  # удаляет последний элемент из списка и возвращает его
# print(last)
# print(lst)
# second = lst.pop(-2)  # удаляет элемент индексу из списка и возвращает его, если индекса нет, то получим исключение
# print(second)
# print(lst)
#
# lst.clear()  # удалил все значения из списка
# print(lst)

# print("Введите элементы списка: ")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# print("Введите индекс: ")
# k = int(input("k = "))
# a.pop(k)
# print(a)


# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# value = 33
# if value in lst:
#     ind = lst.index(value, 5, 9)  # возвращает индекс первого вхождения искомого элемента, можно указать
#     # диапазон от какого до какого индекса мы производим поиск, может выбрасываться исключение ValueError -
#     # если элемент не найден
#     print(ind)
# print(lst)

# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# a = lst.copy()  # создает копию списка по другому адресу
# print(lst, id(lst))
# print(a, id(a))
#
# a.append(100)
# print(lst)
# print(a)
#
# lst[0] = 256
# print(lst)
# print(a)

# print(dir(list))
#
# lst = [11, 1, 22, 2, 33, 3, 55, 66, 33]
# # lst.reverse()  # развернул элементы списка в противоположную строну
# # print(lst)
#
# lst.sort(reverse=True)
# print(lst)
#
# st = "Hello"
# new_lst = sorted(st, reverse=True)
# print(new_lst)
# print(st)

# s = ['Виталий', 'Сергей', 'Александр', 'Анна']
# s.sort(key=len)
# print(s)

# Генерация случайных данных

# import random

# print(random.random())
# print(random.randint(5, 10))
# print(random.randrange(5, 10, 2))
#
# print(random.uniform(10.5, 25.5))

# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# s = [55, 66, 77, 88, 99, 5, 7, 9, 1, 2, 4, 3, 8]
#
# # print(random.choice(city_list))
# # print(random.choice(s))
# # print(random.choices(city_list, k=3))
# # print(random.choices(s, k=3))
# random.shuffle(city_list)
# random.shuffle(s)
# print(city_list)
# print(s)

# import random

# mas1 = [random.randint(0, 100) for i in range(10)]
# print(mas1)
# mas = mas1.copy()
# mas.sort()
# # print(mas)
# min_ = mas[0]
# print("Min =", min_)
# ind = mas1.index(min_)
# print("Index min =", ind)
# del mas1[:ind]
# print(mas1)


# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# print(len(mas))  # длина списка
# print(min(mas))  # минимальный элемент из списка
# print(max(mas))  # максимальный элемент из списка
# print(sum(mas))  # сумма элементов списка


# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# maximum = max(mas)
# print("Max =", maximum)
# mas.remove(maximum)
# print(mas)
# print("Max =", maximum)
# mas.insert(0, maximum)
# print(mas)

# mas = [random.randint(0, 10) for i in range(10)]
# print(mas)
# print(2 not in mas)

# lst = []
# # if len(lst) == 0:
# #     print("Список пустой")
#
# print(bool(lst))
#
# if not lst:
#     print("Список пустой")
# else:
#     print("В списке есть элементы")

# m = [
#     [1, 2, 3, 4],  # 0
#     [5, 6, 7, 8],  # 1
#     [9, 10, 11, 12]  # 2
# ]
# print(m)
# # print(len(m))
# # print(m[1][2])
# # print(m[2][1])
# # print(m[1][3])
#
# print("Вариант 1")
# for row in range(len(m)):  # row = 1  # 0 1 2
#     for col in range(len(m[row])):  # col = 0  # 0 1 2 3
#         print(m[row][col], end="\t")
#     print()
#
# print("Вариант 2")
# for i in m:
#     for j in i:
#         print(j, end="\t")
#     print()

# Модули

# import math
#
# print(math.sqrt(4))  # корень
# print(math.ceil(3.2))  # округление в верхнюю сторону
# print(math.floor(3.8))  # округление в нижнюю сторону

# import math as m
#
# print(m.sqrt(4))
# print(m.ceil(3.2))
# print(m.floor(3.8))

# from math import *
#
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.8))

# from math import sqrt, ceil, floor
#
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.8))

# import math
# print(dir(math))

# from math import pi
#
# # print(pi)
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности:", round(2 * pi * radius, 2))

import time
from os import remove

# import locale
#
# print(time.time())
# print(time.ctime(748863169))
# print(time.localtime())
# res = time.localtime()
# print(res.tm_year, "-0", res.tm_mon, "-0", res.tm_mday, sep="")
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(64797995)))
#
# locale.setlocale(locale.LC_ALL, "ru")
# print(time.strftime("Сегодня: %B %d, %Y, %A"))

# start = time.monotonic()
# pause = 5
# print("Программа запущена")
# time.sleep(pause)
# result = time.monotonic() - start
# print("Программа выполнена за", result, "секунд")


# a = 500
# for i in range(a, -1, -1):
#     time.sleep(1)
#     print(i)

# import math
# from math import sqrt, pi
#
# shape = int(input("Выбор фигуры:\n1-треугольник\n2-прямоугольник\n3-круг\n: "))
# s = None
#
# if shape == 1:
#     a = int(input("Введите сторону a = "))
#     b = int(input("Введите сторону b = "))
#     c = int(input("Введите сторону c = "))
#     p = (a + b + c) / 2
#     s = sqrt(p * (p - a) * (p - b) * (p - c))
#
# elif shape == 2:
#     a = int(input("Введите сторону a = "))
#     b = int(input("Введите сторону b = "))
#     s = a * b
#
# elif shape == 3:
#     radius = int(input("Введите радиус = "))
#     s = pi * radius ** 2
# else:
#     print("Такой фигуры не существует")
#
# print(round(s, 2))

# Функции

# def hello(name, age):
#     print("Меня зовут " + str(name) + ". Мне " + str(age) + " лет.")
#
#
# hello("Irina", 28)
# hello("Ivan", 15)

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)

# get_sum("abc", "def")

# def print_line(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# print_line(9, "+", "-")
# print_line(7, "X", "0")


# def get_sum(a, b):
#     print("Hello")
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)


# print(get_sum(5, 10))

# def max_value(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(max_value(9, 6))
# print(max_value(9, 16))

# def add(x, y):
#     if x > y:
#         return x - y
#     else:
#         q = x + y
#         return q
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# print(add(a, b))


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst

# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# def is_first_big(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# # print(is_first_big(10, 5))
# # print(is_first_big(5, 10))
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if is_first_big(a, b):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше первого")

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(7, 9, d=3, c=5))
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")


# def set_param(count=20, symbol="-"):
#     print(count * symbol)
#
#
# set_param(10, "+")
# set_param(5, "*")
# set_param(15, "#")
# set_param(7)
# set_param()


# def func(a, b=0):
#     return a + b
#
#
# print(func(2, 5))
# print(func(b=2, a=5))
# print(func(2))

# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)
# print(lst1 is lst2)
#
# a = "Hello"
# b = "Hello"
# print(a, id(a))
# print(b, id(b))
# print(a == b)
# print(a is b)

# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))
# lst1.pop(1)
# print(lst1, id(lst1))


# a = "Hello"
# print(a, id(a))
# a = a + "!"
# print(a, id(a))


# a = 5
# print(a, id(a))
# a = a + 3
# print(a, id(a))


# Кортеж (кортеж)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
#
# print(lst[1])
# print(tpl[1])
#
# lst[1] = 50
# print(lst)

# a = (1, 2, 3, 4, 5, 6)
# print(a, type(a))

# a = tuple("Hello")
# print(a, type(a))


# a = (1, 2, 3, 4, 5, 6)
# print(a[2])
# print(a[1:3])

# from random import randint
#
# print(tuple(i + 2 for i in range(10)))

# print(tuple(input("-> ") for i in range(5)))

# print(tuple(randint(50, 100) for i in range(10)))

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# # print(t3 * 2)
# print(t3)


# print(len(t3))

# print(t3.count('l'))
# print(t3.count('a'))
#
# # print(t3.index("l", 9))
# if 'e' in t3:
#     print(t3.index("e"))
# else:
#     print("Такого элемента нет")

# for i in t3:
#     print(i, end=" ")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) == 1:
#             return tpl[tpl.index(el):]  # tpl[2:]
#         else:
#             first = tpl.index(el)  # 1
#             second = tpl.index(el, first + 1) + 1  # 4 + 1 -> 5
#             print("first", first)
#             print("second", second)
#             return tpl[first:second]  # tpl[1:5]  #
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# t = (True, 11, "Python", (4, 5, 6), ["hello", "world"])
# print(t, id(t))
# t[4][0] = 'new'
# print(t, id(t))
# t[4].append("hi")
# print(t, id(t))

# Распаковка кортежа
# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t
# # x, y, z = 1, 2, 3
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married


# user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])
# first_name, year, married = user

# first_name, year, married = get_user()
# print(first_name)
# print(year)
# print(married)


# lst = [1, 2, 3, 4, 5]
# print(lst, type(lst))
# tpl = tuple(lst)
# print(tpl, type(tpl))
# lst2 = list(tpl)
# print(lst2, type(lst2))
# lst2.append(6)
# tpl2 = tuple(lst2)
# print(tpl2, type(tpl2))

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))),
# )
#
# print(countries)
# for country in countries:
#     country_name, country_population, cities = country
#     # print(cities)
#     print("\nСтрана: ", country_name, ", население = ",  country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")

# tpl = tuple(input("Введите строку: "))
# print(tpl)
#
# lst = []
# for i in range(len(tpl)):
#     if tpl[i] not in lst:
#         lst.append(tpl[i])
#
# print(lst)
# for i in range(len(lst)):
#     print("Количество", lst[i], "=", tpl.count(lst[i]))
