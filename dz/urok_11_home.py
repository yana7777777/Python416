
# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# print([i for i in lst if 'b' in i])
#
# print({i for i in lst if 'b' in i})
# print(tuple("B" if i[0] == "b" else "A" for i in lst))

# from random import randint

# lst = []
#
# for i in range(1, 5):
#     lst.append(i)
# print("Создали список: ", lst)
#
# print([(input("=> ")) for i in range(1)])
#
# print([randint(50, 100) for i in range(3)])
#
# print(tuple(i ** 2 for i in range(2)))

# tpl1 = tuple(int(input("=> ")) for i in range(1))
# print(tpl1)
# tpl2 = tuple(int(input("=> ")) for i in range(2))
# print(tpl2)
# tpl = tpl1 + tpl2
# print(tpl)
# print(len(tpl1))
# print(tpl.count(1))
# lst = list(tpl)
# print(lst, type(lst))
# lst[0] = 5
# print(lst)
# tpl = tuple(lst)
# print(tpl, type(tpl))

# t1 = tuple("Hello")
# t2 = tuple("World!")
# t3 = t1 + t2
# print(t3)
# print(t3.count('l'))
# print(t3.count('a'))

# if "l" in t3:
#     print(t3.index("l", 1, 8))
# else:
#     print("Такого элемента нет")

# if "l" in t3:
#     print(t3.count("l"))
# else:
#     print("Такого элемента нет")
#
# for i in t3:
#     print(i, end=" ")


# print({k: v for k, v in students.items()})
#
# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# # print({k: v for k, v in d.items()})
# print({k: v for k, v  in d.items() if v <= 2})

students = {"Игорь": 12, "Валентин": 7, "Виктор": 4, "Григорий": 9, "Дмитрий": 6}
summa = 0
average = 0
count_st = 0
for k, v in students.items():
    # print(count_st)
    summa += v
    count_st += 1
    average = summa / count_st
    print(round(average))
    print(summa)
    if v > average:
        # print("Средний балл: ", average)
        # print("Студенты с баллом выше среднего: ", sep=" ")
        print(k)
    # print(k, "=> ", v)


























