
s1 = input("Введите первую строку: ")  #Python
s2 = input("Введите вторую строку: ")  #Programming Language

s = set(s1) - set(s2)
print(s)
print("Искомыми буквами являются: ")
for i in s:
    print(i, end=" ")

