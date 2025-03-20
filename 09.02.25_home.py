from random import randint

random_list1 = []
random_list = []
for i in range(10):
    random_list1.append(randint(1, 100))
print(random_list1)
random_list = random_list1.copy()
random_list.sort()
print(random_list)
min_ = random_list[0]
print(min_)
ind = random_list1.index(min_)
del random_list1[:ind]
print(random_list1)
del random_list1[ind:100]
print(random_list1)
