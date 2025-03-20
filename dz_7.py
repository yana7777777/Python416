
import random

mas1 = [random.randint(0, 100) for i in range(10)]
print(mas1)
mas = mas1.copy()
mas.sort()
print(mas)
min_ = mas[0]
print("min: ", min_)
ind = mas1.index(min_)
print(ind)
del mas1[:ind]
print(mas1)

