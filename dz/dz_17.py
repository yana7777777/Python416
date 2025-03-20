# s = "I am learning Python. hello, WORLD!"
s = input("Введите строку: ")
# print(s.rfind('h') + 1)
a = s[:s.find('h')]  # s[:17]
b = s[s.find('h'):s.rfind('h') + 1]  # s[17:23]  # hon. h
c = s[s.rfind('h') + 1:]  # s[23:]
print(a + b[::-1] + c)

