import re


st = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, login-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'
reg = r"\w[0-9a-zA-Z][a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]"
print(re.findall(reg, st))
print(re.split(r".\s", st))









