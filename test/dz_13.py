student = {}

n = int(input("Кол-во студентов: "))
s = 0
for i, j in enumerate(range(n), 1):
    name = input(str(i) + "-й студент: ")
    point = int(input("Балл: "))
    student[name] = point
    s += point

average = s / n
print(student)
print("Средний балл: ", round(average), ". Студенты с баллом выше среднего: ", sep="")


for i, j in student.items():
    if j > average:
        print(i)