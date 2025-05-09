def avg(fn):
    def wrap(*args):
        st = ""
        for i in args:
            st += str(i) + ", "
        print("Среднее арифметическое:", st[:-2], "=", fn(*args) / len(args))

    return wrap


@avg
def summa(*args):
    st = ", ".join(map(str, args))
    print("Сумма чисел:", st, "=", sum(args))
    return sum(args)


summa(2, 3, 3, 4)

