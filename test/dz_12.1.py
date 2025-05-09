dict_sales = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
              "Tom": {"N": 4832, "S": 6786, "E": 4773, "W": 3612},
              "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
              "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}

for x, y in dict_sales.items():
    print(x)
    for i, j in y.items():
        print("\t", i, ": ", j, sep="")

person = input("Имя: ")
region = input("Регин: ")
print(dict_sales[person][region])
new_data = int(input("Новое значение: "))
dict_sales[person][region] = new_data
print(dict_sales[person])
