# перегрузка операторов (инф: словари и множества не работают с оператором +)
# число секунд в одном дне: 24 * 60 min * 60sec = 86400

class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом int")
        self.sec = sec

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec * other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec % other.sec)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec == other.sec

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec > other.sec

    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec >= other.sec

    def __lt__(self, other):
        return not self.__gt__(other)

    def __le__(self, other):
        return not self.__ge__(other)

# c1 = Clock(100)
# c2 = Clock(200)
# print(c1.get_format_time())
# print(c2.get_format_time())
# c1 += c2
# print(c1.get_format_time())


c1 = Clock(600)
print("c1:", c1.get_format_time())
c2 = Clock(200)
# print("c2:", c2.get_format_time())
c3 = c1 - c2
print("c1 - c2:", c3.get_format_time())
c3 = c1 * c2
print("c1 * c2:", c3.get_format_time())
c3 = c1 // c2
print("c1 // c2:", c3.get_format_time())
c3 = c1 % c2
print("c1 % c2:", c3.get_format_time())
c1 -= c2
print("c1 -= c2:", c1.get_format_time())
c1 *= c2
print("c1 *= c2:", c1.get_format_time())
c1 //= c2
print("c1 //= c2:", c1.get_format_time())
c1 %= c2
print("c1 %= c2:", c1.get_format_time())

print("*" * 30)

# операторы сравнений перегрузка
c1 = Clock(100)
c2 = Clock(100)
print("c1:", c1.get_format_time())
print("c2:", c2.get_format_time())
if c1 == c2:
    print("Время равно")
else:
    print("Время разное")
print("c1:", c1.get_format_time())
print("c2:", c2.get_format_time())
print("*" * 30)
c1 = Clock(100)
c2 = Clock(100)
c3 = c1 + c2
print("c1:", c1.get_format_time())
print("c2:", c2.get_format_time())
print("c3:", c3.get_format_time())
print("c3 > c1:", c3.get_format_time() > c1.get_format_time())
print("c3 >= c1:", c3.get_format_time() >= c1.get_format_time())
print("c3 < c1:", c3.get_format_time() < c1.get_format_time())
print("c3 <= c1:", c3.get_format_time() <= c1.get_format_time())

