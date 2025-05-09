

numbers = int(input("Введите 5-ти значное число: "))
a = numbers / 10000
b = numbers / 1000 % 10
c = numbers / 100 % 10
d = numbers / 10 % 10
e = numbers % 10

print("Произведение цифр числа " f"{numbers}: ", int(a)*int(b)*int(c)*int(d)*int(e))

print("Среднее арифметическое " f"{numbers}: ", int((a + b + c + d + e) / 5))

