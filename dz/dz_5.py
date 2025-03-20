

lst = [int(input(" -- > ")) for i in range(int(input("n = ")))]
summa = 0
for i in range(len(lst)):
    if lst[i] < 0:
        summa += lst[i]
print("сумма отрицательных элементов", summa)


