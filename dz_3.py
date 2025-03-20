
num = int(input("Введите число от 1 до 99: "))
many = num
if 11 <= many <= 14:
    print(many, "копеек")
elif 1 <= num <= 10 or 15 <= num <= 99:
    many = many % 100
    if many == 1:
        print(many, "копейка")
    elif 2 <= many <= 4:
        print(many, "копейки")
    else:
        print(many, "копеек")
else:
    print("Значения должны быть от 1 до 99")
