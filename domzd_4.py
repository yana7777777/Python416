
num_symbol = int(input("Введите кол-во симоволов: "))
symbol = input("Введит тим символа: ")
line = int(input("0 - горизонтальная линия\n1 - вертикальная\nориентация линии: "))
i = 0
while i < num_symbol:
    if line == 0:
        print(symbol, end="")
    else:
        print(symbol)
    i += 1
