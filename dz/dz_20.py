def minus_number(n):
    if not n:
        return 0
    count = 0
    if n[0] < 0:
        count += 1
    return count + minus_number(n[1:])


lst = [-2, 3, 8, -11, -4, 6]
print(minus_number(lst))
